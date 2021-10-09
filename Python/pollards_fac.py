"""
Pollards(p - 1)

Inputs:
n, B

Pseudocode
a= 2, e = 2

while e <= B:
    a = a^e mod(n)
    e = e + 1

p1 = gcd(a-1, n)
p1 is one factor, therfore 2nd factor p2 = n/p1

"""

from euclidean_gcd import print_gcd, gcd 

def pollard_p(n, B):
    a, e = 2, 2
    counter = 1
    while e <= B:
        a = (a**e)%n
        print(f"IT{counter} while {e} <= {B} \n{a} = {a}^{e} mod({n}) => {a**e} mod({n}) => {(a**e)%n} mod({n})")
        e += 1
        print(f"e = {e} + 1\n")
        counter += 1
    
    print_gcd(a-1, n)
    f1 = gcd(a-1, n)

    if f1 == 1:
        print('Failure')
        return
    f2 = n//f1

    print(f'Therefore the factors are {f1} and {f2}')

pollard_p(299, 5)