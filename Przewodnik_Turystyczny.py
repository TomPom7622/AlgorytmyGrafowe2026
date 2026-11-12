from dimacs import *
import heapq

def dijkstra(start, graf):
    n = len(graf)
    #w dist zapisuwane będą 
    dist = [float('-inf')] * n
    dist[start] = float('inf')

    heap = [(-dist[start], start)]

    while heap:
        d, u = heapq.heappop(heap)
        d = -d
        if d < dist[u]:
            continue

        for v, w in graf[u]:#przechdzimy po sasiadach
            new_dist = min(dist[u], w)

            if new_dist > dist[v]:
                dist[v] = new_dist
                heapq.heappush(heap, (-dist[v], v))

    return dist

V, L = loadWeightedGraph("g1")
g1 = [[] for _ in range(V + 1)]

#tworzenie listy sasiedztwa:
for u, v, c in L:
    g1[u].append((v, c))
    g1[v].append((u, c))
    print(u, v, c)

print(dijkstra(1, g1)[4])

