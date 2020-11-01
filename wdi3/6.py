from random import randint, seed
n = int(input())
seed()
t = [randint(1,1000) for _ in range(n)]
print(t)
for i in range(len(t)):
    l = 0
    while t[i] > 0:
        if t[i] % 2 == 1:
            l += 1
        t[i] //= 10
    if l == 0:
        print("NIE")
        break
if l > 0:
    print("TAK")