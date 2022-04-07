import math

def isPrime(n):
    if n > 1:
        for i in range (2, int(n/2) + 1):
            if(n%i) == 0 :
                return False
        return True
    return False

def nextPrime(n):
    for i in range(1,100):
        ans = n+i
        if(isPrime(ans)): return ans
    return -1


def primeFact(p):
    a = []
    while(p%2 == 0):
        a.append(int(2))
        p = p/2

    
    for i in range(3, int(math.sqrt(p)) + 1, 2):
        while(p % i == 0):
            a.append(int(i))
            p = p/i
    
    if(p > 2):
        a.append(int(p))

    return a

def printPrime(n):
    for i in range (2,n):
        if(isPrime(i)): print(str(i))
    

def cau4(n):
    out = []
    if(n<2): return out
    else:
        out.append(int(2))

        for i in range(3,n):
            flag = True
            j = 0
            while(j+1 < len(out)):
                if(i % out[j] == 0): 
                    flag = False
                    break
                j += 1
            if(flag == True):
                out.append(i)
            if(i+2 < n): i += 2
            else: return out

def gcd(a,b):
    if(b == 0): return a
    return gcd(b,a%b)

def lcm(a,b):
    return a*b/gcd(a,b)

def dec2bin(n):
    if(n == 0): return 0
    return n%2 + dec2bin(n//2)*10

def decFrac2bin(n):
    right = n - int(n)
    left = float(dec2bin(int(n)))
    buff = 1.0
    ans = 0
    while(right < 1):
        right = right * 2
        buff = buff/10
        ans = int(right)*buff
    return left+ans

def dec2hex(decimal):
    conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}
  
    hexadecimal = ''
    while(decimal > 0):
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16
    
    return hexadecimal

def convertbase(a,base1,base2):
    s = ""
    for i in a:
        s = s + str(i)

    if(base1 == 10): a = int(s)
    if(base1 == 2): a = bin(int(s))
    if(base1 == 16): a = hex(int(s))

    if(base2 == 10): b = int(a)
    if(base2 == 2): b = bin(a)
    if(base2 == 16): b = hex(a)

    return b

##########tests
# #cau1
# print(nextPrime(8))
# # #cau2
# print(primeFact(60))
# # #cau3
# printPrime(8)
# # #cau4
# print(cau4(20))
# # #cau5
# print(gcd(12,18))
# #cau6
print(lcm(5,7))
# # #cau7
# print(dec2bin(5))
# # #cau8
# print(decFrac2bin(5.5))
# # #cau9
# print(dec2hex(69))
# # #cau10
# print(convertbase([1,1,1],10,16))