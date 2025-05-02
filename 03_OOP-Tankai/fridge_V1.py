import datetime


class Fridge:
    def __init__(self, max_products_capacity, name, date_until_edible):
        self.old_products = []
        self.name = name
        self.date_until_edible = datetime.datetime.strptime(date_until_edible, "%Y-%m-%d").date()
        self.products = []
        self.max_products_capacity = max_products_capacity

    def is_edible(self):
        current_date = datetime.datetime.now().date()
        if current_date > self.date_until_edible:
            self.old_products.append(self.name)
        return current_date <= self.date_until_edible

    def add_products(self, product):
        self.product = product
        if self.products < self.max_products_capacity:
            self.products.append(self.product)
        else:
            print("Pilnas fridge'as")

    def get_old_products(self):
        return self.old_products

    def count_products(self):
        return len(self.products)


fridge = Fridge(10, "Baranka", "2024-6-2")
