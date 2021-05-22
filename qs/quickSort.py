import timeit

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)


def partition(A, p, r):
    pivot = A[r]
    smaller = p

    for j in range(p, r):
        if A[j] <= pivot:
            A[smaller], A[j] = A[j], A[smaller]
            smaller = smaller + 1

    A[smaller], A[r] = A[r], A[smaller]

    return smaller

A = [2,8,7,1,3,5,6,4, 14, 20, 70, 3]

quickSort(A, 0, len(A) - 1)

timecalc = timeit.timeit(lambda : quickSort(A, 0, len(A) -1), number=100)
print(timecalc)

print(A)