import random
def Bubble_sort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(1,n-i):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
    return A
'''
The above function always runs O(n^2) time even if the array is sorted.
It can be optimized by stopping the algorithm if inner loop didn’t cause any swap.
'''

def Bubble_sort_optimized(A):
    n = len(A)
    swapped = True
    i = 0
    while swapped:
        swapped = False
        for j in range(1, n-i):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                swapped = True
        i += 1
    return A
'''
Worst and Average Case Time Complexity: O(n^2). Worst case occurs when array is reverse sorted.
Best Case Time Complexity: O(n). Best case occurs when array is already sorted.
Auxiliary Space: O(1)
Boundary Cases: Bubble sort takes minimum time (Order of n) when elements are already sorted.
Sorting In Place: Yes
Stable: Yes
'''
#test array
A = []
for i in range(30):
    A.append(random.randrange(50))
print("test array:",A)

print(Bubble_sort(A[:]))
print(Bubble_sort_optimized(A[:]))