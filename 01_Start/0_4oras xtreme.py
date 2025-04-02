temp = 25
wind = 5
time = 13
sky_thunder = False
sky_rain = False

great_temp = 20 < temp < 28
great_wind = 3 < wind < 6
great_time = 9 < time < 19
great_thunder_weather = not sky_thunder
great_rain_weather = not sky_rain
great_weather = great_rain_weather and great_time and great_wind and great_temp and great_thunder_weather

good_temp = 20 < temp < 28
good_wind = wind < 1
good_time = 19 < time < 22
good_thunder_weather = not sky_thunder
good_rain_weather = not sky_rain
good_weather = good_temp and good_wind and good_time and good_thunder_weather and good_rain_weather

bad_temp = (temp > 28) or (temp < 20)
bad_wind = wind > 10
bad_sky_weather = sky_rain or sky_thunder or (22 < time < 9)
bad_weather = bad_sky_weather and bad_wind and bad_temp

if great_weather:
    print("Great time for surfing")
elif good_weather:
    print("Great time to go for a date")
elif bad_weather:
    print("Great time to stay home")
else:
    print("No suggestions")
