import datetime


class Products:
    def __init__(self, name, date_until_edible):
        self.name = name
        self.date_until_edible = datetime.datetime.strptime(date_until_edible, "%Y-%m-%d").date()

    def is_edible(self):
        current_date = datetime.datetime.now().date()
        return current_date <= self.date_until_edible

        
product1 = Products("Pienas", "2023-11-26")
product2 = Products("Baton", "2022-4-9")

print(product1.is_edible())
print(product2.is_edible())
