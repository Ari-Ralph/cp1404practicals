"""
CP1404 - Practical 03
Answer the following questions:
1. When will a ValueError occur?
A Value Error will occur when the input is not an integer.
2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur when the denominator input is 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
To avoid the possibility of a ZeroDivisionError, a while loop could be added to ensure the denominator is
not equal to 0.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
