from math import gcd
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):

        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):

        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):

        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):

        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)


def main():
    num1 = int(input("Enter the numerator of the first fraction: "))
    den1 = int(input("Enter the denominator of the first fraction: "))
    fraction1 = Fraction(num1, den1)

    num2 = int(input("Enter the numerator of the second fraction: "))
    den2 = int(input("Enter the denominator of the second fraction: "))
    fraction2 = Fraction(num2, den2)

    print("\nChoose an operation:")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5.fraction reduction")

    choice = int(input("Enter your choice (1-4): "))


    if choice == 1:
        result = fraction1 + fraction2
        print(f"Result: {fraction1} + {fraction2} = {result}")
    elif choice == 2:
        result = fraction1 - fraction2
        print(f"Result: {fraction1} - {fraction2} = {result}")
    elif choice == 3:
        result = fraction1 * fraction2
        print(f"Result: {fraction1} * {fraction2} = {result}")
    elif choice == 4:
        result = fraction1 / fraction2
        print(f"Result: {fraction1} / {fraction2} = {result}")
    elif choice == 5:
        simplified = fraction1.simplify()
        print(f"Simplified Fraction: {simplified}")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
