def f(x):
    a = x%10
    x //= 10
    while x>0:
        if x%10 >= a:
            return False
        a = x%10
        x //= 10
    return True


n = int(input())
print(f(n))
