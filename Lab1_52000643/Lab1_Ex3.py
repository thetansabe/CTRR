def sum(n):
    sum = 0
    if(n >= 0):
        for i in range(1,n):
            sum +=i
        
    else:
        for i in range(n,1):
            sum +=i
    return sum

print(sum(5))
print(sum(-5))
