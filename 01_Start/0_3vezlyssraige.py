turtle_speed = 134
snail_speed = 96

turtle_will_win = turtle_speed > snail_speed
snail_will_win = snail_speed > turtle_speed
marathon_draw = turtle_speed == snail_speed

print(f"vezlio greitis: {turtle_speed}  laimes: {turtle_will_win} "
      f"\nsraiges greitis: {snail_speed}  laimes: {snail_will_win} \nbus lygiosios: {marathon_draw}")