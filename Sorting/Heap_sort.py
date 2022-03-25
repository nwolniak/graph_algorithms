import random

def heapify(A,i,n):
    left = i*2 + 1
    right = i*2 + 2
    max = i
    if left < n and A[left] > A[max]:
        max = left
    if right < n and A[right] > A[max]:
        max = right
    if max is not i:
        A[i], A[max] = A[max], A[i]
        heapify(A,max,n)

def build_heap(A):
    n = len(A)
    for i in range( (n//2 -1),-1,-1): # to the root node
        heapify(A,i,n)

def heap_sort(A):
    n = len(A)
    build_heap(A)  # build max heap
    for i in range(n-1,0,-1):
        A[0], A[i] = A[i], A[0]  # change last and first ( max ), put max at the end of the array
        heapify(A,0,i)
    return A


'''
Notes:
Heap sort is an in-place algorithm.
Its typical implementation is not stable, but can be made stable
Time Complexity: Time complexity of heapify is O(Logn). Time complexity of createAndBuildHeap() is O(n) and
overall time complexity of Heap Sort is O(nLogn).
Applications of HeapSort
1. Sort a nearly sorted (or K sorted) array
2. k largest(or smallest) elements in an array
'''

# iterative heap_sort

def build_heap_it(A):
    n = len(A)
    for i in range(n):
        if A[i] > A[(i-1)//2]:
            j = i
            while A[j] > A[(j-1)//2]:
                A[j], A[(j-1)//2] = A[(j-1)//2], A[j]
                j = (j-1)//2

def heap_sort_it(A):
    n = len(A)
    build_heap_it(A)
    for i in range(n-1,0,-1):
        A[0], A[i] = A[i], A[0]
        parent = 0
        child = 0
        while child < i:
            child = parent*2 + 1
            if child < i-1 and A[child] < A[child + 1]:
                child +=1
            if child < i and A[parent] < A[child]:
                A[parent], A[child] = A[child], A[parent]
            parent = child
    return A


#test array
A = []
for i in range(30):
    A.append(random.randrange(50))
print("test array:",A)

print(heap_sort(A[:]))
print(heap_sort_it(A[:]))