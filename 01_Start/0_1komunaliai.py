import math

user1_shots = 3
user2_shots = 15
user3_shots = 7
total_shots = user3_shots + user2_shots + user1_shots

shot_capacity = 50
vodka_bottle_price = 10.49
vodka_bottle_capacity = 500
total_shots_capacity = shot_capacity * total_shots
vodka_bottles_bought = math.ceil(total_shots_capacity / vodka_bottle_capacity)
total_vodka_bottles_capacity = vodka_bottle_capacity * vodka_bottles_bought

capacity_left = total_vodka_bottles_capacity - total_shots_capacity

total_vodka_bottles_price = vodka_bottle_price * vodka_bottles_bought
all_of_them_paid = (total_vodka_bottles_price / 3)

print(f"is viso pirkta buteliu: {vodka_bottles_bought} "
      f"\nisgerta shot'u: {total_shots} \nisgerta skyscio: {total_shots_capacity} "
      f"\nskysio likutis: {capacity_left} \nsumoketa viso : {total_vodka_bottles_price} \n"
      f"sumoketa kiekvienos: {all_of_them_paid}")


