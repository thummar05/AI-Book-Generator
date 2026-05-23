# Researcher Prompt

## Purpose

The Researcher Prompt is responsible for gathering, structuring, and ingesting grounded research context for downstream chapter generation.

It powers the platform's retrieval-augmented generation (RAG) pipeline by:
- preparing research context
- chunking source material
- storing embeddings
- enabling retrieval-backed writing

The researcher agent operates before long-form chapter generation begins.

---

## Inputs

### Book Structure
- chapter titles
- chapter summaries
- book topic

### Source Materials
- uploaded PDFs
- extracted text
- internal knowledge content
- curated reference material

### Research Configuration
- chunking strategy
- embedding strategy
- retrieval metadata

---

## Outputs

Structured research artifacts including:
- chunked research content
- vector embeddings
- source metadata
- retrieval-ready context

The resulting data is persisted into the vector store for downstream retrieval.

---

## Core Responsibilities

The researcher agent must:

1. Prepare grounded source material.
2. Chunk research intelligently.
3. Preserve source traceability.
4. Store retrieval-ready embeddings.
5. Improve factual grounding.
6. Support downstream hallucination mitigation.
7. Enable context-aware writing.

---

## Hallucination Mitigation Strategy

The researcher is a foundational hallucination reduction layer.

Hallucination mitigation is achieved through:
- retrieval-augmented generation (RAG)
- source-grounded context
- vector similarity retrieval
- evidence-aware writing support

The researcher improves downstream factual reliability by:
- providing grounded retrieval context
- reducing unsupported generation
- improving terminology consistency

---

## Continuity Strategy

The researcher indirectly supports continuity by:
- maintaining terminology consistency
- preserving domain-specific context
- enabling retrieval across chapters
- reinforcing established concepts

This helps downstream agents maintain:
- thematic consistency
- factual continuity
- conceptual alignment

---

## Humanization Strategy

The researcher itself does not directly humanize prose.

However, it indirectly improves writing quality by:
- supplying concrete examples
- improving contextual richness
- reducing generic filler explanations
- grounding explanations in realistic material

This enables more natural downstream prose generation.

---

## Failure Modes

Known limitations include:
- retrieval quality dependence
- chunking boundary imperfections
- embedding similarity limitations
- possible retrieval redundancy

Poor-quality source material may reduce factual grounding effectiveness.

---

## Example Usage

```python
ingest_research(

    topic="Investing Basics",

    source="finance_guide.pdf",

    content="..."
)
```

---

## Architectural Role

The researcher is a foundational component of the platform's:
- RAG architecture
- factual grounding pipeline
- retrieval system
- hallucination mitigation workflow

It enables downstream agents to generate more reliable and context-aware long-form content.