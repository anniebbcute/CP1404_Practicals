"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When a number with a decimal is entered.
2. When will a ZeroDivisionError occur? When 0 is entered as a denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = 0
    while denominator == 0:
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")