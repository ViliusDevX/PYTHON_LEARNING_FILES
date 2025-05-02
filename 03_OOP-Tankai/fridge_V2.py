import datetime


class Product:
    def __init__(self, name, date_until_edible):
        self.name = name
        self.date_until_edible = datetime.datetime.strptime(date_until_edible, "%Y-%m-%d").date()

    def is_edible(self):
        current_date = datetime.datetime.now().date()
        return current_date <= self.date_until_edible


class Fridge:
    def __init__(self, max_products_capacity):
        self.products = []
        self.max_products_capacity = max_products_capacity
        self.current_date = datetime.datetime.now().date()

    def add_product(self, product):
        if len(self.products) < self.max_products_capacity:
            self.products.append(product)
        else:
            print("Pilnas fridge'as")

    def get_old_products(self):
        out_of_date_products = []
        for product in self.products:
            if not product.is_edible():
                out_of_date_products.append(product)
        return out_of_date_products

    def count_products(self):
        return len(self.products)


fridge = Fridge(10)
bread = Product("duona", "2000-11-5")
fridge.add_product(bread)
meat = Product("mesa", "2025-05-07")
fridge.add_product(meat)
chips = Product("cipsai", "2003-05-07")
fridge.add_product(chips)
drink = Product("gerimas", "2025-09-02")
fridge.add_product(drink)
old_product = fridge.get_old_products()
print(old_product)
