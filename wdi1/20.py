x = float(input())
y = float(input())

eps = 0.000001
while abs(x-y)>eps :
    b = (x * y)**(1/2)
    a = (x+y)/2.0
    x = a
    y = b
print(x)