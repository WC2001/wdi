x = int(input())

v = [1,1]
i = 1
while v[i] * v[i-1] <= x:
    v.append(v[i]+v[i-1])
    i+=1


k = 1
g = 0

while k<len(v):
    if v[k]*v[k-1] == x:
        print('true')
        g = 1
        break
    k+=1


if g==0:
    print('false')