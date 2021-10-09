import math

def fermats_factorization(n, _range):
    for i in range(_range):
        res = n + i**2
        print('(' + str(n) + ' + ' + str(i) + '^2' + ') =  √' + str(res) + ' = ' + str(math.sqrt(res)))
        if math.sqrt(res) == int(math.sqrt(res)):
            return abs(i + int(math.sqrt(res))), abs(i - int(math.sqrt(res)))
            break
    return False

def fermats_factorization_2(n):
    a = math.ceil(math.sqrt(n))
    b = math.sqrt(a**2 - n)
    if b == int(b):
        return abs(a + int(b)), abs(a - int(b))
    


# print(fermats_factorization(8051, 10))
print(fermats_factorization_2(8051))