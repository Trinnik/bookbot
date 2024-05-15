def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    char_count_list = convert_dict_list(get_character_count(file_contents))
    char_count_list.sort(reverse=True, key=sort_on)

    generate_char_report(char_count_list, book_path)


def generate_char_report(l:list, path: str):
    print(f"--- Begin report of {path} ---")
    for i in l:
        print(f"The '{i["char"]}' character was found {i["num"]} times.")
    print(f"--- End report ---")


def get_character_count(text):
    character_dict = {}

    for i in text:
        i_lower = i.lower()
        if i_lower in character_dict:
            character_dict[i_lower] += 1
        else:
            character_dict[i_lower] = 1

    return character_dict


def convert_dict_list(d: dict):
    dict_list = []

    for i in d:
        if i.isalpha():
            new_dict = {"char": i, "num": d[i]}
            dict_list.append(new_dict)

    return dict_list


def sort_on(dict):
    return dict["num"]


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()