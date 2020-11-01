n = int(input())
l = 0
m = n
c = 0
v = []
while m>0:
    c+=1
    m//=10

for i in range (1,2**c):
    m = n
    i2=i
    gen = 0
    mnoznik = 1
    for j in range (c):
        if(i2%2==1):
            gen += m%10 * mnoznik
            mnoznik *= 10
        m//=10
        i2//=2
    v.append(gen)
    if(gen%7==0):
        l+=1
        
print(l)
print(v)