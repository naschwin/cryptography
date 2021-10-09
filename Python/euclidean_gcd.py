# print("n1:", end="")
# n1 = int(input())
# print("n2:", end="")
# n2 = int(input())

def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b) 

def print_gcd(n1, n2):
    if n2 != 0:
        a = max(n1, n2)
        b = min(n1, n2)
        q = a // b
        r = a % b
        print(str(a) + ' = ' + str(b) + ' x ' + str(q) + ' + ' + str(r))
        print_gcd(b, r)
    else:
        print('Gcd: '+ str(n1))
        return

print_gcd(4883, 4369)

