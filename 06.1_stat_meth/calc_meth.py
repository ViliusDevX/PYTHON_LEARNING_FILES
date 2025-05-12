class Calculator:
    @staticmethod
    def add(x, y):
        sum = x + y
        return sum

    @staticmethod
    def subtract(x, y):
        sum = x - y
        return sum

    @staticmethod
    def multiply(x, y):
        sum = x * y
        return sum

    @staticmethod
    def divide(x, y):
        sum = x / y
        return sum


print(Calculator.add(1, 3))
