i = 3
ile = 1
wynik = 2
while i < 10000:
    k = 0
    a = i
    while a != 1:
        while a%2 ==0:
            a/=2
            k+=1
        if a != 1 :
            a = 3*a + 1
            k+=1
    
    if k > ile:
        ile = k
        wynik = i
    i+=1

print(wynik)