class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


if __name__ == "__main__":
    calc = Calculator()
    print("2 + 2 =", calc.add(2, 2))
    print("2 - 2  =", calc.subtract(2, 2))
    print("2 * 2 =", calc.multiply(2, 2))
    print("2 / 2 =", calc.divide(2, 2))
