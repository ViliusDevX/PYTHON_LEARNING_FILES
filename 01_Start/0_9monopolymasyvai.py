
COLOR_BLUE = "blue"
COLOR_ORANGE = "orange"
COLOR_BROWN = "brown"
TYPE_TRAIN = "train"
TYPE_PROPERTY = "property"

cards = {
    "MFBL1": {
        "color": COLOR_BLUE,
        "type": TYPE_PROPERTY,
        "name": "Myfair",
        "houses": 1
    },
    "PLBL2": {
        "color": COLOR_BLUE,
        "type": TYPE_PROPERTY,
        "name": "Park Lane",
        "houses": 2
    },
    "TRKCS": {
        "type": TYPE_TRAIN,
        "name": "King Cross Station",
    },
    "TRMS": {
        "type": TYPE_TRAIN,
        "name": "Marleybone Station",
    },
    "TRCCS": {
        "type": TYPE_TRAIN,
        "name": "Charring Cross Station",
    },
    "OKRBR1": {
        "color": COLOR_BROWN,
        "type": TYPE_PROPERTY,
        "name": "Old Kent Road",
        "houses": 1
    },
    "WCRBR1": {
        "color": COLOR_BROWN,
        "type": TYPE_PROPERTY,
        "name": "White Chapel Road",
        "houses": 1
    },
    "VSOR": {
        "color": COLOR_ORANGE,
        "type": TYPE_PROPERTY,
        "name": "Vine Street",
    }
}

game = {
    "moves" : 15,
    "players" : [
        {
            "name": "Tomas Gandonas",
            "money": 150,
            "cards": ["MFBL1", "PLBL2", "TRKCS", "TRMS"]

        },
        {
            "name": "Jonas Buljonas",
            "money": 500,
            "cards": ["TRCCS", "OKRBR1", "WCRBR1", "VSOR"]
        }]
}

card_index = "TRKCS"
print(cards[card_index]["name"])
if cards[card_index]["type"] == TYPE_PROPERTY:
    print("this is prop")
else:
    print("this is train")


def create_card(id, name, type, color=None):
    color_list = [COLOR_BLUE, COLOR_ORANGE, COLOR_BROWN]
    if (type == TYPE_PROPERTY) and (color not in color_list):
        raise Exception("Nera tokios spalvos")
    if type == TYPE_TRAIN:
        card = {"name": name, "type": type}
    elif type == TYPE_PROPERTY:
        card = {"color": color, "name": name, "type": type}
    else:
        raise Exception("Nurodytas blogas type'as")
    cards[id] = card


create_card("BYBYS1", "kiausinai", TYPE_PROPERTY, COLOR_BLUE)
exit()


def build_house(id):

    if "houses" in cards[id]:
        cards[id]["houses"] += 1

    elif cards[id]["type"] == TYPE_TRAIN:
        raise Exception("Negali statyti namus ant traukiniu")


def build_hotel(id):
    if "houses" in cards[id]:
        cards[id].pop("houses")
        cards[id]["hotel"] = 1
    elif cards[id]["type"] == TYPE_TRAIN:
        raise Exception("Negali statyti viešbutį ant traukiniu")

