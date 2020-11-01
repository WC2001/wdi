x = int(input())

odd = 1
suma = 0
n = 0
while suma + odd <=x:
    suma += odd
    odd += 2
    n+=1
print(n)