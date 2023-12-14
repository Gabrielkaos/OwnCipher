from random import randint, choice, choices
from constants import characters,len_chars
from utils import remove_slash_n,gear,char_idx,use_plugs, generate_plugs, \
    hash_characters

def final_encrypt(plaintext, encrypted_chars,where_to):
    ciphertext = ""
    for j,i in enumerate(plaintext):
        if where_to is not None:
            if j in where_to:
                new_idx = char_idx(i)
                ciphertext += encrypted_chars[new_idx]
            else:
                ciphertext+=i
        else:
            new_idx = char_idx(i)
            ciphertext += encrypted_chars[new_idx]
    return ciphertext

def save(key_5, keylist,no_of_gears,plugs,where_to,path="pad.txt"):
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
    for i in range(len(plugs)):
        if i==len(plugs)-1:
            meon_things3.write(str(plugs[i]))
        else:
            meon_things3.write(str(plugs[i])+",")
    if where_to is not None:
        meon_things3.write("\n")
        for i in range(len(where_to)):
            if i==len(where_to)-1:
                meon_things3.write(str(where_to[i]))
            else:
                meon_things3.write(str(where_to[i])+",")
    meon_things3.close()

def generate_where_to_encrypt(plaintext):
    n = len(plaintext)

    if n > 5:
        n_encrypt = n - randint(2, (n // 2) - 1)
        indices = [i for i in range(n)]

        to_return = []
        while True:
            a = choice(indices)
            if a not in to_return:
                to_return.append(a)

            if len(to_return)>=n_encrypt:break
        return to_return

    return None

def processor(plaintext,no_of_gears,use_settings,settings,where_to):
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

        ciphertext = final_encrypt(plaintext, encrypted_chars,where_to)
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

        ciphertext = final_encrypt(plaintext, encrypted_chars,where_to)
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
        plugs = generate_plugs()
        no_of_gears=int(input("\nEnter how many gears:"))
        where_to_encrypt = generate_where_to_encrypt(plaintext)
    else:
        plugs = settings1[3].split(",")
        no_of_gears=int(settings1[1])

        try:
            where_to_encrypt = [int(i) for i in settings1[4].split(",")]
            if len(plaintext) - len(where_to_encrypt) > 4:
                where_to_encrypt = None
        except IndexError:
            where_to_encrypt = None

    plaintext = use_plugs(plugs,plaintext)

    ciphertext, key_,keylist = processor(plaintext, no_of_gears,use_settings,settings1,where_to_encrypt)

    #use plugs
    ciphertext = use_plugs(plugs,ciphertext)

    if not use_settings:
        is_save = input("Save?\na.)true\nb.)false\nEnter:").lower() == "a"
        print("\ninfo saved to pad")
        save(key_,keylist,no_of_gears,plugs,where_to_encrypt)
        if is_save:save(key_, keylist, no_of_gears,plugs,where_to_encrypt,path="settings.txt")

    print("\nEncrypted Message->" + ciphertext)


if __name__ == "__main__":
    main()