import random

aleksandra_drank_wine = bool(round(random.random()))
icy_roads_outside = bool(round(random.random()))

aleksandra_will_fall_down = aleksandra_drank_wine or icy_roads_outside

print(f"lauke plikledis: {icy_roads_outside} \naleksandra girta: {aleksandra_will_fall_down} \naleksandra nukrito: {aleksandra_will_fall_down}")