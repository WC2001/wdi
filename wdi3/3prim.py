from math import sqrt
from math import ceil
N = int(input(">>"))

tab = [True]*(N+1)
tab[0] = tab[1] = False

for i in range (2, ceil(sqrt(N)+1)):
    if tab[i]:
        for a in range(i*i,N,i):
            tab[a] = False
            
    i+=1
ile =0
for k in range (N):
    if tab[k]:
        print(k)
        ile += 1
print(ile)

