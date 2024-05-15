def main():
    file_contents = get_book_text("books/frankenstein.txt")

    print(get_character_count(file_contents))


def get_character_count(text):
    character_dict = {}

    for i in text:
        i_lower = i.lower()
        if i_lower in character_dict:
            character_dict[i_lower] += 1
        else:
            character_dict[i_lower] = 1

    return character_dict


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()