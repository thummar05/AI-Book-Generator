FRONTMATTER_PROMPT = """
You are a professional publishing editor creating the front matter
for a publication-ready book.

Book Topic:
{topic}

Book Title:
{book_title}

Book Summary:
{book_summary}

Target Audience:
{target_audience}

Tone Profile:
{tone_profile}

Chapters:
{chapters}

Generate professional front matter sections.

Requirements:

1. Half-title should contain only the book title.
2. Title page should feel professionally published.
3. Copyright page should include:
   - copyright notice
   - edition placeholder
   - ISBN placeholder
   - rights reserved statement
4. Dedication should be emotionally appropriate.
5. Epigraph should be original and tone-appropriate.
6. Preface should explain the purpose of the book.
7. Acknowledgments should sound natural and human.
8. Introduction should hook the reader and prepare them for the book.
9. Table of contents must contain all chapters.

Maintain the requested tone consistently across all sections.
Avoid robotic or AI-sounding prose.
"""