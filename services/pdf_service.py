import re

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

from reportlab.lib.enums import (
    TA_CENTER,
    TA_LEFT,
    TA_JUSTIFY
)

from reportlab.lib.pagesizes import LETTER

from reportlab.lib.units import inch


def generate_pdf(book_text, output_path):

    doc = SimpleDocTemplate(
        output_path,
        pagesize=LETTER,
        rightMargin=1.25 * inch,
        leftMargin=1.25 * inch,
        topMargin=1.25 * inch,
        bottomMargin=1.25 * inch
    )

    styles = getSampleStyleSheet()

    # ==========================================
    # CUSTOM STYLES
    # ==========================================

    section_title_style = ParagraphStyle(
        "SectionTitleStyle",
        parent=styles["Heading1"],
        alignment=TA_CENTER,
        fontSize=26,
        leading=32,
        spaceBefore=20,
        spaceAfter=20,
        fontName="Helvetica-Bold",
        leftIndent=0,
        rightIndent=0
    )

    chapter_label_style = ParagraphStyle(
        "ChapterLabelStyle",
        parent=styles["Heading1"],
        alignment=TA_LEFT,
        fontSize=14,
        leading=18,
        spaceBefore=10,
        spaceAfter=4,
        fontName="Helvetica-Bold",
        textColor=(0.4, 0.4, 0.4),
        leftIndent=0,
        rightIndent=0
    )

    chapter_title_style = ParagraphStyle(
        "ChapterTitleStyle",
        parent=styles["Heading1"],
        alignment=TA_LEFT,
        fontSize=22,
        leading=28,
        spaceBefore=4,
        spaceAfter=24,
        fontName="Helvetica-Bold",
        leftIndent=0,
        rightIndent=0
    )

    section_heading_style = ParagraphStyle(
        "SectionHeadingStyle",
        parent=styles["Heading2"],
        alignment=TA_LEFT,
        fontSize=14,
        leading=18,
        spaceBefore=18,
        spaceAfter=8,
        fontName="Helvetica-Bold",
        leftIndent=0,
        rightIndent=0
    )

    body_style = ParagraphStyle(
        "BodyStyle",
        parent=styles["BodyText"],
        fontSize=11,
        leading=18,
        spaceAfter=10,
        alignment=TA_JUSTIFY,
        leftIndent=0,
        rightIndent=0
    )

    toc_style = ParagraphStyle(
        "TOCStyle",
        parent=styles["Normal"],
        fontSize=11,
        leading=20,
        spaceAfter=4,
        alignment=TA_JUSTIFY,
        leftIndent=0,
        rightIndent=0
    )

    term_style = ParagraphStyle(
        "TermStyle",
        parent=styles["Normal"],
        fontSize=12,
        leading=16,
        spaceBefore=12,
        spaceAfter=2,
        fontName="Helvetica-Bold",
        leftIndent=0,
        rightIndent=0
    )

    def_style = ParagraphStyle(
        "DefStyle",
        parent=styles["BodyText"],
        fontSize=11,
        leading=16,
        spaceAfter=8,
        alignment=TA_JUSTIFY,
        leftIndent=18,
        rightIndent=0
    )

    # ==========================================
    # SECTIONS THAT GET A PAGE BREAK BEFORE THEM
    # ==========================================

    PAGE_BREAK_SECTIONS = {
        "HALF_TITLE",
        "TITLE_PAGE",
        "COPYRIGHT",
        "DEDICATION",
        "EPIGRAPH",
        "TOC",
        "ACKNOWLEDGMENTS",
        "INTRODUCTION",
        "GLOSSARY",
        "ABOUT_AUTHOR",
        "BACK_COVER",
        "PREFACE",
        "AFTERWORD",
        "APPENDIX",
        "REFERENCES",
    }

    # ==========================================
    # SECTION DISPLAY NAMES
    # ==========================================

    SECTION_LABELS = {
        "HALF_TITLE":      None,
        "TITLE_PAGE":      None,
        "COPYRIGHT":       "Copyright",
        "DEDICATION":      "Dedication",
        "EPIGRAPH":        None,
        "TOC":             "Table of Contents",
        "ACKNOWLEDGMENTS": "Acknowledgments",
        "INTRODUCTION":    "Introduction",
        "GLOSSARY":        "Glossary",
        "ABOUT_AUTHOR":    "About the Author",
        "BACK_COVER":      "Back Cover",
        "PREFACE":         "Preface",
        "AFTERWORD":       "Afterword",
        "APPENDIX":        "Appendix",
        "REFERENCES":      "References",
    }

    story = []
    # Track the page number where INTRODUCTION begins (1‑based)
    intro_start_page = None
    # Count how many physical pages have been added via PageBreak
    page_counter = 0

    current_section = None
    in_chapter = False
    chapter_num = None
    is_first_section = True

    lines = book_text.split("\n")

    i = 0
    intro_start_page = None  # 1‑based page where Introduction begins
    page_counter = 0  # counts pages added via PageBreak
        
    while i < len(lines):
        line = lines[i]
            
        # SECTION TAG handling
        section_match = re.match(r"^\[SECTION:(\w+)\]$", line.strip())
        if section_match:
            section_key = section_match.group(1)
            current_section = section_key
            in_chapter = False
            # Add page break before section if needed
            if section_key in PAGE_BREAK_SECTIONS and not is_first_section:
                story.append(PageBreak())
                page_counter += 1
                # If this is the INTRODUCTION, record the start page after the break
                if section_key == "INTRODUCTION" and intro_start_page is None:
                    intro_start_page = page_counter
            else:
                # For sections that don't trigger a break, still record intro start if it's INTRODUCTION
                if section_key == "INTRODUCTION" and intro_start_page is None:
                    intro_start_page = page_counter + 1
            is_first_section = False
            label = SECTION_LABELS.get(section_key)
            if label:
                story.append(Paragraph(label, section_title_style))
                story.append(Spacer(1, 12))

            i += 1
            continue

        # ==========================================
        # CHAPTER TAG
        # ==========================================

        chapter_match = re.match(
            r"^\[CHAPTER:(\d+)\]$",
            line.strip()
        )

        if chapter_match:

            chapter_num = chapter_match.group(1)
            in_chapter = True
            current_section = None

            story.append(PageBreak())
            page_counter += 1

            story.append(
                Paragraph(
                    f"Chapter {chapter_num}",
                    chapter_label_style
                )
            )

            i += 1
            continue

        # ==========================================
        # CHAPTER TITLE TAG
        # ==========================================

        chapter_title_match = re.match(
            r"^\[CHAPTER_TITLE\](.*?)\[/CHAPTER_TITLE\]$",
            line.strip()
        )

        if chapter_title_match:

            title_text = chapter_title_match.group(1).strip()

            story.append(
                Paragraph(title_text, chapter_title_style)
            )

            i += 1
            continue

        # ==========================================
        # GLOSSARY TERM TAG
        # ==========================================

        term_match = re.match(
            r"^\[TERM\](.*?)\[/TERM\]$",
            line.strip()
        )

        if term_match:

            story.append(
                Paragraph(
                    term_match.group(1).strip(),
                    term_style
                )
            )

            i += 1
            continue

        # ==========================================
        # GLOSSARY DEFINITION TAG
        # ==========================================

        def_match = re.match(
            r"^\[DEF\](.*?)\[/DEF\]$",
            line.strip()
        )

        if def_match:

            story.append(
                Paragraph(
                    def_match.group(1).strip(),
                    def_style
                )
            )

            i += 1
            continue

        # ==========================================
        # BLANK LINE
        # ==========================================

        if not line.strip():
            story.append(Spacer(1, 6))
            i += 1
            continue

        # ==========================================
        # CONTENT LINES
        # ==========================================

        text = line.strip()

        # TOC entries
        if current_section == "TOC":
            story.append(Paragraph(text, toc_style))
            i += 1
            continue

        # Half title / title page — render as big centered title
        if current_section in ("HALF_TITLE", "TITLE_PAGE"):
            story.append(
                Paragraph(text, section_title_style)
            )
            i += 1
            continue

        # Epigraph — centered body text
        if current_section == "EPIGRAPH":
            epigraph_style = ParagraphStyle(
                "EpigraphStyle",
                parent=body_style,
                alignment=TA_CENTER,
                fontSize=12,
                leading=20,
                leftIndent=40,
                rightIndent=40,
                fontName="Helvetica-Oblique"
            )
            story.append(Paragraph(text, epigraph_style))
            i += 1
            continue

        # Inside a chapter — detect inline section headings
        # A heading is a line that is bold-formatted by the LLM,
        # typically wrapped in ** or is a short standalone line
        # followed by a blank line
        if in_chapter:

            is_heading = False

            # Bold markdown heading: **Some Title**
            bold_match = re.match(
                r"^\*\*(.*?)\*\*$",
                text
            )

            if bold_match:
                story.append(
                    Paragraph(
                        bold_match.group(1),
                        section_heading_style
                    )
                )
                is_heading = True

            if not is_heading:
                story.append(Paragraph(text, body_style))

            i += 1
            continue

        # Default: body text
        story.append(Paragraph(text, body_style))
        i += 1

    # After building the document, add page numbers using the computed ``intro_start_page``.
    def int_to_roman(n):
        val = [
            1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
            ]
        syb = [
            "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
            ]
        roman_num = ''
        i = 0
        while  n > 0:
            for _ in range(n // val[i]):
                roman_num += syb[i]
                n -= val[i]
            i += 1
        return roman_num

    # Add page numbers to the PDF using ReportLab canvas callbacks
    def _add_page_numbers(canvas, doc):
        page_num = canvas.getPageNumber()
        # Determine label based on intro start
        if intro_start_page and page_num < intro_start_page:
            label = int_to_roman(page_num)
        else:
            # Arabic numbering restarts at 1 for the introduction
            start = intro_start_page if intro_start_page else 1
            label = str(page_num - start + 1)
        canvas.saveState()
        canvas.setFont("Helvetica", 9)
        canvas.drawCentredString(
            doc.pagesize[0] / 2,
            0.5 * inch,
            label,
        )
        canvas.restoreState()

    doc.build(story, onFirstPage=_add_page_numbers, onLaterPages=_add_page_numbers)
    return output_path
