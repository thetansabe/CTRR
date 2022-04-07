#bai1
def thieves(x):
    # x la so ngay, 40 la max thieves
    #function thives de tinh so ngay x ngay khi het 40 thieves
    if(x == 1): return 2
    return x + thieves(x-1)

def bai1(x):
    if(thieves(x) > 40): return x + 1
    return bai1(x+1)

#bai 2
def richest(x):
    #mang 1 phan tu thi tra ve luon
    if(len(x) == 1): return x[0]
    max = richest(x[1:])
    return max if max > x[0] else x[0]

def bai2():
    a = [120,720,220,270,360]
    print('Highest gold trong bai 2: ',richest(a))

#bai 3
def waytochoose(n,k):
    # n max = 50 people
    # find k  that give the number of ways to choose as close to 1000 as possible
    if(k == 0 or k == n): return 1
    return waytochoose(n-1,k) + waytochoose(n-1,k-1)

def bai3(n,k):
    if(waytochoose(n,k) > 1000): return k
    return bai3(n,k+1) 

# print(waytochoose(50,1)) #50
# print(waytochoose(50,2)) #1225

# #bai4
def waytochooseP(n,k):
    if(k == 0 or k == n): return 1
    return (n-k+1)*waytochooseP(n,k-1)

def bai4(n,k):
    if(waytochooseP(n,k) > 10000): return k-1
    return bai4(n,k+1)

# print(waytochooseP(50,2)) #2450
# print(waytochooseP(50,3)) #117 600

#bai 5: 2^n
#n: number of stories
def bai5(n):
    if(n == 1): return 1
    return 2*bai5(n-1)

#bai6: return the nth number of fibonacci sequence
def fibo(n):
    if(n<2): return 1
    return fibo(n-1) + fibo(n-2)

def bai6(n):
    #n: so' thu' n trong day fibo
    print('Bai 6: so thu '+str(n)+' trong day Fibo la: '+str(fibo(n-1)))



print('Dap an bai 1 la: ',str(bai1(1)))
bai2()
print('Dap an bai 3: '+str(bai3(50,1)))
print('Dap an bai 4: '+str(bai4(50,1)))
print('Dap an bai 5: '+str(bai5(547)))
bai6(6)

