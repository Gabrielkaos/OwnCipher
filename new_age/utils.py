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
    if reverse:return "".join([characters[(char_idx(i) - int_key) % len_chars] for i in key_word])
    return "".join([characters[(char_idx(i) + int_key) % len_chars] for i in key_word])

# def use_plugs(plugs,ciphertext):
#
#     plugs_dict = {}
#     reverse_plugs_dict = {}
#     for i in plugs:
#         things = i.split('-')
#         plugs_dict[things[0]]=things[1]
#         reverse_plugs_dict[things[1]] = things[0]
#
#     new_text = ""
#     for i in ciphertext:
#         get_from_plug = plugs_dict.get(i,None)
#         backward_from_plug = reverse_plugs_dict.get(i,None)
#         if get_from_plug is not None:
#             to_be_added=get_from_plug
#         elif backward_from_plug is not None:
#             to_be_added=backward_from_plug
#         else:to_be_added=i
#
#         new_text+=to_be_added
#     return new_text
#
# def generate_plugs():
#
#     number_of_pairs = randint(10,30)
#
#     keys = []
#     values = []
#     while True:
#         random_a = choice(characters)
#
#         if random_a not in keys:
#             keys.append(random_a)
#
#         if len(keys) >= number_of_pairs: break
#
#     while True:
#         random_a = choice(characters)
#
#         if random_a not in keys and random_a not in values:
#             values.append(random_a)
#
#         if len(values) >= number_of_pairs: break
#
#     return [k+'-'+v for k,v in zip(keys,values)]


def hash_characters(key_word):
    list_char = list(characters)

    list_char = [i for i in list_char if i not in key_word]

    key_list = list(key_word)
    key_list.extend(list_char)
    final_list = list(dict.fromkeys(key_list))
    return "".join(final_list)
