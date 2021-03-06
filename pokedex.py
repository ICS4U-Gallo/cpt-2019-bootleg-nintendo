import arcade

width = 768
height = 600

# poke_list = ["TORKOAL", "GARBAGE", "PIKACHU", "EEVEE", "GARCHOMP", "
# VESPIQUEN", "COMBEE", "RAYQUAZA"]


def binary_search(target, numbers):
    start = 0
    end = len(numbers) - 1

    while end >= start:
        mid = (start + end) // 2

        if numbers[mid].num == target:
            return mid
        elif numbers[mid].num > target:
            end = mid - 1
        elif numbers[mid].num < target:
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
        if left_side[left_marker].num < right_side[right_marker].num:
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
    arcade.draw_text("Pokedex", 20, 570, arcade.color.BLACK, 50)
    arcade.draw_text("Total Caught:", 20, 520, arcade.color.BLACK, 30)
    arcade.draw_text(str(len(player.poke_list)), 250, 520,
                     arcade.color.BLACK, 30)
    arcade.draw_text("Q - Sort", 30, 30, arcade.color.BLACK, 60)
    arcade.draw_text("E - Search", 370, 30, arcade.color.BLACK, 60)

    arcade.draw_xywh_rectangle_filled(0, 173, 768, 320, arcade.color.WHITE)
    arcade.draw_xywh_rectangle_outline(10, 405, 450, 70,
                                       arcade.color.GRAY, 3)
    arcade.draw_xywh_rectangle_outline(5, 290, 460, 90,
                                       arcade.color.BLACK, 5)
    arcade.draw_xywh_rectangle_outline(10, 193, 450, 70,
                                       arcade.color.GRAY, 3)

    if player.get_pointer() - 1 != -1:
        arcade.draw_text("{}: {}".format(player.poke_list
                         [player.get_pointer() - 1].num,
                         player.poke_list[player.get_pointer() - 1].name), 20,
                         425, arcade.color.BLACK, 20)

    arcade.draw_text("{}: {}".format(player.poke_list
                     [player.get_pointer()].num,
                     player.poke_list[player.get_pointer()].name), 20,
                     320, arcade.color.BLACK, 30)

    if player.get_pointer() + 1 != len(player.poke_list):
        arcade.draw_text("{}: {}".format(player.poke_list
                         [player.get_pointer() + 1].num,
                         player.poke_list[player.get_pointer() + 1].name), 20,
                         213, arcade.color.BLACK, 20)

    arcade.draw_triangle_filled(475, 335, 495, 315, 495,
                                355, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_outline(500, 210, 250, 250,
                                       arcade.color.BLACK, 10)
    arcade.draw_texture_rectangle(625, 335, 240, 240, player.poke_list
                                  [player.get_pointer()].texture)

    if player.search_menu:
        arcade.draw_xywh_rectangle_filled(100, 100, 568, 440,
                                          arcade.color.BLACK)
        arcade.draw_xywh_rectangle_filled(110, 110, 548, 420,
                                          arcade.color.WHITE)
        arcade.draw_text("Enter Pokemon Number:", 140, 450,
                         arcade.color.BLACK, 35)
        arcade.draw_text(" " + player.search_number, 140, 200,
                         arcade.color.BLACK, 220)
    if player.sort_menu:
        arcade.draw_xywh_rectangle_filled(100, 100, 568, 440,
                                          arcade.color.BLACK)
        arcade.draw_xywh_rectangle_filled(110, 110, 548, 420,
                                          arcade.color.WHITE)
        arcade.draw_text("Do you want to sort", 115, 380,
                         arcade.color.BLACK, 50)
        arcade.draw_text("the Pokedex?", 175, 310, arcade.color.BLACK, 50)


def key_logic(player, key):
    if key == arcade.key.W:
        if player.get_pointer() != 0:
            player.edit_pointer(player.get_pointer() - 1)
    elif key == arcade.key.S:
        if player.get_pointer() != len(player.poke_list) - 1:
            player.edit_pointer(player.get_pointer() + 1)
    elif (key == arcade.key.K and not
          player.sort_menu and not player.search_menu):
        player.cur_screen = "game menu"
    if key == arcade.key.E or player.search_menu:
        player.search_menu = True
        player.sort_menu = False

        if key == arcade.key.KEY_0:
            if len(player.search_number) < 2:
                player.search_number += "0"
        elif key == arcade.key.KEY_1:
            if len(player.search_number) < 2:
                player.search_number += "1"
        elif key == arcade.key.KEY_2:
            if len(player.search_number) < 2:
                player.search_number += "2"
        elif key == arcade.key.KEY_3:
            if len(player.search_number) < 2:
                player.search_number += "3"
        elif key == arcade.key.KEY_4:
            if len(player.search_number) < 2:
                player.search_number += "4"
        elif key == arcade.key.KEY_5:
            if len(player.search_number) < 2:
                player.search_number += "5"
        elif key == arcade.key.KEY_6:
            if len(player.search_number) < 2:
                player.search_number += "6"
        elif key == arcade.key.KEY_7:
            if len(player.search_number) < 2:
                player.search_number += "7"
        elif key == arcade.key.KEY_8:
            if len(player.search_number) < 2:
                player.search_number += "8"
        elif key == arcade.key.KEY_9:
            if len(player.search_number) < 2:
                player.search_number += "9"
        elif key == arcade.key.BACKSPACE:
            player.search_number = player.search_number[:-1]

        if key == arcade.key.L and player.search_number != "":
            found = binary_search(int(player.search_number), player.poke_list)

            if found != -1:
                player.edit_pointer(found)
            player.search_menu = False
            player.search_number = ""

        elif key == arcade.key.K:
            player.search_menu = False
            player.search_number = ""

    if key == arcade.key.Q or player.sort_menu:
        player.sort_menu = True
        player.search_menu = False
        if key == arcade.key.L:
            player.poke_list = merge_sort(player.poke_list)
            player.sort_menu = False
        elif key == arcade.key.K:
            player.sort_menu = False


def main():
    game = MyGame(width, height, "Pokedex")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
