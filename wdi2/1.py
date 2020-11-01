def f(x):
    if x==1 or x==2:
        return 1
    else:
        return f(x-1)+f(x-2)


x = int(input())

