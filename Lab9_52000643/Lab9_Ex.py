import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

################EX2: plot a graph
def Ex2a():
    A2 = np.array([[0,0,3,0,1],
    [0,0,5,3,0],
    [0,0,0,1,0],
    [0,0,0,0,2],
    [0,0,0,0,0]])

    G2 = nx.from_numpy_matrix(A2)
    pos=nx.spring_layout(G2)
    nx.draw_networkx(G2,pos=pos,with_labels=True,labels={a:b for
    a,b in enumerate('abcde')})
    edge_labels = nx.draw_networkx_edge_labels(G2,font_size=6,
    pos=pos,label_pos=0.5)
    plt.axis('equal')
    plt.show()

def Ex2b():
    A3 = np.array([[0,0,0,0,1,1],
    [0,0,5,3,0,0],
    [0,0,0,1,5,0],
    [0,0,0,0,2,3],
    [0,0,0,0,0,6],
    [0,0,0,0,0,0]])

    G3 = nx.from_numpy_matrix(A3) #tao graph tu matrix
    pos=nx.spring_layout(G3)
    nx.draw_networkx(G3,pos=pos,with_labels=True,labels={a:b for
    a,b in enumerate('abcdef')})
    edge_labels = nx.draw_networkx_edge_labels(G3,font_size=6,
    pos=pos,label_pos=0.5)
    plt.axis('equal')
    plt.show()

#################EX3: Plot graph from list of edges
def Ex3a():
    A4 = np.array([[0,0,5,3,0,0],
    [0,0,3,2,0,0],
    [0,0,0,1,3,0],
    [0,0,0,0,1,3],
    [0,0,0,0,0,4],
    [0,0,0,0,0,0]])

    G4 = nx.from_numpy_matrix(A4) #tao graph tu matrix
    pos=nx.spring_layout(G4)
    nx.draw_networkx(G4,pos=pos,with_labels=True,labels={a:b for
    a,b in enumerate('abcdef')})
    edge_labels = nx.draw_networkx_edge_labels(G4,font_size=6,
    pos=pos,label_pos=0.5)
    plt.axis('equal')
    plt.show()

def Ex3b():
    A5 = np.array([[0,0,2,3,3,0],
    [0,0,3,2,0,0],
    [0,0,0,2,8,6],
    [0,0,0,0,0,5],
    [0,0,0,0,0,3],
    [0,0,0,0,0,0]])

    G5 = nx.from_numpy_matrix(A5) #tao graph tu matrix
    pos=nx.spring_layout(G5)
    nx.draw_networkx(G5,pos=pos,with_labels=True,labels={a:b for
    a,b in enumerate('abcdef')})
    edge_labels = nx.draw_networkx_edge_labels(G5,font_size=6,
    pos=pos,label_pos=0.5)
    plt.axis('equal')
    plt.show()

################From graph to list of edges
A1=np.array([[0,3,5,2],
[0,0,2,0],
[0,0,0,3],
[0,0,0,0]])

A5 = np.array([[0,0,2,3,3,0],
    [0,0,3,2,0,0],
    [0,0,0,2,8,6],
    [0,0,0,0,0,5],
    [0,0,0,0,0,3],
    [0,0,0,0,0,0]])

def toLoE(A):
    arr = []
    labels = ['A','B','C','D','E','F','G','H','I']
    i = -1
    for r in A:
        i += 1
        k = -1 #reset from A
        for c in r:
            k += 1
            if(c != 0):
                arr.append((labels[i],labels[k],c))
    return arr   

#print(toLoE(A5))
# Ex2a()
# Ex2b()
# Ex3a()
# Ex3b()

#print('pos',pos)

A5 = np.array([[0,0,2,3,3,0],
    [0,0,3,2,0,0],
    [0,0,0,2,8,6],
    [0,0,0,0,0,5],
    [0,0,0,0,0,3],
    [0,0,0,0,0,0]])

G5 = nx.from_numpy_matrix(A5) #tao graph tu matrix
pos=nx.spring_layout(G5) #dict: luu toa. do cua 6 key (6 vertex)  
#print('pos',pos)
nx.draw_networkx(G5,pos=pos,with_labels=True,labels={a:b for
a,b in enumerate('abcdef')}) #ve network voi' cac label tren vertex

edge_labels = nx.draw_networkx_edge_labels(G5,font_size=6,
pos=pos,label_pos= 0.5) #them label cho edge

plt.axis('equal') #can graph trong 1 o vuong (truc x = truc y)
plt.show() #draw_ => ve len tren plt roi` nen chi can .show() ra