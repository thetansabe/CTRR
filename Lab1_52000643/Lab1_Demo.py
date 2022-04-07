# Basic data types
x=3
print(type(x))
print(x**2)
x+=1
print(x)

y=2.5
print(type(y))
print(y,y+1,y+2,y**2)
    #python doesnt have x++ x--
    #for boolean logic python use and or not && ||

t=True
f=False
print(type(t)) #class: bool not boolean
print(not t)
print(t != f) #XOR
print(t and f)
print(t or f)

hello ='hello' #this is string literals: cai gia tri. the hien ban chat string cua no
world ="world" #double quote cho string cung dc
print(hello)
print(len(hello)) #len()
hw = hello + ' '+world #string concat
hw12= '%s %s %d' %(hello,world,12) #formatting
print(hw12)

s="hello"
print(s.capitalize()) #uppercase ONLY FIRST character
print(s.upper()) #upper all
print(s.rjust(7)) #right-justify: padding with spaces to fullfill 7 spots
print(s.center(7)) #center the string by padding both left and right
print(s.replace('l','(ell)')) #replace l with (ell)
print(' world '.strip()) #giong trim()

#CONTAINERS
    #list
xs=[3,1,2]
print(xs,xs[2])
print(xs[-1])
xs[2] = 'foo' #gan lai. xs[2] = foo => 1 mang hon hop nh` kieu dl
print(xs) 
xs.append('bar')
print(xs)
x=xs.pop() #remove and return LAST element

    #SLICING list
nums = list(range(5)) #tao 5 ptu => [0,1,2,3,4]
print(nums)
print(nums[2:4]) #return [2,3] slice to INDEX 4
print(nums[2:]) #return [2,3,4] slice to end
print(nums[:]) #return whole list
print(nums[:2]) #from begin to INDEX 2
print(nums[:-1]) #can be negative
nums[2:4] = [8,9] #assign
print(nums)

    #LOOP
animals=['cat','dog','monkey']
for animal in animals:
    print(animal)

animals=['cat','dog','monkey']
#enumerate return value and index
for idx,animal in enumerate(animals):
    print('%d: %s' %(idx+1,animal))

    #LIST comprehension
num=[0,1,2,3,4]
squares = [x**2 for x in nums]
print(squares)

even_squares = [x**2 for x in nums if x%2==0]
print(even_squares)

#Dictionary
d = {'cat':'cute', 'dog':'furry'}
print(d['cat'])
print('cat' in d) #return bool to check if 'cat' exists
d['fish'] = 'wet' #ADD SET
print(d.get('monkey','N/A')) #if there is monkey return monkey value, if not return NA
del d['fish']

    #Loops
d = {'person':2,'cat':4,'spider':8}
for animal in d:
    legs = d[animal]
    print('A %s has %d legs' %(animal,legs))

for animal,legs in d.items():
    print('A %s has %d legs' %(animal,legs))

    #diction comprehension
nums = [0,1,2,3,4]
even_num_to_square = {x: x**2 for x in nums if x%2==0}
print(even_num_to_square)

#Set
animals = {'cat','dog'}
print('cat' in animals) #check
animals.add('fish') #ADD
print(len(animals))
animals.remove('cat')

    #Loops
animals = {'cat' , 'dog' , 'fish' }
for idx,animal in enumerate(animals):
    print('#%d: %s' %(idx + 1,animal))

    #Set comprehension
from math import sqrt
nums = { int(sqrt(x)) for x in range (30)} #loai bo so khac int
print ( nums )

#Tuples
d = {(x , x + 1): x for x in range ( 10 )} # Create a dictionary with tuple keys

t = (5 , 6 ) # Create a tuple
print ( type (t )) # Prints " < class ’ tuple ’ >"
print (d[t]) # Prints "5"
print (d[(1 , 2)])

#Function
def sign (x):
    if x > 0:
        return 'positive '
    elif x < 0:
        return 'negative '
    else :
        return 'zero '
for x in [-1 , 0 , 1]:
    print ( sign (x ))

def hello ( name , loud = False ):
    if loud :
        print ('HELLO , %s!' % name . upper () )
    else :
        print ('Hello , %s' % name )
    hello ('Bob ') # Prints " Hello , Bob "
    hello ('Fred ', loud = True ) # Prints " HELLO , FRED !" 

#Class
class Greeter ( object ):
# Constructor
    def __init__ ( self , name ):
        self.name = name # Create an instance variable

    # Instance method
    def greet ( self , loud = False ):
        if loud :
            print ('HELLO , %s!' % self.name.upper() )
        else :
            print ('Hello , %s' % self.name )

g = Greeter ('Fred ') # Construct an instance of the Greeter class
g. greet () # Call an instance method ; prints " Hello , Fred"

g. greet ( loud = True)