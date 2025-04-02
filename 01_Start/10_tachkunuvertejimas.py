cars = {
    "starting_price": 30000,
    "months": 24,
    "inflation": 2
}

total_months = 0
how_much_money = int(input("Ivesk kiek turi euru: "))
residual_price = cars["starting_price"]

while residual_price > how_much_money:
    residual_price -= residual_price / 100 * cars["inflation"]
    total_months += 1

print(f"Masina galesi nupirkti po: {total_months} menesiu, kai ji kainuos {residual_price}")
print(f"Kainavo {cars['starting_price']}")
print(f"Kainuoja: {residual_price}")

