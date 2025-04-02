battery_capacity_watthours = 300
battery_charge_capacity_current = battery_capacity_watthours / 100 * 80
fridge_power = 45
want_to_use_fridge_hours = 7

possible_use_time_maximum = round(battery_capacity_watthours / fridge_power)
possible_use_time_current = round(battery_charge_capacity_current / fridge_power)
battery_will_last_current_charge = bool(possible_use_time_current >= want_to_use_fridge_hours)
battery_will_last_maximum_charge = bool(possible_use_time_maximum >= want_to_use_fridge_hours)

print(f"baterijos talpa: {battery_capacity_watthours} \npakrovimo talpa: {battery_charge_capacity_current} \nsaldytuvo galia: {fridge_power} "
      f"\nnori laikyti ijungta saldytuva: {want_to_use_fridge_hours} \ngalimas naudojimo laikas: {possible_use_time_current} "
      f"\nbaterijos uzteks su dabartiniu ikrovimu: {battery_will_last_current_charge} \nbaterijos uzteks su pilnu ikrovimu: {battery_will_last_maximum_charge}")
