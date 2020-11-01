from math import log
from math import ceil
def zpl(liczba,podstawa):
    hex = "0123456789ABCDEF"
    tab = [0 for i in range (ceil(log(liczba,podstawa)))] #dodać 1
    i = 0
    while liczba >0:
        tab[i] = hex[liczba%podstawa]
        liczba //= podstawa
        i+=1
    tab.reverse()
    for j in tab:
        print(j,end="")

zpl(29,16)


