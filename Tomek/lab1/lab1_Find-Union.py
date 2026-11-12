from dimacs import *
class Node:
    def __init__(self,val):
        self.parent=self
        self.rank=0
        self.value=val

def find_set(x):
    if x!=x.parent:
        x.parent=find_set(x.parent)
    return x.parent

def union(x,y):
    x=find_set(x)
    y=find_set(y)
    if x==y: return
    if x.rank>y.rank:
        y.parent=x
    else:
        x.parent=y
        if x.rank==y.rank:
            y.rank+=1

def sortEdgesDesc(E):
    return sorted(E,key = lambda x : x[2], reverse=True)

def main():
    (V, L) = loadWeightedGraph("graphs-lab1\\g1")
    L = sortEdgesDesc(L)
    N = [Node(i) for i in range(V)]
    for (v,u,w) in L:
        if