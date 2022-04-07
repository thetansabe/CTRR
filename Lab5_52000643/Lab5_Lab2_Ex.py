import itertools
# #
def lImplies(p,q):
	if p:
		return q
	else:
		return True

def lAnd(p,q):
	return p and q

def lOr(p,q):
	return p or q

def lXOr(p,q):
	return p != q

def lNot(p):
	return not p

def lEquivalent(q,p):
	return p == q
##
def genere_table(n):
	return list(itertools.product([False, True], repeat=n))

print("\n--------------------ex4-------------")
def printTruthTable(arr, space):
	return "\t".join([item.ljust(space) for item in arr])
 
def printTruthTable1(arr, space):
	return "\t".join([str(item).ljust(space) for item in arr])

##ex4
table3 = genere_table(3)

def cau4b():
    print("Truth table 4b: ¬p ∨ (q ∧ r) → r")
    print(printTruthTable(['p','q','r','~p','(q ∧ r)','¬p ∨ (q ∧ r)','¬p∨(q ∧ r)→ r'],12))
    print('-'*100)
    for(p,q,r) in table3:
        A = not p
        B = lAnd(q,r)
        C = lOr(A,B)
        D = lImplies(C,r)

        print(printTruthTable1([p,q,r,A,B,C,D],12))

table4 = genere_table(4)

def cau4e():
    print("Truth table 4e: p ∨ q → ¬r ∨ t")
    print(printTruthTable(['p','q','r','t','p ∨ q','¬r ∨ t','p ∨ q → ¬r ∨ t'],12))
    print('-'*100)
    for(p,q,r,t) in table4:
        A = lOr(p,q)
        B = lOr(not r,t)
        C = lImplies(A,B)

        print(printTruthTable1([p,q,r,t,A,B,C],12))


def cau4g():
    print("Truth table 4g: p ∨ t → q → (r → t)")
    print(printTruthTable(['p','q','r','t','p ∨ t','p ∨ t → q','r → t','p∨t→q→(r → t)'],8))
    print('-'*150)
    for(p,q,r,t) in table4:
        A = lOr(p,t)
        B = lImplies(A,q)
        C = lImplies(r,t)
        D = lImplies(B,C)

        print(printTruthTable1([p,q,r,t,A,B,C,D],8))

##cau5
def ex5a():
	table = [True, False]
	for p in table:
		if p != lNot(lNot(p)):
			return 'Cau 5a: Inequivalent'
	return 'Cau 5a: Equivalent'


table2 = genere_table(2)
#¬(p ∨ q) ≡ (¬p ∨ ¬q)
def ex5c():
    for (p,q) in table2:
        if not(lOr(p,q)) != lOr(not p , not q):
            return 'Cau 5c: Inequalivant'
    
    return 'Cau 5c:Equalivant'

#(p ∨ q) → r ≡ (p → r) ∧ (q → r)
def ex5d():
    for (p,q,r) in table3:
        if lImplies(lOr(p,q),r) != lAnd(lImplies(p,r),lImplies(q,r)):
            return 'Cau 5d: Inequalivant'
    return 'Cau 5d: Equalivant'

#(p ∨ ¬q) → ¬p ≡ (p ∨ (¬q)) → ¬p
def ex5f():
    for (p,q) in table2:
        left = lImplies(lOr(p,not q),not p)
        right = lImplies(lOr(p,not q),not p)
        if left != right:
            return 'Cau 5f: Inequalivant'
        return 'Cau 5f: Equalivant'

##cau6
def ex6c():
    print("Truth table 6c: ")
    print(printTruthTable(['p->q','¬r ∨ s','p ∨ r','∴ ¬q → s'],8))
    print('-'*150)
    for(p,q,r,s) in table4:
        A = lImplies(p,q)
        B = lOr(not r, s)
        C = lOr(p,r)
        con = lImplies(not q, s)

        premises = {A,B,C}
        print(printTruthTable1([A,B,C,con],10))

        if(len(premises) == 1 and (True in premises)):
            if con == False:
                return "Cau 6c: INVALID"
    return "Cau 6c: VALID"

table5 = genere_table(5)
def ex6b():
    print("Truth table 6b: ")
    print(printTruthTable(['p → (q → r)','p ∨ s','t → q','¬s','∴ ¬r → ¬t'],8))
    print('-'*150)
    for(p,q,r,s,t) in table5:
        A = lImplies(p,lImplies(q,r))
        B = lOr(p,s)
        C = lImplies(t,q)
        D = not s
        con = lImplies(not r, not t)

        print(printTruthTable1([A,B,C,D,con],10))

        premises = {A,B,C,D}
        if(len(premises) == 1 and (True in premises)):
            if con == False:
                return "Cau 6b: INVALID"
    return "Cau 6b: VALID"

cau4b()
cau4e()
cau4g()
print("\n--------------------ex5-------------")
print(ex5a())
print(ex5c())
print(ex5d())
print(ex5f())
print("\n--------------------ex6-------------")
print(ex6c())
print()
print(ex6b())

