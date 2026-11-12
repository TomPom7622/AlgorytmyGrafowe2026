from dimacs import *
from queue import PriorityQueue
def Dijkstra(G,s,t):
    n=len(G)
    d=[float("-inf") for _ in range(n)]
    Q=PriorityQueue()

    d[s]=0
    Q.put((float("-inf"),s))

    while not Q.empty():
        w,v =Q.get()
        w = -w
        if w>=d[v]:
            for u,w2 in G[v]:
                newDist=min(w,w2)
                if newDist>d[u]:
                    d[u]= newDist
                    Q.put((-d[u],u))

    return d[t]

def main():
    (V, L) = loadWeightedGraph("graphs-lab1\\g1")
    G=[ [] for _ in range(V)]
    for v,u,w in L:
        G[v-1].append((u-1,w))
        G[u-1].append((v-1,w))
    return Dijkstra(G,0,1)

print(main())
