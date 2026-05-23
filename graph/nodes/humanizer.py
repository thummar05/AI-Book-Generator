from langchain_core.prompts import ChatPromptTemplate

from prompts.humanizer_prompt import (
    HUMANIZER_PROMPT
)

from models.humanizer_models import (
    HumanizerOutput
)

from services.llm_service import writer_llm

from services.ai_tell_detector import (
    detect_ai_tells
)

from services.style_variation_service import (
    vary_sentence_rhythm
)

from services.hook_generator_service import (
    generate_hook
)


def humanizer_node(state):
    """Humanizes each chapter's content.

    Steps:
    1. Generate a humanized version via LLM.
    2. Detect AI‑tells in the humanized text.
    3. Apply rhythm variation on the humanized text.
    4. Generate a tone‑appropriate hook and prepend it.
    5. Record callbacks added by the LLM.
    """
    updated_chapters = []

    for chapter in state["chapters"]:
        # --------------------------------------------------
        # 1. Humanize content via LLM
        # --------------------------------------------------
        prompt = ChatPromptTemplate.from_template(HUMANIZER_PROMPT)
        structured_llm = writer_llm.with_structured_output(HumanizerOutput)
        chain = prompt | structured_llm
        result = chain.invoke({
            "tone_profile": state["tone_profile"],
            "chapter_content": chapter["content"]
        })
        # Store the LLM‑generated humanized text
        humanized = result.humanized_content

        # --------------------------------------------------
        # 2. Detect AI‑tells in the humanized text
        # --------------------------------------------------
        detected_tells = detect_ai_tells(humanized)

        # --------------------------------------------------
        # 3. Apply rhythm variation (LLM‑guided or heuristic)
        # --------------------------------------------------
        varied_content = vary_sentence_rhythm(humanized)

        # --------------------------------------------------
        # 4. Generate a hook based on the chapter title and tone
        # --------------------------------------------------
        tone = state["brief"]["tone"]
        hook = generate_hook(topic=chapter["title"], tone=tone)

        # --------------------------------------------------
        # 5. Assemble final chapter content
        # --------------------------------------------------
        final_content = f"{hook}\n\n{varied_content}"
        chapter["content"] = final_content

        # --------------------------------------------------
        # 6. Record metadata
        # --------------------------------------------------
        chapter["ai_tells_detected"] = detected_tells
        # Ensure the callbacks list exists before extending
        if "callbacks_used" not in chapter or not isinstance(chapter["callbacks_used"], list):
            chapter["callbacks_used"] = []
        chapter["callbacks_used"].extend(result.callbacks_added)

        updated_chapters.append(chapter)

    state["chapters"] = updated_chapters
    return state