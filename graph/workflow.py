from langgraph.graph import StateGraph, END

from graph.state import BookState

from graph.nodes.planner import planner_node
from graph.nodes.researcher import researcher_node
from graph.nodes.memory_keeper import memory_keeper_node
from graph.nodes.writer import writer_node
from graph.nodes.humanizer import humanizer_node
from graph.nodes.editor import editor_node
from graph.nodes.fact_checker import fact_checker_node
from graph.nodes.assembler import assembler_node
from graph.nodes.frontmatter import (
    frontmatter_node
)

from graph.nodes.backmatter import (
    backmatter_node
)

from graph.nodes.evaluator import (
    evaluator_node
)

def build_graph():

    workflow = StateGraph(BookState)

    workflow.add_node("planner", planner_node)
    
    workflow.add_node("frontmatter",frontmatter_node)

    workflow.add_node("researcher", researcher_node)

    workflow.add_node("memory_keeper", memory_keeper_node)

    workflow.add_node("writer", writer_node)

    workflow.add_node("humanizer", humanizer_node)

    workflow.add_node("editor", editor_node)

    workflow.add_node("fact_checker", fact_checker_node)

    workflow.add_node(
    "backmatter",
    backmatter_node
)
    
    workflow.add_node(
    "evaluator",
    evaluator_node
)

    workflow.add_node("assembler", assembler_node)

    workflow.set_entry_point("planner")

    workflow.add_edge(
    "planner",
    "frontmatter"
)

    workflow.add_edge(
        "frontmatter",
        "researcher"
    )

    workflow.add_edge("researcher", "writer")

    workflow.add_edge("writer", "humanizer")

    workflow.add_edge("humanizer", "editor")

    workflow.add_edge("editor", "fact_checker")

    # Move memory keeper after fact checking
    workflow.add_edge("fact_checker", "memory_keeper")
    workflow.add_edge("memory_keeper", "backmatter")

    workflow.add_edge(
        "backmatter",
        "evaluator"
    )

    workflow.add_edge(
        "evaluator",
        "assembler"
    )

    workflow.add_edge("assembler", END)

    return workflow.compile()