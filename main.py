from stats import count_words
from stats import get_num_chars
# from stats import sort_on

frankenstein = "./books/frankenstein.txt"


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


char_count_list = get_num_chars(get_book_text(frankenstein))

print("============ BOOKBOT ============")
print(f"Analyzing book found at {frankenstein}...")
print("----------- Word Count ----------")
print(f"Found {count_words(get_book_text(frankenstein))} total words")
print("-------- Character Count --------")
print(f"List of characters in text: {char_count_list}")
