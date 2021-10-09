"""
Blub Blub Shub Algorithm
Algorithm
1 - generate p & q, two large prime nos, (given in the question)
2 - calc n = p*q
3 - choose S -> (1 to (n-1))
4 - calc X0 = (S**2)mod(n)
5 - sequence Xi = (Xi-1)**2 mod(n)

"""


def decimalToBinary(n): 
    return list(bin(n).replace("0b", ""))

c = decimalToBinary(6)
c = c.count('1')
print(c)

