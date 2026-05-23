# Evaluator Prompt

## Purpose

The Evaluator Prompt is responsible for assessing the quality of generated book chapters using an LLM-as-judge architecture.

It evaluates:
- tone fidelity
- humanization quality
- structural quality
- callback consistency
- factual grounding

The evaluator operates as a post-generation quality assessment layer within the LangGraph workflow.

---

## Inputs

### Generated Content
- `chapter_content`

### Requested Tone
- `tone`

### Evaluation Criteria
Implicit scoring criteria defined in the prompt instructions.

---

## Outputs

Structured evaluation output containing:
- tone fidelity score
- humanization score
- structural quality score
- callback consistency score
- factual grounding score
- overall score
- strengths
- weaknesses
- detected issues

Scores are normalized between 0 and 10.

---

## Core Responsibilities

The evaluator agent must:

1. Assess adherence to requested tone.
2. Detect robotic AI prose patterns.
3. Evaluate conversational naturalness.
4. Evaluate chapter structure and readability.
5. Evaluate continuity consistency.
6. Assess factual grounding quality.
7. Produce structured evaluation metadata.

---

## Hallucination Mitigation Strategy

Although the evaluator does not directly rewrite content, it contributes to hallucination mitigation by:
- penalizing unsupported certainty
- identifying weak factual grounding
- reducing reward for fabricated claims
- rewarding evidence-aware prose

This creates a feedback-oriented evaluation layer for generated content quality.

---

## Continuity Strategy

Continuity evaluation includes:
- callback consistency assessment
- terminology consistency
- narrative coherence
- chapter-to-chapter alignment

The evaluator rewards chapters that:
- maintain thematic consistency
- preserve established concepts
- avoid abrupt tonal shifts

---

## Humanization Strategy

Humanization scoring focuses on:
- sentence rhythm variation
- conversational flow
- emotional resonance
- natural phrasing
- reduced AI tell frequency

The evaluator penalizes:
- repetitive sentence structure
- generic AI transitions
- robotic explanatory patterns
- overly formal phrasing

---

## Failure Modes

Known limitations include:
- subjective evaluation variance
- imperfect literary judgment
- occasional over-penalization of formal writing
- limited deep narrative interpretation

Evaluation quality depends on:
- prompt quality
- model capability
- chapter complexity

---

## Example Usage

```python
evaluate_chapter(

    tone="Conversational",

    chapter_content="..."
)
```

---

## Architectural Role

The evaluator is a core component of the platform's:
- quality assurance architecture
- LLM-as-judge evaluation pipeline
- humanization scoring system
- tone fidelity assessment workflow

It enables measurable quality analysis for generated long-form content.