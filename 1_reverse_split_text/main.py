def reverse_string(word):
    if not word:
        return ""
    list_only_character = []
    word_list = list(word)
    for letter in word:
        if letter.isalpha():
            list_only_character.append(letter)
    for index, letter in enumerate(word_list):
        if letter.isalpha():
            word_list[index] = list_only_character.pop()
    temp_res = ''.join(word_list)
    return temp_res


def split_text(input_text):
    result = []
    list_words = input_text.split()
    for words in list_words:
        reverse_word = reverse_string(words)
        result.append(reverse_word)
    return " ".join(result)




if __name__ == '__main__':
    cases = [
        ("abcd efgh", "dcba hgfe"),
        ("a1bcd efg!h", "d1cba hgf!e"),
        ("", ""),
        ("hn*b6 j34g@", "bn*h6 g34j@")
    ]

    for text, reversed_text in cases:
        assert split_text(text) == reversed_text
        print(split_text(text))