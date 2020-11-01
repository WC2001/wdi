def f(x):
    j = x%10
    x //= 10
    while x>0:
        if j == x%10:
            return False
        x //=10
    return True

n = int(input())
print(f(n))