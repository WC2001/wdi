def f(x):
    v = [x%10]
    c = 0
    while x>0:
        c+=1
        x //= 10
        v.append(x%10)
    for i in range(len(v)):
        if c == v[i]:
            return True
    return False

n = int(input())
print(f(n))
