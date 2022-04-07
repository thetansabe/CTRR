import math

def cau2e():
    for x in range(0,101):
        if (math.sqrt(x+5) == (math.sqrt(x) + math.sqrt(5))):
            return "Cau 2e: The given statement is correct when x equals to "+str(x)
    return "Cau 2e: The given statement is incorrect for all values x within the given domain"

def cau3f():
    print('-'*50)
    print('Cau3f: ∃c ∈ Z, 0 < c ≤ 100, c^2 ≤ c')
    print('Formal form of origin statement: Exist c in Z, such that P(c), Q(c) ')
    print('Formal form of negated statement: For all c in Z, if P(x) then NOT Q(x)')
    print('NEGATED: For all c in Z, if 0 < c ≤ 100, then c^2>c')

    for c in range(1,101):
        if(c**2 - c <= 0):
            return "The given statement is incorrect when x equals to "+str(c)
    return "The NEGATED statement is correct for all values x within the given domain"

def cau4a():
    left = right = 0
    for x in range(0,11):
        for y in range(0,11):
            left = left + (x+y)**2
            right = right + (x+2*y)**2
            if(left <= right):
                return "4a: The given statement is NOT correct"
    return "4a: The given statement is correct"

def cau4d():
    right = 10**4 + 2 * 10**3 + 10**2 - 5**4 - 2 * 5**3 - 5*2
    left = 0
    for x in range(5,11):
        left = left + (4*x**3+6*x**2+2*x)

    if(left <= right):
        return "4d: The given statement is NOT correct"
    return "4d: The given statement is correct"

def cau3d():
    print('-'*50)
    print('Cau3d: ∀c ∈ Z, 0 < c ≤ 100, c%4 = 0, ∃a, b ∈ Z+, c^2 = a^2 + b^2')
    print('Formal form of origin statement: For all c in Z, if P(c), then exist a,b in Z+, such that Q(c,a,b)')
    print('Formal form of negated statement: Exist c in Z, P(c) such that for all a,b in Z+, NOT Q(c,a,b)')
    print('NEGATED: Exist c in Z, 0 < c ≤ 100, c%4 = 0, For all a, b in Z+, c^2 != a^2 + b^2')

    for c in range(1,101):
        if(c%4 == 0 and prove1(c)):
            return "The given statement is correct when x equals to "+str(c)
    return "The NEGATED statement is incorrect for all values x within the given domain"

def prove1(c):
    # print('Origin: For all a, b in Z+, c^2 != a^2 + b^2')
    # print('Negated: Exist a,b in Z+, c^2 = a^2 + b^2')

    #if negated is correct when there is a value of x -> origin is false -> return false
    for a in range(1,c):
        for b in range(1,c):
            t = a**2 + b**2
            if(t == c**2):
                return False

    return True

def cau3e():
    print('-'*50)
    print('Cau3d: ∀c ∈ Z, 0 < c ≤ 100, c%5 = 0, ∃a, b ∈ Z+, c^2 = a^2 + b^2')
    print('Formal form of origin statement: For all c in Z, if P(c), then exist a,b in Z+, such that Q(c,a,b)')
    print('Formal form of negated statement: Exist c in Z, P(c) such that for all a,b in Z+, NOT Q(c,a,b)')
    print('NEGATED: Exist c in Z, 0 < c ≤ 100, c%5 = 0, For all a, b in Z+, c^2 != a^2 + b^2')

    for c in range(1,101):
        if(c%5 == 0 and prove1(c)):
            return "The given statement is correct when x equals to "+str(c)
    return "The NEGATED statement is incorrect for all values x within the given domain"

print(cau2e())
print('-'*100)
print(cau3d())
print(cau3e())
print(cau3f())
print('-'*100)
print(cau4a())
print(cau4d())

