from caeser_cipher2 import caesar

code = caesar()
c = code.encrypt()
brute_force = caesar()
brute_force.str_inp = c
for key in range(26):
    brute_force.encrypt(key)