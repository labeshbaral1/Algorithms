def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def heapify(A, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and A[largest] < A[l]:
        largest = l

    if r < n and A[largest] < A[r]:
        largest = r

    if largest != i:
        swap(A, i, largest)
        heapify(A, n, largest)

def heap_sort(A):
    n = len(A)

    for i in range(n//2 - 1, -1, -1):
        heapify(A, n, i)

    for i in range(n-1, 0, -1):
        swap(A, 0, i)
        heapify(A, i, 0)

    return A

print(heap_sort([14, 1, 2, 4, 9, 8, 6, 13]))
