import random

def partition(A,left,right):
    pivot = A[right]
    min_index = left-1
    for i in range(left,right):
        if A[i] < pivot:
            min_index += 1
            A[min_index], A[i] = A[i], A[min_index]
    A[min_index+1], A[right] = A[right], A[min_index+1]
    return min_index + 1

def select(A,left,right,k):
    if left == right:
        return A[left]
    p = partition(A,left,right)
    i = p-left + 1 # wielkosc sub tablicy
    if k == i: # dlugosc sub tablicy
        return A[p]
    if k < i :
        return select(A,left,p-1,k)
    else:
        return select(A,p+1,right,k-i)


'''
zlozonosc oczekiwana O(n)
zlozonosc pesymistyczna O(n^2)
'''

# test
A = []
for i in range(30):
    A.append(random.randrange(50))
print("test array",A)
print(select(A,0,len(A)-1,8))
A.sort()
print(A)