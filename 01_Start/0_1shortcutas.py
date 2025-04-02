import math
street_1 = 100
street_2 = 200

street_1_sqr = math.pow(street_1, 2)
street_2_sqr = math.pow(street_2, 2)

around = street_2 + street_1
shortcut = math.sqrt(around)

distance_difference = around - shortcut

print(f"Begti aplink: {round(around)} \nBegti shortcuta: {round(shortcut)} \nShortcutas trumpesnis: {round(distance_difference)}")