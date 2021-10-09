"""Quadractic Sieve"""

import math
from euler_totient import gcd

def q_sieve(n):
    root = math.ceil(math.sqrt(n))
    for i in range(100):
        x = ((root + i)**2) % n
        if math.sqrt(x) == int(math.sqrt(x)):
            if (root + i)%n != math.sqrt(x) and (root + i)%n != -math.sqrt(x):
                return gcd((root+i) + math.sqrt(x), n), gcd((root+i) - math.sqrt(x), n)


a, b = q_sieve(1649)
print(a)
print(b)
print(a*b)
