def factorial(x):
    if x == 0:
        return 1
    else:
        return x*factorial(x-1)

n = int(input())

i = 0
wynik = 0
while i < n :
    wynik+= 1/factorial(i)
    i+=1
print(wynik)