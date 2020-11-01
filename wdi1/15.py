def f(x):
    if x==1:
        return 1/2
    else:
        return f(1) + 1/2 * (f(x-1))**(1/2)
    
wynik = 1/2
n = 2
while n<20:
    wynik *= f(n)
    n+=1
wynik **=(1/2)

print(2/wynik)