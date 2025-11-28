print("Jeśli chcesz dodać liczby wpisz -> 1")
print("Odjąc -> 2")
print("Pomnożyć -> 3")
print("Podzielić -> 4")

type_of_mathematical_operation = float(input())

num1 = float(input("Podaj pierwszą liczbę: "))

num2 = float(input("Podaj drugą liczbę: "))

if type_of_mathematical_operation == 1:
    print ("Wynik to:", num1 + num2)