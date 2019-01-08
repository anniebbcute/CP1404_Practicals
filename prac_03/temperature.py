"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

def CelsiusToFahrenheit(cel):
    fah = cel * 9.0 / 5 + 32
    return fah

def FahrenheitToCelsius(fah):
    cel = 5 / 9 * (fah - 32)
    return cel

def menu():
    MENU = """C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    return choice


option = menu()
while option!= "Q":
    if option == "C":
        celsius = float(input("Celsius: "))
        print("Result: {:.2f} F".format(CelsiusToFahrenheit(celsius)))
    elif option == "F":
        fahrenheit = float(input("Fahrenheit: "))
        print("Result: {:.2f} C".format(FahrenheitToCelsius(fahrenheit)))
    else:
        print("Invalid option")
    option = menu()
print("Thank you.")