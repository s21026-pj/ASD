def partition(array, n):
    largest = array[0]
    for i in range(1, n - 1):
        if array[i] > largest:
            largest = array[i]
            break

    pivot = largest
    pointer = 0

    for i in range(0, n - 1):
        if array[i] < pivot:
            array[pointer], array[i] = array[i], array[pointer]
            pointer = pointer + 1

    array[pointer], array[n - 1] = array[n - 1], array[pointer]


A = [6, 6, 6, 6, 168, 6, 168, 168]
n = len(A)
partition(A, n)
print(A)

