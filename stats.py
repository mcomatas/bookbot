def get_book_word_count(text):
    words = text.split()
    return len(words)


def get_book_letter_count(text):
    letters = text.lower().replace(" ", "").replace("\n", "")
    count = {}
    for letter in letters:
        if letter.isalpha():
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
    return count


def sort_letter_count(letters):
    sorted = []
    for letter in letters:
        sorted.append({"char": letter, "num": letters[letter]})

    def sort_on(items):
        return items["num"]

    sorted.sort(reverse=True, key=sort_on)
    return sorted
