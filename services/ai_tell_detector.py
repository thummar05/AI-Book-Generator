AI_TELLS = [

    "it's important to note",

    "in today's fast-paced world",

    "delve into",

    "landscape of",

    "not only",

    "but also",

    "plays a crucial role",

    "when it comes to",

    "a testament to",

    "navigate the complexities",

    "ever-evolving",

    "unlock the potential",

    "seamlessly",

    "robust",

    "furthermore",

    "moreover",

    "in conclusion"
]


def detect_ai_tells(
    text
):

    found = []

    lower_text = text.lower()

    for phrase in AI_TELLS:

        if phrase in lower_text:

            found.append(phrase)

    return found