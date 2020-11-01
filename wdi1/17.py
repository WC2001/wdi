a = 1
b = 1
c = 2

i = 0
n = int(input())
while i<n:
    print(b/a)
    c = a + b
    a = b
    b = c
    i+=1