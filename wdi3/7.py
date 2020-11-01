from random import randint, seed
n = int(input())
seed()
t = [randint(1, 1000) for _ in range(n)]
print(t)
for i in range(n):
    g = 0
    while t[i] > 0:
        if t[i] % 2 == 0:
            g = 1
            break
        t[i] //= 10
    if g == 0:
        print("tak")
        g = 1
        break
if g == 0:
    print("nie")



