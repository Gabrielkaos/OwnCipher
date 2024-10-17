from random import randint, choices
from constants import characters,len_chars
from utils import remove_slash_n,gear,char_idx, \
    hash_characters

def final_encrypt(plaintext, encrypted_chars):
    ciphertext = ""
    for j,i in enumerate(plaintext):
        new_idx = char_idx(i)
        ciphertext += encrypted_chars[new_idx]
    return ciphertext

def save(key_5, keylist,no_of_gears,path="pad.txt"):
    meon_things = open(path, 'w')
    meon_things.write(key_5)
    meon_things.close()
    meon_things1 = open(path, 'a')
    meon_things1.write("\n"+str(no_of_gears))
    meon_things1.close()
    meon_things2 = open(path, 'a')
    meon_things2.write("\n")
    for i in range(len(keylist)):
        if i==len(keylist)-1:
            meon_things2.write(str(keylist[i]))
        else:
            meon_things2.write(str(keylist[i])+",")
    meon_things2.close()
    meon_things3 = open(path, 'a')
    meon_things3.write("\n")

    meon_things3.close()

def processor(plaintext,no_of_gears,use_settings,settings):
    if not use_settings:
        key_word = "".join(choices(characters, k=len_chars))

        x=key_word
        previous_key=x
        key_int_list=[]

        for i in range(no_of_gears):
            key_int=randint(0,len_chars-1)
            key_int_list.append(key_int)
            previous_key=gear(previous_key,key_int)

        final_key=previous_key

        encrypted_chars = hash_characters(key_word)

        ciphertext = final_encrypt(plaintext, encrypted_chars)
        return ciphertext, final_key,key_int_list
    else:
        key_word=settings[0]
        keylist=settings[2].split(",")
        x = key_word
        previous_key = x
        for i in range(no_of_gears - 1, -1, -1):
            key_int = int(keylist[i])
            previous_key = gear(previous_key, key_int,reverse=True)

        old_key = previous_key
        encrypted_chars = hash_characters(old_key)

        ciphertext = final_encrypt(plaintext, encrypted_chars)
        return ciphertext, old_key, keylist

def main():
    with open("settings.txt","r") as f:
        settings0=f.readlines()
    settings1 = remove_slash_n(settings0)

    print("\nNon AlphaNumerics and Spaces are not allowed\n")
    plaintext = input("Enter plaintext:")
    plaintext = plaintext.replace(" ","")

    use_settings = input("Use settings\na.)true\nb.)false\nEnter:").lower() == "a"
    if not use_settings:
        # plugs = generate_plugs()
        no_of_gears=int(input("\nEnter how many gears:"))
    else:
        # plugs = settings1[3].split(",")
        no_of_gears=int(settings1[1])

    # plaintext = use_plugs(plugs,plaintext)

    ciphertext, key_,keylist = processor(plaintext, no_of_gears,use_settings,settings1)

    # if '\n' in list(ciphertext):print("HERE1")

    # print(ciphertext)

    #use plugs
    # ciphertext = use_plugs(plugs,ciphertext)
    # if '\n' in list(ciphertext):print("HERE2")

    if not use_settings:
        is_save = input("Save?\na.)true\nb.)false\nEnter:").lower() == "a"
        print("\ninfo saved to pad")
        save(key_,keylist,no_of_gears)
        if is_save:save(key_, keylist, no_of_gears,path="settings.txt")

    print("\nEncrypted Message->" + ciphertext)


if __name__ == "__main__":
    main()
