import yaml


class Car:
    def __init__(self, mark):
        self.mark = mark


vehicle = Car("tayota")


dict = {"name" : "Jonas",
        "age": 20,
        "items": ["food", "drugs", "guns", vehicle]}


with open('output.yaml', 'w') as file:
    yaml.dump(dict, file)

with open('output.yaml', 'r') as file:
    data = yaml.safe_load(file)

print(data)
