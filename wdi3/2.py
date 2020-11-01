def f(n,m):
    v = [0]*10
    w = [0]*10
    while n>0:
        v[n%10]+=1
        n//=10
    while m>0:
        w[m%10]+=1
        m//=10
    if v == w:
        return True
    return False

n = int(input())
m = int(input())
print(f(n,m))
