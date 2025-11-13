def count_words(string):
    num_words = len(string.split())
    return num_words


def get_num_chars(string):
    char_count = {}
    for char in string:
        char_low = char.lower()
        if not char_low.isalpha():
            continue
        elif char_low not in char_count:
            char_count[char_low] = 1
        else:
            char_count[char_low] += 1
    return char_count


def sort_on(entry):
    return entry["num"]


def get_char_list(dict):
    char_list = []
    for k, v in dict.items():
        char_dict = {"char": k, "num": v}
        char_list.append(char_dict)
    return char_list
