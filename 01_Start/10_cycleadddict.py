mfs = [
    {
        "name": "Trod Urod",
        "items": {
            "jarate": {
                    "name": "Bottle of piss",
                    "qty": 4
        },
            "vodka": {
                "name": "Stumbras",
                "qty": 1
            }
        }
    },
    {
        "name": "Eric Queef",
        "items": {
            "nomeda": {
                "name": "Neskanus sokoladukas",
                        "qty": 1
        },
            "tupla": {
                "name": "Snickers ripoff",
                "qty": 1
        }
    }
}
]

id_input = input("Ivesk objekto ID: ")
name_input = input("Ivesk objekto Name: ")
qty_input = input("Ivesk objekto kieki: ")

for mf in mfs:
    mf["items"][id_input] = {
        "name": name_input,
        "qty": qty_input
    }
    print(mf)
