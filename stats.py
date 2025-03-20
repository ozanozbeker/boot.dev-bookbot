def count_words(book_text):
    words = 0
    for word in book_text.split():
        words += 1

    return words


def count_characters(book_text):
    characters = {}

    for character in book_text.lower():
        if character not in characters:
            characters[character] = 0
        characters[character] += 1

    return characters


def sort_character_count(character_dict):
    def sort_on(dict):
        return dict["count"]

    counts = []

    for character in character_dict:
        if character.isalpha():
            counts.append({"character": character, "count": character_dict[character]})

    counts.sort(key=sort_on, reverse=True)

    return counts
