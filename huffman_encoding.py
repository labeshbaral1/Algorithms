import heapq

F = [40, 10, 10, 10, 30]


def encode(F):

    L = [None for i in range(2 * len(F))]
    R = [None for i in range(2 * len(F))]
    P = [None for i in range(2 * len(F))]
    Q = [(F[i], i) for i in range(len(F))]
    heapq.heapify(Q)
    for i in range(len(F), 2 * (len(F))):
        
        if Q:
            (x_f, x_i) = heapq.heappop(Q)
            P[x_i] = i 
            L[i] = x_i 


        if Q:
            (y_f, y_i) = heapq.heappop(Q)
            P[y_i] = i 
            R[i] = y_i 

        else:
            (y_f, y_i) = (0, None)

       
        heapq.heappush(Q, (x_f+y_f, i))

    P[-1] = None
    return (L, R, P)



print(encode(F))


