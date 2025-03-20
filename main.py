from stats import count_words, count_characters, sort_character_count
import sys


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()


def main():
    file_path = sys.argv[1]

    book_text = get_book_text(file_path)
    word_count = count_words(book_text)
    character_count = count_characters(book_text)
    characters_sorted = sort_character_count(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for pair in characters_sorted:
        print(f"{pair["character"]}: {pair["count"]}")

    print("============= END ===============")


main()
