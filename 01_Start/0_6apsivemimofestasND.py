import math


def calculate_bottles(girls, boys, days):
    one_vodka_bottle_capacity = 0.7
    each_girl_needs_vodka = 0.5
    each_boy_needs_vodka = 0.7
    total_vodka_needed = (((girls * each_girl_needs_vodka) + (boys * each_boy_needs_vodka) * days) / one_vodka_bottle_capacity)
    return math.ceil(total_vodka_needed)


girls_total = int(input("Iš viso bus panų:"))
boys_total = int(input("Iš viso bus bahurų:"))
days_total = int(input("Iš viso gersit dienų:"))


total_vodka = calculate_bottles(girls_total, boys_total, days_total)
print(f"Reikes is viso: {total_vodka} degtines ")
