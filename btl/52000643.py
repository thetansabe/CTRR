import itertools

def readInfix(filename):
    with open(filename) as f:
        Infix = f.readlines()
    return Infix[0]

##########################################Student do these 2 function
def generate_table(n): 
  return list(itertools.product([False, True], repeat= n))

def Infix2Postfix(Infix):
    Postfix = ''
    stack = []
    ###BUOC 1, DUYET CHUOI TU TRAI SANG PHAI
    for ch in Infix:
        ###BUOC 2, THEM TOAN HANG
        if(ch >= 'A' and ch <= 'Z'):
            Postfix = Postfix + ch
        ###BUOC 3 , THEM KI TU '(' VAO STACK
        if(ch == '('):
            stack.append(ch)
        ###BUOC 4, KHI GAP KI TU ')'
        if(ch == ')'):
            ##POP STACK LUU VAO POSTFIX CHO DEN KHI GAP '('
            while(stack[-1] != '('):
                Postfix = Postfix + stack.pop()
            ##XOA KI' TU '('
            stack.pop()
        ###BUOC 5, KHI GAP PHEP TOAN
        if(ch == '~' or ch == '&' or ch == '|' or ch == '>' or ch == '='):
            ## POP NHUNG PHEP TOAN CO DO UU TIEN CAO HON THEM VAO POSTFIX
            while(len(stack) != 0 and
                 stack[-1] != '(' and
                 precedence(ch) <= precedence(stack[-1])):
                    Postfix = Postfix + stack.pop()
            ## THEM PHEP TOAN VAO STACK
            stack.append(ch)
    
    ###BUOC 6, POP STACK LUU VAO POSTFIX CHO DEN KHI STACK RONG
    while(len(stack) != 0):
        Postfix = Postfix+stack.pop()
    
    return Postfix

def precedence(ch):
    if(ch =='~'): return 10*5
    if(ch =='&'): return 10*4
    if(ch == '|'): return 10*3
    if(ch == '>'): return 10*2
    return 10

def Postfix2Truthtable(Postfix):
    ##############
    charList = [] #luu cac operand -> khoi tao truth table
    
    for ch in Postfix:
        if(ch >= 'A' and ch <= 'Z'):
            charList.append(ch)
            
    charList = list(set(charList)) #set de xoa phan tu trung lap -> chuyen lai thanh list de sort
    charList.sort() #sort de xep theo thu tu A, B, C, ...

    Truthtable = generate_table(len(charList))
    ################
    stack = [] #dung de tinh toan
    for ch in Postfix:
        if(ch >= 'A' and ch <= 'Z'):
            stack.append(ch)

        if ch == '~':
            arg = stack.pop()
            charList.append(''.join('~'+arg))
            stack.append(''.join('~'+arg))
            tmpList = [ not a[charList.index(arg)] for a in Truthtable]
            Truthtable = mergeTable(tmpList,Truthtable)

        if ch == '&':
            arg1 = stack.pop()
            arg2 = stack.pop()
            charList.append(''.join(arg2+'&'+arg1))
            stack.append(''.join(arg2+'&'+arg1))
            tmpList = [a[charList.index(arg1)] and a[charList.index(arg2)] for a in Truthtable]
            Truthtable = mergeTable(tmpList,Truthtable)
        if ch == '|':
            arg1 = stack.pop()
            arg2 = stack.pop()
            charList.append(''.join(arg2+'|'+arg1))
            stack.append(''.join(arg2+'|'+arg1))
            tmpList = [a[charList.index(arg1)] or a[charList.index(arg2)] for a in Truthtable]
            Truthtable = mergeTable(tmpList,Truthtable)
        if ch == '>':
            arg1 = stack.pop()
            arg2 = stack.pop()
            charList.append(''.join(arg2+'>'+arg1))
            stack.append(''.join(arg2+'>'+arg1))
            tmpList = [lImplies(a[charList.index(arg2)], a[charList.index(arg1)]) for a in Truthtable]
            Truthtable = mergeTable(tmpList,Truthtable)
        if ch == '=':
            arg1 = stack.pop()
            arg2 = stack.pop()
            charList.append(''.join(arg2+'>'+arg1))
            stack.append(''.join(arg2+'>'+arg1))
            tmpList = [a[charList.index(arg1)] == a[charList.index(arg2)] for a in Truthtable]
            Truthtable = mergeTable(tmpList,Truthtable)

    return Truthtable

def mergeTable(r,Truthtable):
  i = 0
  res = []
  for tup in Truthtable:
    li = list(tup)
    li.append(r[i])
    i+=1
    res.append(tuple(li))

  return res

#logical connective

def lImplies(p,q):
    if p==True:
        return q
    else:
        return True

##########################################End student part
def writeTruthtable(table):
    import sys
    outfile=sys.argv[0]
    outfile=outfile[0:-2]
    outfile+="txt"
    with open(outfile, 'w') as f:
        for lines in table:
            for item in lines:
                f.write("%s\t" % item)
            f.write("\n")
    f.close()

def main():
    Infix=readInfix("logicexpression.txt")
    Postfix=Infix2Postfix(Infix)
    Truthtable=Postfix2Truthtable(Postfix)
    writeTruthtable(Truthtable)
main()