import random

def Merge(A,left,mid,right):
    L = A[left:mid + 1]
    R = A[mid + 1:right + 1]
    i = j = 0
    k = left
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1

def Merge_sort(A,left,right):
    n = len(A)
    if right - left > 0:
        mid = (left+right)//2
        Merge_sort(A,left,mid)
        Merge_sort(A,mid+1,right)
        Merge(A,left,mid,right)
    return A


'''
Time Complexity: Sorting arrays on different machines. Merge Sort is a recursive algorithm and time complexity can be 
expressed as following recurrence relation.
T(n) = 2T(n/2) + \Theta(n)
The above recurrence can be solved either using Recurrence Tree method or Master method. It falls in case II of 
Master Method and solution of the recurrence is \Theta(nLogn).
Time complexity of Merge Sort is \Theta(nLogn) in all 3 cases (worst, average and best) as merge sort always divides 
the array into two halves and take linear time to merge two halves.

Auxiliary Space: O(n)
Algorithmic Paradigm: Divide and Conquer
Sorting In Place: No in a typical implementation
Stable: Yes
'''


#test array
A = []
for i in range(30):
    A.append(random.randrange(50))
print("test array:",A)

print(Merge_sort(A[:],0,len(A)-1))