"""
    Linear Congruency
if eqn is ax = b(mod(n)), 
    then solution exist if gcd(a, n) = k, 
        where n%k == 0
No of solutions for x = gcd(a, n)
"""

def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b) 

def linear_congruence_f(a, b, n):
    if b == 0:
        return 0
    if a < 0:
        a = -a
        b = -b
    b %= n
    while a > n:
        a -= n
    return (n * linear_congruence_f(n, -b, a) + b) // a

def linear_congruence_all(first_val, no_of_sols, sep):
    lst = [first_val, ]
    for i in range(no_of_sols - 1):
        lst.append(lst[i] + sep)
    return lst

a = 12
b = 28
n = 236

sep = int(n / gcd(a, n))

lst = linear_congruence_all(linear_congruence_f(a, b, n), gcd(a, n), sep)

print(lst, sep)