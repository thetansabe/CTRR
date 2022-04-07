import numpy as np

def createMatrix(m,n): #row
    matrix = []
    for i in range(0,m): #col
        col = []
        for j in range(0,n):
            t = int(input("Nhap phan tu m[%d][%d]: " %(i,j)))
            col.append(t)
        print()
        matrix.append(col)
    return matrix

def printMatrix(matrix,m,n):
    for i in range(m):
        for j in range(n):
            print(matrix[i][j],end = " ")
        print()

def inputTwoMatrixs():
    m1 = int(input("Enter number of Rows for matrix A: "))
    n1 = int(input("Enter number of Columns for matrix A: "))
    A = createMatrix(m1,n1)

    m2 = int(input("Enter number of Rows for matrix B: "))
    n2 = int(input("Enter number of Columns for matrix B: "))
    B = createMatrix(m2,n2)
    
    return (A,B,m1,n1,m2,n2)

def mSum(A,B,m,n):
    C = []
    for i in range(m):
        tmp = []
        for j in range(n):
            t = A[i][j] + B[i][j]
            tmp.append(t)
        C.append(tmp)
    return C

def bai7():
    (A,B,m1,n1,m2,n2) = inputTwoMatrixs()
    # printMatrix(A,m1,n1)
    # print()
    # printMatrix(B,m2,n2)
    print("Sum 2 matrixes: ")
    if(m1 != m2 or n1 != n2):
        print("Cannot add!!!")
        
    else:
        C = mSum(A,B,m1,n1)
        printMatrix(C,m1,n1)

def mProd(A,B):
    C = np.dot(A,B)
    return C

def bai8():
    (A,B,m1,n1,m2,n2) = inputTwoMatrixs()
    print("Product 2 matrixes: ")
    if(n1 != m2):
        print("Dimension error for multiply!!!")
        
    else:
        C = mProd(A,B)
        printMatrix(C,m1,n1)

##################################
def ithCombine(p,q):
    return "If "+p.lower()+", then "+q

def pandqCombine(p,q):
    return p + " and " + q[0 :q.index(" ")] + " not " + q[q.index(" ")+1 :]

def npoqCombine(p,q):
    return p[0 :p.index(" ")]+" not "+p[p.index(" ")+1 :] + ", or "+q

def bai9():
    p = "It sunny outside"
    q = "I go camping"
    print(ithCombine(p,q))
    print(pandqCombine(p,q))
    print(npoqCombine(p,q))

bai9()
bai7()
bai8()
