import random

sunny = bool(round(random.random()))
rainy = bool(round(random.random()))

sun_is_shining = sunny and not rainy
rainbow = sunny and rainy
cloudy = not sunny and not rainy
cloudy_and_raining = not sunny and rainy

if sun_is_shining:
    print("sauleta")
elif rainbow:
    print("vaivorykste")
elif cloudy:
    print("debesuota")
else:
    print("debesuota + lietus")
