def generate_hook(topic, tone):

    hooks = {

        "Conversational":
            f"Let's be honest — {topic} can feel overwhelming at first.",

        "Motivational":
            f"Your future changes the moment you take control of {topic}.",

        "Storyteller":
            f"Every journey begins somewhere, and this one begins with {topic}.",

        "Academic":
            f"Understanding {topic} requires both theory and practical insight.",

        "Witty":
            f"{topic} is a lot like assembling furniture without instructions."
    }

    return hooks.get(
        tone,
        f"{topic} matters more than most people realize."
    )