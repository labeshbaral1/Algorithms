import heapq

def decrement_vertex(PQ, neighbor, new_weight):
    for i, (weight, name) in enumerate(PQ):
        if name == neighbor:
            PQ[i] = (new_weight, name)
            break
    heapq.heapify(PQ)

def djikstra(G, s):

    d = {vertex: float("inf") for vertex in G}
    d[s] = 0


    PQ = [(d[vertex], vertex) for vertex in G]
    heapq.heapify(PQ)

    while PQ:

        current_distance, u = heapq.heappop(PQ)
        if current_distance > d[u]:
            continue


        for neighbor, weight in G[u].items():
            distance = current_distance + weight
            if distance < d[neighbor]:
                d[neighbor] = distance
                decrement_vertex(PQ, neighbor, distance)

    return d


G = {
    'a': {'s': 2, 'b': 20},
    'b': {'s': 20, 'd': 14, 'a': 20},
    's': {'b': 20, 'i': 16, 'e': 10, 'a': 2},
    'd': {'b': 14, 'i': 4, 'e': 30, 'f': 40},
    'i': {'s': 16, 'd': 4, 'e': 2},
    'e': {'d': 30, 'g': 12, 's': 10, 'i': 2, 'f': 22},
    'g': {'f': 30, 'h': 8, 'e': 12},
    'f': {'g': 30, 'd': 40, 'e': 22},
    'h': {'g': 8}
}

print(djikstra(G, 's'))
