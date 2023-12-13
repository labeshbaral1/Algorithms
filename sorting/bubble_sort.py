def bubble_sort(A):

    def swap(i,j):
        A[i], A[j] = A[j], A[i]

    for i in range(len(A)-1, 0, -1):
        for j in range(i):
            if A[i] < A[j]:
                swap(i, j)
    return A




A = [1,32,4,1,43,5,1,23,2,1,7,12]
print(bubble_sort(A))