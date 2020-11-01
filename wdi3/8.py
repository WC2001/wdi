from random import randint, seed
n = int(input())
seed()
t = [randint(0, 10000000) for _ in range(n)]
print(t)
