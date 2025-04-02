def ask_user_letter(user_pressed_a, user_pressed_b, user_pressed_c):
    enter_letter = str(input("Pasirink raide a, b ar c:"))
    a_pressed = enter_letter == 'a'
    b_pressed = enter_letter == 'b'
    c_pressed = enter_letter == 'c'
    all_letters_pressed = a_pressed and b_pressed and c_pressed
    user_pressed_all_letter = user_pressed_c and user_pressed_b and user_pressed_a

    if all_letters_pressed:
        user_pressed_all_letter = True
    else:
        ask_user_letter(user_pressed_a, user_pressed_b, user_pressed_c)


ask_user_letter(False, False, False)