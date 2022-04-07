def lImplies(p,q):
    if p==True:
        return q
    else:
        return True

def lAnd(p,q):
    return p and q

def lOr(p,q):
    return p or q

def lXor(p,q):
    return p != q

def lNot(p):
    return not p

def lEquivalent(p, q):
    return p == q

def rowTruthTable(arr):
    return "\t".join(arr)

import itertools

def generate_table(n): 
  return list(itertools.product([False, True], repeat= n))

# Cau 2
table2 = generate_table(2)
print("True table of Ex2")
print(rowTruthTable(['p', 'q', 'lLImp-lies(P,Q)', 'lLAnd-(P,Q)', 'lLOr(P,Q)', 'lLXor-(P,Q)', 'lLNot(P)', 'lLEquiva-lent(P,Q)']))
print('--------------------------------------------------------------------------------------------------------------------------')

for (p, q) in table2: 
  print(rowTruthTable([str(p), str(q), str(lImplies(p, q)).rjust(7), str(lAnd(p,q)).rjust(15), str(lOr(p,q)).rjust(13), str(lXor(p,q)).rjust(13), str(lNot(p)).rjust(13), str(lEquivalent(p,q)).rjust(13)]))

# Cau 3
table3 = generate_table(3)
print("True table of Ex3a")
print(rowTruthTable(['p', 'q','r', 'p ^ q', 'p ^ q -> r']))
print('-----------------------------------------------------')

for (p, q, r) in table3: 
  print(rowTruthTable([str(p), str(q), str(r), str(lAnd(p,q)), str(lImplies(lAnd(p, q), r)).ljust(13) ]))


print("True table of Ex3b")
print(rowTruthTable(['p', 'q','r', 'p ^ q', 'r -> (p ^ q)']))
print('----------------------------------------------------------------')

for (p, q, r) in table3: 
  print(rowTruthTable([str(p), str(q), str(r), str(lAnd(p,q)), str(lImplies(r, lAnd(p,q))).ljust(13) ]))

# Cau 4
print("True table of Ex4b")
print(rowTruthTable(['p','q','r','q ∧ r','¬p ∨ (q ∧ r)','¬p ∨ (q ∧ r) → r']))
print('----------------------------------------------------------------')
for (p, q, r) in table3: 
  A =  lAnd(q,r)
  B =  lOr(A,not p)
  C = lImplies(B,r)
  
  print(rowTruthTable([str(p), str(q), str(r),str(A), str(B).rjust(5), str(C)]))

table4 = generate_table(4)
print("True table of Ex4e")
print(rowTruthTable(['p','q','r','t','p V q','¬r ∨ t','p ∨ q → ¬r ∨ t']))
print('----------------------------------------------------------------')
for (p, q, r,t) in table4: 
  A =  lOr(p,q)
  B = lOr(not r,t)
  C = lImplies(A,B)
  
  print(rowTruthTable([str(p), str(q), str(r),str(t),str(A), str(B).rjust(7), str(C).rjust(15)]))


print("True table of Ex4f")
print(rowTruthTable(['p','q','r','t','p V t','p V t -> q','r -> t','p ∨ t → q → (r → t)']))
print('-------------------------------------------------------------------------------------')
for (p, q, r,t) in table4: 
  A =  lOr(p,t)
  B = lImplies(A,q)
  C = lImplies(r,t)
  D = lImplies(B,C)
  
  print(rowTruthTable([str(p), str(q), str(r),str(t),str(A), str(B).rjust(7), str(C).rjust(13),str(D).rjust(7)]))

print("True table of Ex4g")
print(rowTruthTable(['p','q','r','t','(p ∨ (q ∧ r))','((p ∨ q) ∧ (p ∨ r))',' (t ∨ ¬t)',' (((p ∨ q) ∧ (p ∨ r)) ∧ (t ∨ ¬t))','(p ∨ (q ∧ r)) ↔ (((p ∨ q) ∧ (p ∨ r)) ∧ (t ∨ ¬t))']))
print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
for (p, q, r,t) in table4: 
  A =  lOr(p,lAnd(q,r))
  B = lAnd(lOr(p,q),lOr(p,r))
  C = lOr(t,not t)
  D = lAnd(B,C)
  E = lEquivalent(A,D)
  
  print(rowTruthTable([str(p), str(q), str(r),str(t),str(A), str(B).rjust(20), str(C).rjust(15),str(D).rjust(20),str(E).rjust(30)]))

#cau 5
print("Cau 5a: Chac chan dung")
count = 0
print("Cau 5c: ")
print(rowTruthTable(['p','q','¬(p ∨ q)',' (¬p ∨ ¬q)',' ¬(p ∨ q) ≡ (¬p ∨ ¬q)']))
for(p,q) in table2:
    A = not (lOr(p,q))
    B = lOr(not p , not q)
    if(not (A==B)): 
        count+=1
    print(rowTruthTable([str(p), str(q),str(A).rjust(7),str(B).rjust(17),str(A == B).rjust(15)]))
if(count > 0): print("Invalid")
else: print("Valid")

count = 0
print("Cau 5d: ")
print(rowTruthTable(['p','q','r','(p ∨ q) → r',' (p → r) ∧ (q → r)','(p ∨ q) → r ≡ (p → r) ∧ (q → r)']))
for(p,q,r) in table3:
    A = lImplies(lOr(p,q),r)
    B = lAnd(lImplies(p,r),lImplies(q,r))
    if(not (A==B)): 
        count+=1
    print(rowTruthTable([str(p), str(q), str(r),str(A).rjust(7),str(B).rjust(17),str(A == B).rjust(25)]))
if(count > 0): print("Invalid",str(count))
else: print("Valid")

# cau 6
table5 = generate_table(5)
print("Cau 6b: ")
count = 0
print(rowTruthTable(['p','q','r','s','t','p → (q → r)','p ∨ s','t → q','~s']))
for(p,q,r,s,t) in table5:
    A = lImplies(p,lImplies(q,r))
    B = lOr(p,s)
    C = lImplies(t,q)
    D = not s
    if(A and B and C and D): count+=1
    print(rowTruthTable([str(p), str(q), str(r),str(s),str(t),str(A).rjust(7),str(B).rjust(12),str(C).rjust(7),str(D)]))
if(count < 32): print("Invalid",str(count))
else: print("Valid")