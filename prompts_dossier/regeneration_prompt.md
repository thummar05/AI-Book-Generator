# Regeneration Prompt

## Purpose

The Regeneration Prompt is responsible for repairing and regenerating book chapters after upstream chapter modifications.

It powers the system's self-healing continuity architecture by selectively regenerating affected chapters while preserving:
- tone
- narrative consistency
- callback continuity
- character consistency
- factual grounding

This prompt is used during the repair workflow and downstream continuity regeneration pipeline.

---

## Inputs

### Book Metadata
- `book_title`

### Chapter Metadata
- `chapter_title`

### Original Chapter State
- `original_content`

### Repair Context
- `changed_chapter`
- `updated_content`

### Tone + Style
- `tone_profile`

### Memory Systems
- `memory_context`
- `callback_candidates`
- `character_memory`

---

## Outputs

Regenerated chapter content that:
- preserves continuity
- incorporates upstream changes
- maintains narrative coherence
- preserves established tone

The output is returned as regenerated long-form prose.

---

## Core Responsibilities

The regeneration agent must:

1. Repair downstream continuity after chapter modifications.
2. Preserve the original tone and pacing.
3. Maintain callback consistency.
4. Preserve important concepts from the original chapter.
5. Maintain character continuity.
6. Adapt naturally to upstream changes.
7. Avoid obvious rewrite artifacts.

---

## Hallucination Mitigation Strategy

Hallucination reduction is implemented through:
- memory retrieval
- callback retrieval
- character retrieval
- continuity-aware prompting
- grounded regeneration instructions

The prompt explicitly discourages:
- fabricated narrative changes
- unsupported factual additions
- abrupt continuity shifts
- contradictory callbacks

The regeneration workflow prefers conservative rewriting over aggressive content replacement.

---

## Continuity Strategy

Continuity preservation is the central responsibility of this prompt.

The system maintains continuity through:
- chapter memory retrieval
- callback candidate retrieval
- downstream dependency tracking
- selective regeneration workflows
- character memory persistence

The prompt receives:
- original chapter content
- updated upstream chapter content
- prior memory context

This allows the regeneration agent to preserve:
- narrative flow
- thematic consistency
- callback alignment
- pacing continuity

---

## Humanization Strategy

Humanization is preserved during regeneration by:
- maintaining original prose rhythm
- preserving conversational tone
- avoiding robotic rewrite patterns
- minimizing repetitive transitions
- preserving stylistic fingerprints

The prompt specifically instructs the model to:
- regenerate naturally
- avoid sounding patched or rewritten
- maintain emotional flow

---

## Failure Modes

Known limitations include:
- occasional over-preservation of outdated context
- imperfect callback adaptation
- partial continuity drift in long books
- possible redundancy during heavy regeneration

Large-scale upstream changes may require broader regeneration than currently implemented.

---

## Example Usage

```python
variables = {

    "book_title":
        "Money Moves",

    "chapter_title":
        "Investing Early",

    "original_content":
        "...",

    "changed_chapter":
        2,

    "updated_content":
        "...",

    "tone_profile":
        "Conversational",

    "memory_context":
        "...",

    "callback_candidates":
        "...",

    "character_memory":
        "..."
}

regenerate_chapter_content(
    variables
)
```

---

## Architectural Role

The regeneration prompt is a core component of the system's:
- self-healing architecture
- selective repair pipeline
- continuity-preserving orchestration

It enables the platform to modify books incrementally without requiring full-book regeneration.