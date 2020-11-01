a = int(input())
b = int(input())
n = int(input())
c = a // b
print(c,'.',end='',sep='')
r = a % b
for i in range(n):
    r *= 10
    print(r//b,end='')
    r = r%b

