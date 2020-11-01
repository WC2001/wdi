def f(x):
    a = 3
    i = 4
    while a <=n:
        if(n%a==0):
            return True
        a+=i
        i+=2
    return False

n = int(input())

print(f(n))


