import random
def counting_sort(A,k):
    n = len(A)
    B = [None]*n
    C = [0]*10
    for i in range(n):
        C[(A[i]//k)%10] +=1
    for i in range(1,10):
        C[i] += C[i-1]
    for i in range(n-1,-1,-1):  # stable
        C[(A[i]//k)%10] -= 1
        B[C[(A[i]//k)%10]] = A[i]
    for i in range(n):
        A[i] = B[i]

def Radix_sort(A,k): # k dlugosc maksymalna
    exp = 1
    for i in range(1,k+1):
        counting_sort(A,exp)
        exp *= 10
    return A

#test array
A = []
for i in range(30):
    A.append(random.randrange(50))
print("test array:",A)

print(Radix_sort(A,2))