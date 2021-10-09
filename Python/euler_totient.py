"""
ϕ(n)
"""

import math, numpy

def isPrime(n):
    """Source: https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/ """
    # Corner cases 
    if (n <= 1): 
        return False
    if (n <= 3): 
        return True
    # This is checked so that we can skip 
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0): 
        return False 
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0): 
            return False
        i = i + 6
    return True

def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b) 

def euler_totient_vals(n):
    for i in range(1, n):
        if gcd(i, n) == 1:
            print(i)

def euler_totient(n):
    if n == 1:
        return 0
    elif isPrime(n):
        return n - 1
    else:
        prime_factors = primeFactors(n)
        newlist = set(prime_factors)
        raised_to = dict()
        for i in newlist:
            raised_to[i] = 0
        for i in prime_factors:
            if i in newlist:
                raised_to[i] += 1
            newlist.add(i)
        lastlst = []
        for k, v in raised_to.items():
            lastlst.append((k**v) - (k**(v-1)))
        return numpy.prod(lastlst)
    
def primeFactors(n): 
    """Source: https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/"""
    lst = []
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        lst.append(2) 
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2):
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            lst.append(i)  
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        lst.append(n)
    
    return lst




# print('n: ', end="")
# n = int(input())
# euler_totient_vals(n)
# print('Euler Totient:' + str(euler_totient(n)))
# print(gcd(172-126, 3427))
# print(gcd(172+126, 3427))
