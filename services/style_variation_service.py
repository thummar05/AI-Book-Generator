import random


def vary_sentence_rhythm(
    text
):

    sentences = text.split(". ")

    varied = []

    for idx, sentence in enumerate(
        sentences
    ):

        sentence = sentence.strip()

        if not sentence:
            continue

        # occasionally shorten
        if idx % 5 == 0:

            varied.append(sentence)

            continue

        # occasionally extend
        if idx % 3 == 0:

            sentence = (
                sentence +
                ", creating a more natural flow"
            )

        varied.append(sentence)

    return ". ".join(varied)