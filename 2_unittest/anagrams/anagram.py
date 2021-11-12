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
    if not isinstance(input_text, str):
        raise TypeError('work only with strings')
    result = []
    list_words = input_text.split()
    for words in list_words:
        reverse_word = reverse_string(words)
        result.append(reverse_word)
    return " ".join(result)




