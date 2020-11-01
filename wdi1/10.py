def sumaDzielnikow(x):
    if x==1:
        return 0
    i=2
    suma = 1
    while i*i<=x:
        if x%i==0:
            suma+=i
            if int(x/i)!=i:
                suma +=int(x/i)
        i+=1
    return suma

k = 1
while k<1000000:
    if sumaDzielnikow(k)==k:
        print(k)
    k+=1
