def f(x):
    a = 2
    while a<=x:
        if(x%a==0):
            return True
        a += 2*a +1
    return False



n = int(input())

print(f(n))
