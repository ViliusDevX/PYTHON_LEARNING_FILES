def ask_hero_name():
    return input("Ivesk herojaus varda: ")


def ask_place():
    return input("Ivesk veiksmo vieta: ")


def ask_villain_name():
    return input("Ivesk blogo veikejo varda: ")


def ask_if_good_ending():
    good_ending_question = str(input("Ar viskas baigesi gerai? atsakymas taip arba ne: "))
    return good_ending_question == "taip"


def create_story(character, place, villain, good_ending):
    character_introduction = f"Gyveno karta {character} ir niekam netrugde. "
    place_introduction = f"Visas veiksmas ivyko {place}. "
    villain_introduction = f"{villain} norejo duoti malku {character} ir pavogti jo pinigus. "

    if good_ending:
        story_ending = "Viskas baigesi pukiai"
    else:
        story_ending = "Viskas baigesi blogai"

    total_story = character_introduction + place_introduction + villain_introduction + story_ending
    return total_story


hero = ask_hero_name()
place = ask_place()
villain = ask_villain_name()
good_ending = ask_if_good_ending()


story = create_story(hero, place, villain, good_ending)
print(story)
