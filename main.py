from stats import count_words
from stats import get_num_chars


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


char_count_list = get_num_chars(get_book_text("./books/frankenstein.txt"))

print(f"Found {count_words(get_book_text('./books/frankenstein.txt'))} total words")
print(f"List of characters in text: {char_count_list}")
