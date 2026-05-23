# Planner Prompt

## Purpose

The Planner Prompt is responsible for generating the high-level structure of the book before long-form content generation begins.

It creates:
- book title
- book summary
- chapter sequencing
- chapter titles
- chapter summaries

The planner acts as the orchestration foundation for the entire LangGraph workflow.

---

## Inputs

### User Brief
- topic
- target audience
- tone
- desired depth
- optional constraints

### System Guidance
- long-form structure instructions
- pacing expectations
- educational or narrative goals

---

## Outputs

Structured outline data containing:
- book title
- book summary
- ordered chapter list
- chapter metadata
- chapter summaries

This output becomes the primary planning artifact used by downstream agents.

---

## Core Responsibilities

The planner agent must:

1. Create a coherent long-form structure.
2. Sequence chapters logically.
3. Maintain topic progression.
4. Align structure with target audience.
5. Match requested tone and complexity.
6. Create balanced chapter scope.
7. Prepare the foundation for downstream generation.

---

## Hallucination Mitigation Strategy

The planner minimizes hallucinations by:
- operating at structural level only
- avoiding unsupported factual detail generation
- focusing on organization rather than factual claims

The planner intentionally avoids:
- fabricated statistics
- fake citations
- unsupported technical assertions

This reduces risk early in the pipeline.

---

## Continuity Strategy

Continuity begins at the planning stage.

The planner creates:
- logical topic progression
- thematic continuity
- chapter dependency flow
- callback opportunities

The resulting outline acts as the continuity backbone for:
- memory retrieval
- callback generation
- downstream regeneration

---

## Humanization Strategy

Humanization at the planning layer includes:
- emotionally engaging chapter titles
- audience-aware summaries
- conversational framing
- narrative progression awareness

The planner avoids:
- sterile academic sequencing
- repetitive chapter naming
- generic educational framing

---

## Failure Modes

Known limitations include:
- occasional chapter overlap
- uneven chapter granularity
- imperfect pacing estimation
- limited deep narrative arc modeling

Very broad topics may require additional planning refinement.

---

## Example Usage

```python
chain.invoke({

    "topic":
        "Personal Finance",

    "target_audience":
        "Young Professionals",

    "tone":
        "Conversational",

    "depth":
        "Beginner Friendly"
})
```

---

## Architectural Role

The planner is the foundational orchestration layer of the platform.

It provides:
- structural guidance
- sequencing logic
- continuity scaffolding
- downstream generation context

All major agents depend on planner outputs to maintain coherence across the full book generation pipeline.