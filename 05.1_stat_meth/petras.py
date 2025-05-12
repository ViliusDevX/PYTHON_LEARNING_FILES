class Person:
    population = []

    def __init__(self, name):
        self.name = name
        Person.population += 1

    @staticmethod
    def get_population():
        return Person.population

    def get_name(self):
        return self.name


petras = Person("Petras")

print(Person.get_population())
print(petras.get_name())
