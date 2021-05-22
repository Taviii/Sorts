import timeit


def heapify(numbers, heap_size, index):
    max = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < heap_size and numbers[left] > numbers[max]:
        max = left

    if right < heap_size and numbers[right] > numbers[max]:
        max = right

    if max != index:
        numbers[index], numbers[max] = numbers[max], numbers[index]
        heapify(numbers, heap_size, max)


def heap_sort(numbers):
    n = len(numbers)

    for i in range(n, -1, -1):
        heapify(numbers, n, i)

    for i in range(n - 1, 0, -1):
        numbers[i], numbers[0] = numbers[0], numbers[i]
        heapify(numbers, i, 0)


random = [2,8,7,1,3,5,6,4, 14, 20, 70, 3]
time1 = timeit.timeit(lambda: heap_sort(random), number=100)

print(time1)

heap_sort(random)

print(random)
