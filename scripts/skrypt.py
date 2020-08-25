import random

liczba = random.randint(1,10)
print("Wylosowana liczba to: ", liczba)

#INSTRUKCJE WARUNKOWE

imie = 'Jan'
nazwisko ='Kowalski'
wiek = 30

if nazwisko == 'Kowalski' and wiek == 30:
    print('Cześć Kowalski, masz 30 lat')
else:
    print('To nie Ty')

if imie in ['Jan', 'Krzysztof'] and wiek == 30:
    print('Cześć Jan, masz 30 lat')
else:
    print('Nie jesteś Jan ani Krzysztof')

zmienna1 = 1
zmienna2 = 2
zmienna3 = 3

if zmienna1 > 0:
    print('1')
elif zmienna2 < 0:
    print('2')
else:
    print('same falsy')

#PĘTLE FOR i WHILE

liczby = [1,2,3,4,5]

for i in liczby:
    print(liczby)

for i in range(10):
    print(i)

for i2 in range(15,18):
    print(i2)

licznik = 0

while licznik < 5:
    print(licznik)
    licznik +=1

licznik2 = 0

while True:
    print(licznik2)
    licznik2 += 1
    if licznik2 >=8:
        break

for x in range(20):
    if x % 2 ==0:
        continue
    print(x)