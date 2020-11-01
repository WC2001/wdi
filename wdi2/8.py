def f(x):
    v = [0,1,2]
    a1 = 1
    a2 = 1
    a3 = 2
    suma = 2
    while a3<=x+1:
        a3 = a1+a2
        a1 = a2
        a2 = a3
        suma += a3
        v.append(suma)

    for i in range (x+1,a3):
        g = 0
        for j in range(1,len(v)):
            if(v[j]-v[j-1]==i):
                g+=1
        if g ==0:
            return i        

    return a3

n = int(input())

print(f(n))