import sys

from stats import get_book_letter_count, get_book_word_count, sort_letter_count


def get_book_text(filepath):
    with open(filepath, "r") as f:
        contents = f.read()
        return contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    text = get_book_text(book)
    words = get_book_word_count(text)
    letters = get_book_letter_count(text)
    sorted = sort_letter_count(letters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for c in sorted:
        print(f"{c['char']}: {c['num']}")


main()
