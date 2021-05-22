import timeit

def bubbleSort(arr):
    n = len(arr)

    for i in range(n - 1):

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [2,8,7,1,3,5,6,4, 14, 20, 70, 3]

bubbleSort(arr)

timecalc = timeit.timeit(lambda: bubbleSort(arr), number=100)
print(timecalc)

for i in range(len(arr)):
    print("%d" % arr[i]),

