alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

key = "Cipher"

def num_maker(str_, main_str):
    str_new = []
    for i in range(len(str_)):
        for j in range(len(main_str)):
            if str_[i].lower() ==  main_str[j].lower():
                str_new.append(j)
    return str_new

def encrypt(key, str_, i = 0):
    global alpha
    lst_key = num_maker(key, alpha)
    lst_mes = num_maker(str_, alpha)
    new_lst = []
    j = 0
    if i >= len(lst_mes):
        pass
    else:
        encrypt(key, str_, counter)
    while i < len(lst_key) and j < len(lst_key):
        new_lst.append(lst_mes[i] + lst_key[j])
        counter = i
        i += 1

    
    return lst1

#num_maker(key, alpha)
lst = encrypt(key, "Watashi wa kita")
print(lst)
