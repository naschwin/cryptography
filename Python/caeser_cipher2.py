from random import randint

class caesar():
    def __init__(self):
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.alpha = alpha
        self.alpha_len = len(self.alpha)
        string_input = input("Enter the string:\n")
        str_inp = string_input.upper()
        self.str_inp = str_inp
        input_length = len(string_input)
        self.input_length = input_length

    def encrypt(self, shift = 11):
        lst_len = len(self.alpha)
        str_len = len(self.str_inp)
        new_str = ""
        #n = int(input("Enter shift:\n"))
        self.shift = shift
        n = shift
        if(n == 0):
            print("Same string")
        else:
            print(n)
        for i in range(str_len):
            for j in range(lst_len):
                if(self.alpha[j] == self.str_inp[i]):
                    if((j+n) < lst_len):
                        new_char = self.alpha[j+n]
                    else:
                        new_char = self.alpha[(j+n)%lst_len]
                    
                    new_str += new_char
        print(new_str)
        self.encrypted = new_str
        return new_str

    def decrypt(self):
        dec_str = ""
        str_len = len(self.encrypted)
        lst_len = len(self.alpha)
        for i in range(str_len):
            for j in range(lst_len):
                if(self.alpha[j] == self.encrypted[i]):
                    if((j-self.shift) < lst_len):
                        new_char = self.alpha[j - self.shift]
                    elif((j - self.shift) < 0):
                        new_char = self.alpha[self.shift - j]            
                    dec_str += new_char
        print('Decrypted:',dec_str)

if __name__ == "__main__":
    code = caesar()
    n = int(input("1)Encrypt \n2)Decrypt"))
    if n == 1:
        a = int(input("Enter the shift"))
        code.encrypt(a)
        code.decrypt()
    elif n == 2:
        code.decrypt()
