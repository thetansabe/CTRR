import re

def formalConvert(str):
  strSpl = re.split('^For all |Exist |Every|There is at least one ',str)[1]
  str1 = strSpl.split(',')
  D = str1[0]
  S = str1[1][str1[1].index(' ', 1) + 1:]
  if(str.startswith('For all')):
    F = 'For all x in D, P(x)'
  else:
    F = 'Exist x in D, such that P(x)'
  return [D, S, F]

def printResult(str, res):
  print(str)
  print('D is: ' + res[0])
  print('P is: ' + res[1])
  print('Formal form: ' + res[2])

ex2a = 'For all fishes, they need water to survive'
print('--------------------------------2a-------------------------------')
printResult(ex2a, formalConvert(ex2a))
ex2b = 'Exist a person, who is left handed'
print('--------------------------------2b-------------------------------')
printResult(ex2b, formalConvert(ex2b))
ex2c = 'Exist an employee in the company, who is late to work everyday'
print('--------------------------------2c-------------------------------')
printResult(ex2c, formalConvert(ex2c))
ex2d = 'For all fishes in this pond, they are Koi fish'
print('--------------------------------2d-------------------------------')
printResult(ex2d, formalConvert(ex2d))
ex2e = 'There is at least one creature in the ocean, it can live on land'
print('--------------------------------2e-------------------------------')
printResult(ex2e, formalConvert(ex2e))
ex2f = 'Exist a bird, who have wing but can’t fly'
print('--------------------------------2f-------------------------------')
printResult(ex2f, formalConvert(ex2f))


def formalConvertPQ(str):
  strSpl = re.split('^For all |For every |Exist |Every|at least ',str)[1]
  str1 = strSpl.split(',')
# D la string ngay sau for all, exist, ...va truoc' dau' ,
  D = str1[0]
# xu li sau dau' , de tim P va Q
  strSpl2 = re.split('^ if they | whose | who ',str1[1])[1]
    # xu li clause if then phia sau
  P = re.split('.then they |but |then |they',strSpl2)[0]
  Q = re.split('.then they |but |then |they',strSpl2)[1]
  if(str.startswith('For all') or str.startswith('For every')):
    F = 'For all x in D, P(x) -> Q(x)'
  else:
    F = 'Exist x in D, P(x) ^ Q(x)'
  return [D,P, Q, F]

def printResultPQ(str, res):
  print(str)
  print('D is: ' + res[0])
  print('P is: ' + res[1])
  print('Q is: ' + res[2])
  print('Formal form: ' + res[3])

ex4a = 'For all people, if they are blond then they are westerners'
print('--------------------------------4a-------------------------------')
printResultPQ(ex4a, formalConvertPQ(ex4a))

ex4b = 'Exist a person, whose hair is black but is a westerner'
print('--------------------------------4b-------------------------------')
printResultPQ(ex4b, formalConvertPQ(ex4b))

ex4c = 'For all students, if they study correctly then they have high score'
print('--------------------------------4c-------------------------------')
printResultPQ(ex4c, formalConvertPQ(ex4c))

ex4f = 'Exist a bird, who have wing but can’t fly'
print('--------------------------------4f-------------------------------')
printResultPQ(ex4f, formalConvertPQ(ex4f))

ex4e = 'For every bird, if they don’t have wings and can swim then they are penguins'
print('--------------------------------4e-------------------------------')
printResultPQ(ex4e, formalConvertPQ(ex4e))


def formalConvertPQ2(str):
  strSpl = re.split('^For every ',str)[1]
  str1 = strSpl.split(',')
# D la string ngay sau for all, exist, ...va truoc' dau' ,
  D = str1[0]
# xu li sau dau' , de tim P va Q
  P = re.split('^ if they ',str1[1])[1]
  Q = re.split('^ they ',str1[2])[1]
  if(str.startswith('For every')):
    F = 'For all x in D, P(x) -> Q(x)'
  else:
    F = 'Exist x in D, P(x) ^ Q(x)'
  return [D,P, Q, F]

ex4d = 'For every mammal, if they live in the sea, they are either dolphins or whales'
print('--------------------------------4d-------------------------------')
printResultPQ(ex4d, formalConvertPQ2(ex4d))