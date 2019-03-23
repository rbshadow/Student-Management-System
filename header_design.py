vertical_char = "│"
horizontal_char = "─"
Top_left = "┌"
Top_right = "┐"
Bottom_left = "└"
Bottom_right = "┘"


def margin(character_sign, total_times):
    margin_character = ""
    for i in range(total_times):
        margin_character = margin_character + character_sign
    return margin_character


def draw_menu(menus):
    main_menu = menus
    maximum_text_length = len(main_menu) + 20

    maximum_text_size = maximum_text_length
    y = maximum_text_length

    top_margin_left_to_right = Top_left + margin(horizontal_char, y) + Top_right
    print(" " * 20 + top_margin_left_to_right)

    free_space = maximum_text_size - len(main_menu) - 10
    right_vertical_wall = margin(" ", free_space) + vertical_char
    print(" " * 20 + vertical_char + " " * 10 + main_menu + right_vertical_wall)

    lower_margin_left_to_right = Bottom_left + margin(horizontal_char, y) + Bottom_right
    print(" " * 20 + lower_margin_left_to_right)


def art(var):
    var = var
    draw_menu(menus=var)


if __name__ == '__main__':
    art('Test')
