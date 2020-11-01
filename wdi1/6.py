acc = 0.0000001

val = 2020

a = 4
b = 5


while b-a > acc:
    x = (a+b)/2
    if(x**x > 2020):
        b = x
    else :
        a = x
print(x)