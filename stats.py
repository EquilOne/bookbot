def count_words(string: str) -> int:
    num_words = len(string.split())
    return num_words


def get_num_chars(string: str) -> dict[str, int]:
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


def sort_on(entry: tuple[str, int]) -> int:
    return entry[1]


def get_char_list(dict: dict[str, int]) -> list[tuple[str, int]]:
    char_list = []
    for k, v in dict.items():
        char_tuple = (k, v)
        char_list.append(char_tuple)
    return char_list
