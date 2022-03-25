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

def Bucket_sort(A):
    n = len(A)
    buckets = [[] for i in range(n+1)]   # dla wartosci [0:1) inaczej (n+1)
    for element in A:
        buckets[int((n)*element)].append(element)
    for i in range(n):
        buckets[i] = Insertion_sort(buckets[i])

    k = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            A[k] = buckets[i][j]
            k += 1
    return A



A = []
for i in range(30):
    A.append(random.random())

print(A)
print(Bucket_sort(A))