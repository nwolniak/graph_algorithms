import random

def Insertion_sort(A):
    n = len(A)
    for i in range(1,n):
        current_value = A[i]
        j = i-1
        while j >= 0 and A[j] > current_value:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = current_value
    return A
'''
Time Complexity: O(n*2)
Auxiliary Space: O(1)
Boundary Cases: Insertion sort takes maximum time to sort if elements are sorted in reverse order.
And it takes minimum time (Order of n) when elements are already sorted.
Algorithmic Paradigm: Incremental Approach
Sorting In Place: Yes
Stable: Yes
Online: Yes
'''


#test array
A = []
for i in range(30):
    A.append(random.randrange(50))
print("test array:",A)

print(Insertion_sort(A[:]))