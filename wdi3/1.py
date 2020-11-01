def zpl(n,podstawa):
    s = "0123456789ABCDEF"
    wynik = ""
    while n > 0:
        wynik = s[n%podstawa] + wynik
        n //= podstawa
    return wynik

print(zpl(255,16))