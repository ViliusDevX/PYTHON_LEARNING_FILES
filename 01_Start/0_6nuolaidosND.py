def apply_discount(price, discount):
    return price - (price / 100 * discount)  # Pagal formule: kaina - (kaina / 100 * nuolaida)


potatoes_juice_final_price = apply_discount(5.99, 12)  # 5.99 - (5.99 / 100 * 12) = 5.27
screwdriver_final_price = apply_discount(8.99, 25)  # 8.99 - (8.99 / 100 * 25) = 6.74


print(f"Bulviu sultims 12% akcija: {potatoes_juice_final_price} Euru (buvo 5.99 Eur)")
print(f"Atsuktuvams akcija 25%: {screwdriver_final_price} Euru(buvo 8.99 Eur)")

