print("Jeśli chcesz dodać liczby wpisz -> 1")
print("Odjąc -> 2")
print("Pomnożyć -> 3")
print("Podzielić -> 4")

type_of_mathematical_operation = float(input())
num1 = float(input("Podaj pierwszą liczbę: "))
num2 = float(input("Podaj drugą liczbę: "))
con_tinue = "TAK"

def addition(num1, num2, sum):
    sum = num1 + num2
    return sum

def subtraction(num1, num2, sum):
    sum = num1 - num2
    return sum

def multiplication(num1, num2, sum):
    sum = num1 * num2
    return sum

def division(num1, num2, sum):
    sum = num1 / num2
    return sum

while con_tinue == "TAK":
    if type_of_mathematical_operation == 1:
        print ("Wynik to:", addition(num1, num2, sum))
        break
    elif type_of_mathematical_operation == 2:
        print ("Wynik to:", subtraction(num1, num2, sum))
        break
    elif type_of_mathematical_operation == 3:
        print ("Wynik to:", multiplication(num1, num2, sum))
        break
    elif type_of_mathematical_operation == 4:
        print ("Wynik to:", division(num1, num2, sum))
        break


