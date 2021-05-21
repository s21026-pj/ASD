import random
import threading
import sys


def Heapify(A, i, heapSize):
    l = i * 2 + 1
    r = i * 2 + 2
    if l < heapSize and A[i] < A[l]:
        largest = l
    else:
        largest = i

    if r < heapSize and A[r] > A[largest]:
        largest = r

    if i != largest:
        A[largest], A[i] = A[i], A[largest]
        Heapify(A, largest, heapSize)


def BuildHeap(A):
    heapsize = len(A)
    for i in range(heapsize // 2 - 1, 0, -1):
        Heapify(A, i, heapsize)


def HeapSort(A):
    BuildHeap(A)
    heapsize = len(A)
    for i in range(heapsize - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapsize -= 1
        Heapify(A, 0, heapsize)


def quickSort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quickSort(array, p, q - 1)
        quickSort(array, q + 1, r)

def quickSort2(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quickSort(array, p, q - 1)
        quickSort(array, q + 1, r)

def partition(array, p, r):
    pivot = array[r]
    pointer = p

    for i in range(p, r):
        if array[i] <= pivot:
            array[pointer], array[i] = array[i], array[pointer]
            pointer = pointer + 1

    array[pointer], array[r] = array[r], array[pointer]

    return pointer


def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


randomlist = []

for i in range(0, 2000):
    n = random.randint(1, 9223372036854775807)
    randomlist.append(n)

if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    threading.stack_size(200000000)


    thread = threading.Thread(target=quickSort(randomlist, 0, len(randomlist) - 1))
    thread.start()
    thread = threading.Thread(target=quickSort2(randomlist, 0, len(randomlist) - 1))
    thread.start()
    thread = threading.Thread(target=HeapSort(randomlist))
    thread.start()
    thread = threading.Thread(target=bubbleSort(randomlist))
    thread.start()
