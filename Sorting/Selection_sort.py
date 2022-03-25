import random

def Select_sort(A):  # not stable
    n = len(A)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if A[min_index] > A[j]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return A


'''
Time Complexity: O(n^2) as there are two nested loops.
Auxiliary Space: O(1)
The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write is a costly operation.
Stability : The default implementation is not stable. However it can be made stable.
In Place : Yes, it does not require extra space.
'''


def Select_sort_stable(A):  # stable , slower , np przy pomocy linked list
    n = len(A)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if A[min_index] > A[j]:
                min_index = j
        value_of_replacing_element = A[min_index]
        while min_index > i:
            A[min_index] = A[min_index-1]
            min_index -= 1
        A[i] = value_of_replacing_element
    return A


#test array
A = []
for i in range(30):
    A.append(random.randrange(50))
print("test array:",A)

print(Select_sort(A[:]))
print(Select_sort_stable(A[:]))