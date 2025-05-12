class Employee:
    def __init__(self, name, age, salary):
        self._name = None
        self._age = None
        self._salary = None
        self.name = name
        self.age = age
        self.salary = salary

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def salary(self):
        return self._salary

    @name.setter
    def name(self, name1):
        if isinstance(name1, str) and len(name1.split()) == 2:
            capitalized_name = ' '.join(word.capitalize() for word in name1.split())
            self._name = capitalized_name
        else:
            raise ValueError("Name should be a string with two words")

    @age.setter
    def age(self, age1):
        if isinstance(age1, int) and 18 < age1 < 65:
            self._age = age1
        else:
            raise ValueError("Age should be an integer between 18 and 65")

    @salary.setter
    def salary(self, salary1):
        if isinstance(salary1, int) and salary1 > 0:
            self._salary = salary1
        else:
            raise ValueError("Salary should be a positive integer")


employee = Employee("Bob Jones", 21, 1000)
print(employee.name, employee.age, employee.salary)
