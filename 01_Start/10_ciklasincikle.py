mfs = [
    {
        "name": "Trod Urod",
        "items": ["jarate", "vodka"]
    },
    {
        "name": "Eric Queef",
        "items": ["nomeda", "tupla"]
    }
]
fuck_input = input("Ivesk ka nori prideti: ")

for mf in mfs:
    mf["items"].append(fuck_input)


print(mfs)