def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divine(x, y):
    return x / y


print("Wybierz operację:")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnożenie")
print("4.Dzielenie")

while True:
    choice = input("Wybierz operację(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))
        if choice == '1':
            print('Twój wynikt to: ', add(num1, num2))
            break
        elif choice == '2':
            print('Twój wynikt to: ', subtract(num1, num2))
            break
        elif choice == '3':
            print('Twój wynikt to: ', multiply(num1, num2))
            break
        elif choice == '4':
            print('Twój wynikt to: ', divine(num1, num2))
            break

    else:
        print("Błędna wartość, podaj poprawną")