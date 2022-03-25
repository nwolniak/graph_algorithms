import random
# zlozonosc O(n)
# metoda wysoce ekstensywna czyli potrzebujaca duzej dodatkowej pamieci
# oplaca sie gdy zakres kluczy jest maly

def Counting_sort(A,k):  # k - zakres kluczy
    n = len(A)
    B = [None]*n  # tablica wynikowa
    C = [0]*k  # tablica kluczy
    for i in range(n):  # zliczanie wystapien wartosci elementow
        C[A[i]] += 1
    for i in range(1,k):  # ile elementow <= jest dla danej wartosci
        C[i] += C[i-1]
    for i in range(n-1,-1,-1):  # umieszczanie w tablicy B
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    return B

#test array
A = []
for i in range(30):
    A.append(random.randrange(50))
print("test array:",A)

print(Counting_sort(A,51))