def ex1():
    T1 = [2,
        7, 5,
        2,6,None,9,
    None,None,5,11,None,None,4,None]

    T2 = [50,
        17, 76,
    9,23 , 54, None,
None,14,19,None,None,72,None,None,
None,None,12,None,None,None,None,None,None,None,67,None,None,None,None,None]

############################################################Ex2
class bNode(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

################
A1 = bNode(2)
A1.left = bNode(7)
A1.right = bNode(5)

B1 = A1.left
C1 = A1.right
B1.left = bNode(2)
B1.right = bNode(6)
C1.right = bNode(9)

D1 = B1.left
E1 = B1.right
E1.left = bNode(5)
E1.right = bNode(11)

F1 = C1.right
F1.left = bNode(4)

I1 = F1.left
#######################
A2 = bNode(50)
A2.left = bNode(17)
A2.right = bNode(76)

B2 = A2.left
B2.left = bNode(9)
B2.right = bNode(23)

D2 = B2.left
D2.right = bNode(14)

G2 = D2.right
G2.left = bNode(12)

E2 = B2.right
E2.left = bNode(19)

C2 = A2.right
C2.left = bNode(54)

F2 = C2.left
F2.right = bNode(72)

I2 = F2.right
I2.left = bNode(67)

L2 = I2.left

def LNR(A):
    if A:
        LNR(A.left)
        print(A.data)
        LNR(A.right)

LNR(A2)