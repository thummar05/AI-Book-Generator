# Fact Checker Prompt

## Purpose

The Fact Checker Prompt is responsible for validating and refining generated chapter content using retrieved research evidence.

It acts as a post-generation verification layer that:
- reduces hallucinations
- softens unsupported claims
- improves factual grounding
- attaches evidence-aware reasoning

This prompt operates after writing and editing stages within the LangGraph workflow.

---

## Inputs

### Generated Content
- `chapter_content`

### Research Evidence
- `research_context`

### Chapter Metadata
- `chapter_title`

### Tone Context
- `tone_profile`

---

## Outputs

Structured fact-checking output containing:
- revised chapter content
- identified claims
- verdicts
- confidence scores
- supporting evidence excerpts

The output is designed for downstream auditability and quality evaluation.

---

## Core Responsibilities

The fact checker agent must:

1. Verify factual claims against retrieved evidence.
2. Reduce hallucinated content.
3. Soften unsupported certainty.
4. Preserve readability and tone.
5. Avoid fabricated statistics or references.
6. Maintain narrative flow while correcting inaccuracies.
7. Return structured verification metadata.

---

## Hallucination Mitigation Strategy

Hallucination mitigation is the primary purpose of this prompt.

The system reduces hallucinations using:
- retrieval-augmented evidence
- citation-aware prompting
- confidence scoring
- conservative rewriting instructions
- evidence-grounded validation

The prompt explicitly instructs the model to:
- avoid invented facts
- avoid fabricated citations
- avoid unsupported claims
- prefer cautious language when evidence is weak

---

## Continuity Strategy

The fact checker preserves continuity by:
- avoiding excessive rewrites
- maintaining original chapter structure
- preserving callback references when valid
- preserving established terminology

The goal is corrective refinement rather than aggressive rewriting.

---

## Humanization Strategy

Humanization is preserved during fact checking through:
- minimal invasive edits
- conversational factual corrections
- natural uncertainty phrasing
- preservation of original rhythm and tone

The prompt discourages:
- robotic disclaimers
- excessive hedging
- repetitive correction patterns

---

## Failure Modes

Known limitations include:
- imperfect semantic verification
- occasional over-softening of claims
- inability to fully verify nuanced expertise domains
- dependence on retrieval quality

If retrieval evidence is weak, factual verification quality may degrade.

---

## Example Usage

```python
chain.invoke({

    "chapter_title":
        "Building Wealth Early",

    "chapter_content":
        "...",

    "research_context":
        "...",

    "tone_profile":
        "Conversational"
})
```

---

## Architectural Role

The fact checker is a critical component of the system's:
- hallucination mitigation pipeline
- grounded generation architecture
- evidence-aware AI workflow

It provides an additional verification layer between:
- generation
- publication
- evaluation