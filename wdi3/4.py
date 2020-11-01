n = int(input())
silnia = 1
i = 0
to_add = [0]*n
result = [0]*n
to_add[0] = 1 #1.00000000000000
while True:
    to_add = 1/silnia
    if to_add == 0:
        break
    #result += to_add
    p = 0
    for i in range(n-1, -1, -1):
        tmp = result[i] + to_add[i] + p
        result[i] = tmp % 10
        p = tmp // 10

    i += 1
    silnia *= i
    
print(result)


