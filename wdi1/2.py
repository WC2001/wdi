def f(n,m,o):
    if n == 1:
        return o
    if n==2:
        return m
    else:
        return f(n-1,m,o)+f(n-2,m,o)


n = 1
m = 1
o = 1
wynik = 2020
wynik1 = 0
wynik2 = 0

while o<wynik: # 404,404 jest ok, przpadki w których o - pierwszy wyraz jest większy mają większą sumę zatem nie szukamy dalej
    n = 1
    
    while True:
        if f(n,m,o) > 2020:
            break
        if f(n,m,o) == 2020 and m + o < wynik:
            wynik = m + o #zmieniamy wynik na mniejszy
            wynik1 = o
            wynik2 = m
        n+=1
    m+=1
    if o+m>wynik:
        o+=1
        m = o


print(wynik1,wynik2)
