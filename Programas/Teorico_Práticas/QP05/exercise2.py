def camel_case(phrase):
    phrase = phrase.title()
    phrase = phrase.title()
    phrase = phrase[0].lower() + phrase[1:]
    for character in phrase:
        if not character.isalpha():
            phrase = phrase.replace(character, "")
    return phrase
