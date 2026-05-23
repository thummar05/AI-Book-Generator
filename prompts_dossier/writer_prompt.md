# Writer Prompt

## Purpose

The Writer Prompt is responsible for generating complete book chapters using:
- structured outline data
- retrieved research context
- callback memory
- character memory
- tone guidance
- continuity information

It acts as the primary long-form content generation agent within the LangGraph workflow.

---

## Inputs

### Book Metadata
- `book_title`
- `book_summary`

### Chapter Metadata
- `chapter_title`
- `chapter_summary`

### Tone + Audience
- `tone_profile`
- `target_audience`

### Memory Systems
- `memory_context`
- `callback_candidates`
- `character_memory`

### RAG Context
- `research_context`

---

## Outputs

Structured chapter object containing:
- chapter title
- full chapter content
- glossary terms
- callbacks used
- character references
- citations (if applicable)

---

## Core Responsibilities

The writer agent must:

1. Generate coherent long-form prose.
2. Maintain consistency with prior chapters.
3. Incorporate retrieved research naturally.
4. Preserve established tone and pacing.
5. Use callbacks when appropriate.
6. Avoid repetitive AI phrasing.
7. Generate publication-quality chapter structure.

---

## Hallucination Mitigation Strategy

Hallucination reduction is implemented through:
- retrieval-augmented generation (RAG)
- source-grounded research context
- fact-checking post-processing
- conservative prompting
- explicit anti-fabrication instructions

The prompt explicitly instructs the model to:
- avoid fabricated statistics
- avoid fake citations
- avoid unsupported claims
- prefer uncertainty over invention

---

## Continuity Strategy

Continuity is preserved using:
- callback retrieval
- chapter memory retrieval
- character memory retrieval
- downstream regeneration workflows

The writer agent receives contextual memory from previous chapters to maintain:
- narrative consistency
- terminology consistency
- callback alignment
- character continuity

---

## Humanization Strategy

Humanization is achieved through:
- conversational tone prompting
- rhythm variation post-processing
- hook generation
- AI-tell detection
- tone-aware rewriting

The system avoids:
- robotic transitions
- repetitive sentence cadence
- generic AI prose patterns

---

## Failure Modes

Known limitations include:
- occasional overuse of callbacks
- possible verbosity in explanatory sections
- imperfect metaphor generation
- limited deep semantic narrative tracking

Long-context degradation may occur in very large books.

---

## Example Usage

```python
chain.invoke({

    "book_title":
        "Money Moves",

    "chapter_title":
        "Budgeting Basics",

    "research_context":
        "...",

    "memory_context":
        "...",

    "callback_candidates":
        "...",

    "tone_profile":
        "Conversational"
})
```