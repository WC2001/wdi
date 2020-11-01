a = int(input())

b = 0
d = a
while a>0:
    c = a%2 #10
    a = a//2
    b = b*2 + c

if b == d:
    print("TAK")

else:
    print("NIE")