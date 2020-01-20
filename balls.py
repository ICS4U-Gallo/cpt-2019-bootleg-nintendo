import arcade

width = 768
height = 640


def binary_search(target, numbers):
    start = 0
    end = len(numbers) - 1

    while end >= start:
        mid = (start + end) // 2

        if numbers[mid].name[:1] == target:
            return mid
        elif numbers[mid].name[:1] > target:
            end = mid - 1
        elif numbers[mid].name[:1] < target:
            start = mid + 1

    return -1


def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers

    left_side = merge_sort(numbers[:len(numbers)//2])
    right_side = merge_sort(numbers[len(numbers)//2:])

    left_marker, right_marker = 0, 0

    new_list = []

    while left_marker < len(left_side) and right_marker < len(right_side):
        if left_side[left_marker].amount < right_side[right_marker].amount:
            new_list.append(left_side[left_marker])
            left_marker += 1
        else:
            new_list.append(right_side[right_marker])
            right_marker += 1

    while right_marker < len(right_side):
        new_list.append(right_side[right_marker])
        right_marker += 1

    while left_marker < len(left_side):
        new_list.append(left_side[left_marker])
        left_marker += 1

    return new_list


def on_draw(player):
    arcade.start_render()
    arcade.set_background_color(arcade.color.WHITE)
    arcade.draw_text("Balls", 20, 570, arcade.color.BLACK, 50)
    arcade.draw_text("Balls Known:", 20, 520, arcade.color.BLACK, 30)
    arcade.draw_text(str(len(player.ball_list)), 250, 520,
                     arcade.color.BLACK, 30)
    arcade.draw_text("Q - Sort", 30, 30, arcade.color.BLACK, 60)
    arcade.draw_text("E - Search", 370, 30, arcade.color.BLACK, 60)

    arcade.draw_xywh_rectangle_outline(10, 405, 450, 70,
                                       arcade.color.GRAY, 3)
    arcade.draw_xywh_rectangle_outline(5, 290, 460, 90,
                                       arcade.color.BLACK, 5)
    arcade.draw_xywh_rectangle_outline(10, 193, 450, 70,
                                       arcade.color.GRAY, 3)

    if player.get_pointer() - 1 != -1:
        arcade.draw_text("{}: {}".format(player.ball_list
                         [player.get_pointer() - 1].name,
                         player.ball_list
                         [player.get_pointer() - 1].effect), 20,
                         425, arcade.color.BLACK, 20)

    arcade.draw_text("{}: {}".format(player.ball_list
                     [player.get_pointer()].name,
                     player.ball_list
                     [player.get_pointer()].effect), 20,
                     320, arcade.color.BLACK, 30)

    if player.get_pointer() + 1 != len(player.ball_list):
        arcade.draw_text("{}: {}".format(player.ball_list
                         [player.get_pointer() + 1].name,
                         player.ball_list
                         [player.get_pointer() + 1].effect), 20,
                         213, arcade.color.BLACK, 20)

    arcade.draw_triangle_filled(475, 335, 495, 315, 495,
                                355, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_outline(500, 210, 250, 250,
                                       arcade.color.BLACK, 10)
    arcade.draw_texture_rectangle(625, 335, 240, 240, player.ball_list
                                  [player.get_pointer()].texture)
    arcade.draw_text("Amount: {}".format(str(player.ball_list
                                             [player.get_pointer()].amount)),
                     465, 150, arcade.color.BLACK, 50)

    if player.search_menu:
        arcade.draw_xywh_rectangle_filled(100, 100, 568, 440,
                                          arcade.color.BLACK)
        arcade.draw_xywh_rectangle_filled(110, 110, 548, 420,
                                          arcade.color.WHITE)
        arcade.draw_text("Enter Item First Letter:", 140, 450,
                         arcade.color.BLACK, 35)
        arcade.draw_text(" " + player.search_letter, 140, 200,
                         arcade.color.BLACK, 220)
    if player.sort_menu:
        arcade.draw_xywh_rectangle_filled(100, 100, 568, 440,
                                          arcade.color.BLACK)
        arcade.draw_xywh_rectangle_filled(110, 110, 548, 420,
                                          arcade.color.WHITE)
        arcade.draw_text("Do you want to sort", 175, 380,
                         arcade.color.BLACK, 40)
        arcade.draw_text("the balls by least amount?", 130,
                         310, arcade.color.BLACK, 40)


def search_logic(player, key):
    if key == arcade.key.E or player.search_menu:
        player.search_menu = True
        player.sort_menu = False

    if key == arcade.key.W:
        if player.get_pointer() != 0:
            player.edit_pointer(player.get_pointer() - 1)
    elif key == arcade.key.S:
        if player.get_pointer() != len(player.ball_list) - 1:
            player.edit_pointer(player.get_pointer() + 1)

    if player.search_menu is True:
        if key == arcade.key.A:
            if len(player.search_letter) < 1:
                player.search_letter += "a"
        elif key == arcade.key.B:
            if len(player.search_letter) < 1:
                player.search_letter += "b"
        elif key == arcade.key.C:
            if len(player.search_letter) < 1:
                player.search_letter += "c"
        elif key == arcade.key.D:
            if len(player.search_letter) < 1:
                player.search_letter += "d"
        elif key == arcade.key.E:
            if len(player.search_letter) < 1:
                player.search_letter += "e"
        elif key == arcade.key.F:
            if len(player.search_letter) < 1:
                player.search_letter += "f"
        elif key == arcade.key.G:
            if len(player.search_letter) < 1:
                player.search_letter += "g"
        elif key == arcade.key.H:
            if len(player.search_letter) < 1:
                player.search_letter += "h"
        elif key == arcade.key.I:
            if len(player.search_letter) < 1:
                player.search_letter += "i"
        elif key == arcade.key.J:
            if len(player.search_letter) < 1:
                player.search_letter += "j"
        elif key == arcade.key.K:
            if len(player.search_letter) < 1:
                player.search_letter += "k"
        elif key == arcade.key.L:
            if len(player.search_letter) < 1:
                player.search_letter += "l"
        elif key == arcade.key.M:
            if len(player.search_letter) < 1:
                player.search_letter += "m"
        elif key == arcade.key.N:
            if len(player.search_letter) < 1:
                player.search_letter += "n"
        elif key == arcade.key.O:
            if len(player.search_letter) < 1:
                player.search_letter += "o"
        elif key == arcade.key.P:
            if len(player.search_letter) < 1:
                player.search_letter += "p"
        elif key == arcade.key.Q:
            if len(player.search_letter) < 1:
                player.search_letter += "q"
        elif key == arcade.key.R:
            if len(player.search_letter) < 1:
                player.search_letter += "r"
        elif key == arcade.key.S:
            if len(player.search_letter) < 1:
                player.search_letter += "s"
        elif key == arcade.key.T:
            if len(player.search_letter) < 1:
                player.search_letter += "t"
        elif key == arcade.key.U:
            if len(player.search_letter) < 1:
                player.search_letter += "u"
        elif key == arcade.key.V:
            if len(player.search_letter) < 1:
                player.search_letter += "v"
        elif key == arcade.key.W:
            if len(player.search_letter) < 1:
                player.search_letter += "w"
        elif key == arcade.key.X:
            if len(player.search_letter) < 1:
                player.search_letter += "x"
        elif key == arcade.key.Y:
            if len(player.search_letter) < 1:
                player.search_letter += "y"
        elif key == arcade.key.Z:
            if len(player.search_letter) < 1:
                player.search_letter += "z"
        elif key == arcade.key.BACKSPACE:
            player.search_letter = player.search_letter[:-1]

        if key == arcade.key.L and player.search_letter != "":
            found = binary_search(player.search_letter, player.ball_list)

            if found != -1:
                player.edit_pointer(found)
            player.search_menu = False
            player.search_letter = ""

        elif key == arcade.key.K:
            player.search_menu = False
            player.search_letter = ""

    if key == arcade.key.Q or player.sort_menu:
        player.sort_menu = True
        player.search_menu = False
        if key == arcade.key.L:
            player.ball_list = merge_sort(player.ball_list)
            player.sort_menu = False
        elif key == arcade.key.K:
            player.sort_menu = False

    if key == arcade.key.K:
        player.cur_screen = "bag"


def main():
    game = MyGame(width, height, "balls")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
