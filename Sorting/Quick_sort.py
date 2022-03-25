import random

def Partition(A,left,right): # pivot last
    pivot = A[right]
    min_index = left - 1
    for i in range(left, right):
        if A[i] < pivot:
            min_index += 1
            A[i], A[min_index] = A[min_index], A[i]
    A[min_index + 1], A[right] = A[right], A[min_index + 1]
    return (min_index + 1)

def Quick_sort(A,left,right):  # not stable
    if right - left > 0:
        p = Partition(A,left,right)
        Quick_sort(A,left,p-1)
        Quick_sort(A,p+1,right)
    return A

#test array
A = []
for i in range(30):
    A.append(random.randrange(50))
print("test array:",A)

print(Quick_sort(A[:],0,len(A)-1))