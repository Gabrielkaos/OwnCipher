from constants import characters,len_chars
# from random import randint,choice

def char_idx(a):return characters.index(a)

def remove_slash_n(settings):
    settings1 = []
    for i, t in enumerate(settings):
        if i == len(settings) - 1:
            settings1.append(t[:])
        else:
            settings1.append(t[:-1])

    return settings1

def gear(key_word, int_key,reverse=False):
    # if reverse:
    #     return "".join([characters[(char_idx(i) - int_key) % len_chars] for i in key_word])

    previous_key = []
    for i in key_word:
        if reverse:
            character = characters[(char_idx(i) - int_key) % len_chars]
        else:
            character = characters[(char_idx(i) + int_key) % len_chars]
        previous_key.append(character)
    return "".join(previous_key)

    # return "".join([characters[(char_idx(i) + int_key) % len_chars] for i in key_word])

def hash_characters(key_word):
    list_char = list(characters)

    list_char = [i for i in list_char if i not in key_word]

    key_list = list(key_word)
    key_list.extend(list_char)
    final_list = list(dict.fromkeys(key_list))
    return "".join(final_list)
