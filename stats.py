def count_words(string):
    num_words = len(string.split())
    return num_words


def get_num_chars(string):
    char_count = {}
    for char in string:
        char = char.lower()
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count
