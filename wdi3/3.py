def sito(x):
    t = [0]*(x+1)
    v = []
    i = 2
    while i*i<=x:
        if not t[i] :
            j = i*2
            while j <=n:
                t[j] = 1
                j+=i
        i+=1
    for k in range(2,x):
        if not t[k]:
            v.append(k)
    return v

n = int(input())
print(sito(n))