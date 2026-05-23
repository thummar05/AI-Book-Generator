
# Humanizer Prompt

## Purpose

The Humanizer Prompt is responsible for transforming structurally correct AI-generated prose into more natural, engaging, and human-feeling writing.

It operates after chapter generation and before final evaluation.

The humanization layer improves:
- conversational flow
- sentence rhythm
- emotional resonance
- readability
- narrative engagement

while reducing:
- robotic phrasing
- repetitive cadence
- generic AI writing patterns

---

## Inputs

### Generated Chapter Content
- `chapter_content`

### Tone Guidance
- `tone_profile`

### Audience Information
- `target_audience`

### Chapter Metadata
- `chapter_title`

---

## Outputs

Humanized long-form prose that:
- preserves factual meaning
- preserves structure
- improves natural readability
- reduces AI tell patterns

The output remains compatible with downstream:
- fact checking
- evaluation
- publishing

---

## Core Responsibilities

The humanizer agent must:

1. Improve conversational flow.
2. Vary sentence rhythm naturally.
3. Reduce repetitive AI structures.
4. Improve readability and pacing.
5. Preserve the requested tone.
6. Preserve factual meaning.
7. Maintain narrative continuity.

---

## Hallucination Mitigation Strategy

The humanizer is intentionally constrained to stylistic rewriting rather than factual expansion.

Hallucination mitigation includes:
- preserving core meaning
- discouraging invention of new facts
- avoiding unsupported examples
- minimizing semantic drift

The prompt explicitly prioritizes:
- style refinement
over
- content invention

---

## Continuity Strategy

The humanizer preserves continuity by:
- maintaining established terminology
- preserving callbacks
- preserving chapter intent
- avoiding structural reorganization

The goal is enhancement rather than rewriting.

---

## Humanization Strategy

Humanization is achieved through:
- conversational phrasing
- sentence length variation
- rhythm modulation
- hook injection
- transition softening
- AI tell reduction
- natural emphasis patterns

The system also includes:
- AI tell detection
- cadence variation utilities
- tone-aware hook generation

The prompt discourages:
- repetitive transitions
- corporate phrasing
- generic motivational clichés
- over-formal explanations

---

## Failure Modes

Known limitations include:
- occasional over-conversational phrasing
- imperfect stylistic consistency
- limited metaphor diversity
- possible verbosity increases

Heavy humanization may occasionally soften technical precision.

---

## Example Usage

```python
chain.invoke({

    "chapter_title":
        "Budgeting Basics",

    "chapter_content":
        "...",

    "tone_profile":
        "Conversational",

    "target_audience":
        "Young Professionals"
})
```

---

## Architectural Role

The humanizer is a core component of the platform's:
- prose refinement pipeline
- AI tell reduction system
- tone enhancement architecture
- publication quality workflow

It significantly improves perceived writing quality and reader engagement.