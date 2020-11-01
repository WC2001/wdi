def sumaDzielnikow(x):
    i=2
    suma = 1
    while i*i<=x:
        if x%i==0:
            suma+=i
            if int(x/i)!=i:
                suma +=int(x/i)
        i+=1
    return suma

k = 2

while k<n:
    
    if sumaDzielnikow(sumaDzielnikow(k))==k and sumaDzielnikow(k) >k:
        print(k,sumaDzielnikow(k))
    k+=1