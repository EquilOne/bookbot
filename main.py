from stats import count_words
from stats import get_num_chars
from stats import get_char_list
from stats import sort_on

frankenstein = "./books/frankenstein.txt"


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def print_report():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {frankenstein}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(get_book_text(frankenstein))} total words")
    print("-------- Character Count --------")
    for item in char_list:
        print(f"{item['char']}: {item['num']}")


char_count_dict = get_num_chars(get_book_text(frankenstein))

char_list = get_char_list(char_count_dict)

char_list.sort(reverse=True, key=sort_on)

print_report()
# print(f"{char_list[0]['char']}: {char_list[0]['num']}")
