from functools import lru_cache
from collections import Counter


@lru_cache(maxsize=32)
def amount_of_unique_char(string):
    if not isinstance(string, str):
        raise TypeError
    dict_of_char = Counter(string)
    list_unique_char = [value for value, count in dict_of_char.items() if count == 1]
    amount_unique = len(list_unique_char)
    return amount_unique, list_unique_char


if __name__ == "__main__":
    input_string = input()
    func = (amount_of_unique_char(input_string))
    if func[0] == 0:
        print(f'"{input_string}" => {func[0]}' + '\n' + "none" + " are present once.")
    else:
        print(f'"{input_string}" => {func[0]}' + '\n' + ",".join(func[1]) + " are present once.")
