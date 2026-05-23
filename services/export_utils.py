def is_front_matter(section_key: str) -> bool:
    """Return True if the given SECTION key belongs to front‑matter.
    The set mirrors PAGE_BREAK_SECTIONS used in the PDF service.
    """
    front_sections = {
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
    return section_key in front_sections


def to_roman(num: int) -> str:
    """Convert an integer >=1 to a Roman numeral string.
    Simple implementation covering typical book front‑matter range.
    """
    if not (0 < num < 4000):
        raise ValueError("Roman numeral conversion supports 1‑3999")
    val = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    ]
    res = ""
    for (arabic, roman) in val:
        while num >= arabic:
            res += roman
            num -= arabic
    return res
