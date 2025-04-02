def ask_for_beer(beer_count):
    beer = int(input("Kiek nori alaus?:"))
    beer_count += beer
    still_want_beer = str(input("Ar vis dar nori alaus?:"))
    if still_want_beer == 'n':
        return beer_count
    else:
        ask_for_beer(beer_count)


total_beer = ask_for_beer(0)
print(total_beer)

