import math

sewers_total = 10
house_floor_total = 10

leakage_tempo_per_minute = sewers_total * 5
leakage_tempo_per_second = leakage_tempo_per_minute / 60
leakage_pressure = 1 * house_floor_total

pipe_diameter_meters = math.sqrt(leakage_pressure * leakage_tempo_per_second)
pipe_diameter_centimeters = pipe_diameter_meters * 100
print(f"Vamzdzio storis: {round(pipe_diameter_centimeters)} centimetrai")