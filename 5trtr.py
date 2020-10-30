def zpl(x,podstawa):
    s = "0123456789ABCDEF"
    wynik =""
    while x>0:
        wynik = s[x%podstawa] + wynik
        x //= podstawa
    return wynik

print(zpl(255,7))