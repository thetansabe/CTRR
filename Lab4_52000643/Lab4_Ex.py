import math
def printAns(result):
    if(result[0]):
        print("The given statement is correct when x equals to %d" %result[1])
    else:
        print("The given statement is incorrect for all values x within the given domain.")



print('------------------cau 2 b----------------------')
print('Cau2b: ∃x ∈ Z, 0 ≤ x ≤ 100, x^2 = 12^2 + 16^2')

def cau2b():
    for i in range(0,101):
        if(i**2 == 12**2 + 16**2):
            result = (True,i) 
            break
        else:
            result = (False,-1)
    printAns(result)
cau2b()

# cau2c
print('------------------cau 2 c----------------------')
print('Cau2c: ∃x ∈ Z, −50 ≤ x ≤ 50, x^2 ≥ 99x')

def cau2c():
    for i in range(-50,51):
        if(i**2 - 99*i >= 0):
            result = (True,i)
            break
        else:
            result = (False,-1)
    printAns(result)

cau2c()

#cau2d
print('------------------cau 2 d----------------------')
print('Cau2d: ∃x ∈ Z, 50 ≤ x ≤ 100, x(x + 1)(x + 2)%6 != 0')

def cau2d():
    for i in range(50,101):
        if(i*(i+1)*(i+2) % 6 != 0 ):
            result = (True,i)
            break
        else:
            result = (False,-1)
    printAns(result)
cau2d()


print('-'*50)
print('Cau3b: ∀x ∈ Z, 0 ≤ x ≤ 100, and x is even, x ∗ 3 + 1 is a prime number')
print('Formal form of origin statement: ∀x in Z, if P(x) and Q(x) then R(x)')
print('Formal form of negated statement: Exist x in Z, such that P(x) and Q(x), R(x) is NOT a prime number')
print('NEGATED: Exist x in Z, such that 0 ≤ x ≤ 100 and x is even, x ∗ 3 + 1 is NOT a prime number')
def checkPrime(n):
    prime_flag = 0
 
    if(n > 1):
        for i in range(2, int(math.sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False

def cau3b():
    for x in range(0,101,2):
        num = x*3+1
        if(not checkPrime(num)):
            return "The NEGATED statement is correct when x equals to " + str(x)
    return "The NEGATED statement is incorrect for all values x within the given domain"

print(cau3b())

print('-'*50)
print('Cau3c: ∀x ∈ Z, 1 ≤ x≤ 100, and x is even, x ∗ 5 + 3 is a prime number')
print('Formal form of origin statement: For all x in Z, if P(x) and Q(x) then R(x)')
print('Formal form of negated statement: Exist x in Z, such that P(x) and Q(x), R(x) is NOT a prime number')
print('NEGATED: Exist x in Z, such that 1 ≤ x≤ 100 and x is even, x ∗ 5 + 3 is NOT a prime number')

def cau3c():
    for x in range(2,100,2):
        num = x*5+3
        if(not checkPrime(num)):
            return "The NEGATED statement is correct when x equals to " + str(x)
    return "The NEGATED statement is incorrect for all values x within the given domain"
print(cau3c())

print('-'*100)

def factorial(n):
    result = 1
    for i in range(2,n+1):
        result = result * i
    return result
print('cau 4b: ')

def cau4b():
    left = factorial(20)
    right = 0
    for i in range(1,11):
        right = right + factorial(i)
    if(left < right): return "The statement is VALID"
    else: return "The statement is INVALID"
print(cau4b())

print('-'*100)
print('cau 4c: ')
def cau4c():
    left = 0
    for i in range(0,11):
        left += 3*(i**2)
    right = 10**3
    if(left >= right): return "The statement is VALID"
    else: return "The statement is INVALID"
print(cau4c())