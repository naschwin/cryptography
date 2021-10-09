from random import randint
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

string_input = input("Enter the string:\n")
str_inp = string_input.upper()
print(string_input)
input_length = len(string_input)
print("Input Length: ",input_length)
length_alpha = len(alpha)
n = int(input("Enter shift:\n"))
if(n == 0):
    print("Same string")
else:
    print(n)

def encrypt(str_,str_len,lst_len,lst,l):
    new_str = ""
    for i in range(str_len):
        for j in range(lst_len):
            if(lst[j] == str_[i]):
                if((j+l) < lst_len):
                    new_char = lst[j+l]
                else:
                    new_char = lst[(j+l)%lst_len]
                
                new_str += new_char
    #print(new_str)
    return new_str            

def key_maker(shift):
    a = bin(shift)
    pluser = randint(1000,2000)
    b = bin(pluser)
    key = a + b
    print(key)
    return key

def key_validator(key):
    a = key_maker(n)
    if(key == a):
        return True
    
def decrypt(str_,lst,shift):
    key = input('Enter Key:\n')
    if(key_validator(key) == True):
        dec_str = ""
        str_len = len(str_)
        lst_len = len(lst)
        for i in range(str_len):
            for j in range(lst_len):
                if(lst[j] == str_[i]):
                    if((j-key) < lst_len):
                        new_char = lst[j-key]
                    elif((j - key) < 0):
                        new_char = lst[key - j]
                    
                    dec_str += new_char
        print(dec_str)

def decrypt_option():
    p = input("Decrpyt ? (Y/N)")
    if(p == 'Y'):
        decrypt(a,alpha,n)
    elif(p == 'N'):
        return
    else:
        print('Wrong Input')
        decrypt_option()
    
a = encrypt(str_inp,input_length,length_alpha,alpha,n)
print(a)    
u = key_maker(n)
print(u)
decrypt_option()
