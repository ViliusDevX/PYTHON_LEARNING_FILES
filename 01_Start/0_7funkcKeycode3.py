def ask_user_letter(user_pressed_a, user_pressed_b, user_pressed_c):
    enter_letter = str(input("Pasirink raide a, b ar c:"))

    a_pressed = enter_letter == 'a'
    b_pressed = enter_letter == 'b'
    c_pressed = enter_letter == 'c'

    if a_pressed:
        user_pressed_a = True
    if b_pressed:
        user_pressed_b = True
    if c_pressed:
        user_pressed_c = True

    user_pressed_all_letter = user_pressed_c and user_pressed_b and user_pressed_a

    if not user_pressed_all_letter:
        ask_user_letter(user_pressed_a, user_pressed_b, user_pressed_c)


ask_user_letter(False, False, False)
