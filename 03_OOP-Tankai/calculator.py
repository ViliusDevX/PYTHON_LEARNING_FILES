class Calculation:
    def __init__(self):
        self.history = []

    def add(self, x, y):
        answer  =x + y
        self.history.append(answer)
        return answer

    def substract(self, x, y):
        answer = x - y
        self.history.append(answer)
        return answer

    def divide(self, x, y):
        answer = x / y
        self.history.append(answer)
        return answer

    def multiply(self, x, y):
        answer = x * y
        self.history.append(answer)
        return answer

    def get_history(self):
        return self.history


calc = Calculation()
print(calc.divide(10,2), calc.add(123, 23456))
print(calc.get_history())

calc1 = Calculation()
print(calc1.divide(55,42), calc1.add(23, 236))
print(calc1.get_history())


