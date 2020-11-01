def podzielniki(x):
    i = 2
    if x ==1:
        return 1
    v = [1,x]
    while i*i<=x:
        if x%i==0:
            v.append(i)
            if x!=i*i:
                v.append(int(x/i))
        i+=1

    v.sort()   
    return v

x = int(input())
print(podzielniki(x))