from langchain_core.prompts import ChatPromptTemplate

from prompts.planner_prompt import PLANNER_PROMPT
from prompts.tone_profiles import TONE_PROFILES

from models.planner_models import PlannerOutput

from services.llm_service import planner_llm


def planner_node(state):

    brief = state["brief"]

    tone_profile = TONE_PROFILES.get(
        brief["tone"],
        {}
    )

    prompt = ChatPromptTemplate.from_template(
        PLANNER_PROMPT
    )

    structured_llm = planner_llm.with_structured_output(
        PlannerOutput
    )

    chain = prompt | structured_llm

    result = chain.invoke({
        "topic": brief["topic"],
        "tone": brief["tone"],
        "target_audience": brief["target_audience"],
        "chapters": brief["chapters"],
        "tone_profile": tone_profile
    })

    state["outline"] = result.model_dump()

    state["tone_profile"] = tone_profile


    return state