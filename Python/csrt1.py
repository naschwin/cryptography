class Caesar_cipher():
    def __init__(self):
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.alpha = alpha
        str_inp = input("Enter the string: \n")
        self.str_inp = str_inp.upper()

    def encrypt(self):
        inp_len = len(self.str_inp) 
        lst_len = len(self.alpha)
        enc_str = ""
        n = int(input("Enter the number of letters to be shifted: \n"))
        self.shift = n
        if n == 0:
            print("Same string")
        elif n < 0:
            print("Shift not possible")
        for i in range(len(self.str_inp)):  ##Iterating over the given String
            for j in range(len(self.alpha)):  ##Iterating over all the letters in the Alphabets to shift them
                if self.alpha[j] == self.str_inp[i]: ##to find the letter in the alpha list
                    if (j + n) < lst_len: ##To check if the shift is less then the list len
                        new_char = self.alpha[j + n]
                    else:
                        new_char = self.alpha[(j+n)%lst_len] ##This repeats the iteration from the start

                    enc_str += new_char 
        print(enc_str)



if __name__ == '__main__':
    cd = Caesar_cipher()
    cd.encrypt()
    
