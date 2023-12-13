 
#              n1       n2
#[1,3,2,4] -> [1,2] -> [3, 4]

def merge(A, b, m, e):

    n1 = m - b + 1
    n2 = e - m
    L = [A[b+i] for i in range(n1)]
    L.append(float("inf"))
    R = [A[m+j+1] for j in range(n2)]
    R.append(float("inf"))
    
    i, j = 0,0

    for k in range(b, e +1):
        
        if L[i]<R[j]: 
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1
    


    

def merge_sort(A, b=0, e=None):
    if e==None: e = len(A)-1
    if b < e:
        m = (b + e) // 2
        merge_sort(A, b, m)
        merge_sort(A, m+1, e)
        merge(A, b, m, e)
    return A
    


print(merge_sort([14,1,2,4,9,8,6,13]))