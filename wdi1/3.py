

suma = int(input())
v = [1,1]
i = 1
p = [0,1,2]
while v[i]+v[i-1]<=suma:
    v.append(v[i]+v[i-1])
    i+=1
    p.append(v[i]+p[len(p)-1])

k = 1

g = 0
print(p)
while k<len(p) and g == 0:
    j = 0
    while j<k and g == 0:
        if p[k]-p[j]==suma:
            print('true')
            g +=1
        j+=1
    k += 1

if g == 0:
    print('false')