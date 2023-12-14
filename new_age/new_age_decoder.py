from utils import remove_slash_n, gear, use_plugs, hash_characters
from constants import characters,len_chars

def enc_idx(a,encrypted_chars):return encrypted_chars.index(a)

def final_decrypt(ciphertext,encrypted_chars,where_to):
    plaintext = ""
    for j,i in enumerate(ciphertext):
        if where_to is not None:
            if j in where_to:
                new_idx = enc_idx(i, encrypted_chars)
                plaintext += characters[new_idx]
            else:
                plaintext+=i
        else:
            new_idx = enc_idx(i, encrypted_chars)
            plaintext += characters[new_idx]
    return plaintext

def get_info(use_settings):
    if not use_settings:
        with open("pad.txt","r") as f:
            lists=f.readlines()
    else:
        with open("settings.txt","r") as f:
            lists=f.readlines()

    return lists

def de_processor(settings_list):
    key_word = settings_list[0]
    no_of_gears = int(settings_list[1])
    keylist = settings_list[2].split(",")

    x = key_word
    previous_key = x
    for i in range(no_of_gears - 1, -1, -1):
        key_int = int(keylist[i])
        previous_key = gear(previous_key, key_int,reverse=True)

    old_key = previous_key
    meon_key = old_key[:len_chars]
    return hash_characters(meon_key)

def main():
    ciphertext=input("\nEnter ciphertext:")
    settings_opt = input("Use settings\na.)true\nb.)false\nEnter:")
    use_settings = settings_opt.lower() == "a"

    settings_list=get_info(use_settings)

    settings_list=remove_slash_n(settings_list)

    plugs = settings_list[3].split(",")
    try:
        where_to = [int(i) for i in settings_list[4].split(",")]

        if len(ciphertext) - len(where_to) > 4: where_to = None
    except IndexError:
        where_to = None
    ciphertext = use_plugs(plugs,ciphertext)

    encrypted_chars = de_processor(settings_list)

    plaintext=final_decrypt(ciphertext,encrypted_chars,where_to)

    plaintext = use_plugs(plugs, plaintext)

    print("\nDecrypted Message->"+plaintext)

    #delete the pad
    _ = open("pad.txt","w").close()

if __name__=="__main__":
    main()