# Requirements - Python 3.8.1

"""
    In mathematics, for given real numbers a and b, the logarithm logb a is a number x such that bx = a. 
    Analogously, in any group G, powers bk can be defined for all integers k, 
    and the discrete logarithm logb a is an integer k such that bk = a
"""

# https://en.wikipedia.org/wiki/Discrete_logarithm <= For more info


def discrete_logarithm(a, b, p):
    """
    Discrete Logarithm

    Variables = α, β, x, p
    If n is the smallest +ve int such that α^n ≡ 1(mod(p)), 
        we may assume 0 <= x <= n

        x = Lα(β), which is called as dicrete log of β wrt to α
    """
    for i in range((p-1)):
        print(f"{b} = {a}^{i}mod{p} = {(a**i)%p}")
        if b == (a**i)%p:
            print(f"{i} = L{a}({b})")
            return


# Test code
discrete_logarithm(2, 3, 13)