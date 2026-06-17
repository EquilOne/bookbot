import sys

from stats import count_words, get_char_list, get_num_chars, sort_on


def run_book_bot(path_to_book):
    book_text = get_book_text(path_to_book)
    word_count = count_words(book_text)
    sorted_list = get_sorted_list(book_text)
    print_report(path_to_book, word_count, sorted_list)


def get_book_text(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
    return file_contents


def get_sorted_list(book_text: str):
    char_count = get_num_chars(book_text)
    char_list = get_char_list(char_count)
    char_list.sort(reverse=True, key=sort_on)
    return char_list


def print_report(path_to_book, word_count, list):
    print("================= BOOKBOT =================\n")
    print(f"Analyzing book found at: {path_to_book}...\n")
    print("---------------- Word Count ---------------\n")
    print(f"Found {word_count} total words\n")
    print("------------- Character Count -------------\n")
    for item in list:
        print(f"{item[0]}: {item[1]}")


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    run_book_bot(sys.argv[1])

run_book_bot("books/frankenstein.txt")
