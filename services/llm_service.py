from langchain_openai import ChatOpenAI


planner_llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.7
)

writer_llm = ChatOpenAI(
    model="gpt-4.1",
    temperature=0.9
)

editor_llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.3
)

judge_llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2
)