class Pension:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    def get_age(self):
        age = 2023 - self.birth_date
        return age

    def get_years_until_pension(self):
        years_until_pension = 65 - self.get_age()
        if years_until_pension < 65:
            return years_until_pension


when_is_my_pension = Pension("Vilius", 2008)
print(f"Iki pensijos: {when_is_my_pension.get_years_until_pension()}")
