import arcade
import loz
import pokemon
import random
import math

width = 768
height = 640


def sort_pokemon(poke):
    # sort pokemon storage by number, then level
    if len(poke) <= 1:
        return poke

    midpoint = len(poke) // 2
    left_side = sort_pokemon(poke[:midpoint])
    right_side = sort_pokemon(poke[midpoint:])
    sorted_poke = []

    left_marker = 0
    right_marker = 0
    while left_marker < len(left_side) and right_marker < len(right_side):
        if left_side[left_marker].num < right_side[right_marker].num:
            sorted_poke.append(left_side[left_marker])
            left_marker += 1
        elif left_side[left_marker].num == right_side[right_marker].num:
            if left_side[left_marker].lvl < right_side[right_marker].lvl:
                sorted_poke.append(left_side[left_marker])
                left_marker += 1
            else:
                sorted_poke.append(right_side[right_marker])
                right_marker += 1
        else:
            sorted_poke.append(right_side[right_marker])
            right_marker += 1

    while right_marker < len(right_side):
        sorted_poke.append(right_side[right_marker])
        right_marker += 1

    while left_marker < len(left_side):
        sorted_poke.append(left_side[left_marker])
        left_marker += 1

    return sorted_poke


def search_pokemon(poke_list, target):
    # search pokemon by number, return list of pokemon
    result = []
    for poke in poke_list:
        if poke.num == target:
            result.append(poke)

    return result

#
# class MyGame(arcade.Window):
#
#     def __init__(self, width, height, title):
#         super().__init__(width, height, title)
#         arcade.set_background_color(arcade.color.WHITE)


def setup(game):
    game.sto_page = 1
    game.sto_poke_list = game.player_sprite.pokemon_storage
    game.sto_selected = None
    game.sto_searching = False
    game.sto_search_number = 0


def draw_button():
    arcade.draw_xywh_rectangle_outline(20, 530, 140, 50, arcade.color.BLACK, 3)
    arcade.draw_text("Prev Page", 90, 555, arcade.color.BLACK, 25,
                     align="center", anchor_x="center",
                     anchor_y="center")

    arcade.draw_xywh_rectangle_outline(380, 530, 140, 50,
                                       arcade.color.BLACK, 3)
    arcade.draw_text("Next Page", 450, 555, arcade.color.BLACK, 25,
                     align="center", anchor_x="center",
                     anchor_y="center")

    for i in range(9):
        arcade.draw_xywh_rectangle_outline(20 + i % 3 * 175, 370 - i // 3 *
                                           175, 150, 150, arcade.color.BLACK,
                                           2)


def draw_pokemon(game):
    if len(game.sto_poke_list) // 9 >= game.sto_page:
        end = game.sto_page * 9
    else:
        end = len(game.sto_poke_list)
    for i in range((game.sto_page - 1) * 9, end):
        game.sto_poke_list[i].center_x = 95 + (i % 9) % 3 * 175
        game.sto_poke_list[i].center_y = 445 - (i % 9) // 3 * 175
        game.sto_poke_list[i].draw()


def on_draw(game):
    arcade.start_render()
    arcade.draw_text("Pokemon Storage", width / 2, height - 20,
                     arcade.color.BLACK, 40, align="center",
                     anchor_x="center", anchor_y="center")
    arcade.draw_text(f"Page: {game.sto_page}", 270, 555,
                     arcade.color.BLACK, 30, align="center",
                     anchor_x="center", anchor_y="center")
    arcade.draw_text("Q to sort by #", 540, 60, arcade.color.BLACK, 20)
    arcade.draw_text("E to search by #", 540, 40, arcade.color.BLACK, 20)

    draw_pokemon(game)
    draw_button()

    if game.sto_selected != None:
        arcade.draw_text(game.sto_selected.name, 540, 480,
                         arcade.color.BLACK, 20)
        arcade.draw_text(f"# {game.sto_selected.num}", 540,
                         460, arcade.color.BLACK, 20)
        arcade.draw_text(f"lvl: {game.sto_selected.lvl}",
                         540, 440, arcade.color.BLACK, 20)
        arcade.draw_text(f"hp: {game.sto_selected.cur_stats[0]} /"
                         f" {game.sto_selected.stats[0]}",
                         540, 420, arcade.color.BLACK, 20)
        arcade.draw_text(f"atk: {game.sto_selected.stats[1]}",
                         540, 400, arcade.color.BLACK, 20)
        arcade.draw_text(f"def: {game.sto_selected.stats[2]}",
                         540, 380, arcade.color.BLACK, 20)
        arcade.draw_text(f"spd: {game.sto_selected.stats[3]}",
                         540, 360, arcade.color.BLACK, 20)
        arcade.draw_xywh_rectangle_outline(540, 300, 200, 50,
                                           arcade.color.BLACK, 3)
        arcade.draw_text("Send to bag", 640, 325,
                         arcade.color.BLACK, 24, align="center",
                         anchor_x="center", anchor_y="center")
        if len(game.player_sprite.pokemon) >= 6:
            arcade.draw_text("bag is full", 540, 270,
                             arcade.color.BLACK, 20)
    else:
        arcade.draw_text("No Pokemon Selected", 540,
                         480, arcade.color.BLACK, 20)

    if game.sto_searching:
        arcade.draw_text("K to stop searching", 540,
                         560, arcade.color.BLACK, 20)
        arcade.draw_text(f"Searching for", 540, 530,
                         arcade.color.BLACK, 20)
        arcade.draw_text(f"pokemon #{game.sto_search_number}",
                         540, 510, arcade.color.BLACK, 20)


def key_logic(game, key):
    if key == arcade.key.Q:
        game.player_sprite.pokemon_storage =\
            sort_pokemon(game.player_sprite.pokemon_storage)
    elif key == arcade.key.E:
        game.sto_page = 1
        game.sto_searching = True
    elif key == arcade.key.K and not game.sto_searching:
        game.cur_screen = "bag"
        print(game.cur_screen)

    if game.sto_searching:
        if arcade.key.KEY_0 <= key <= arcade.key.KEY_9:
            game.sto_search_number = game.sto_search_number * 10\
                                     + (key-arcade.key.KEY_0)
        elif key == arcade.key.BACKSPACE:
            game.sto_search_number = game.sto_search_number//10
        elif key == arcade.key.K:
            game.sto_searching = False
            game.sto_poke_list = game.player_sprite.pokemon_storage


def on_key_release(self, key, modifiers):
    pass


def update(game):
    if game.sto_searching:
        game.sto_poke_list =\
            search_pokemon(game.player_sprite.pokemon_storage,
                           game.sto_search_number)
    else:
        game.sto_poke_list = game.player_sprite.pokemon_storage


def set_selected(game, num):
    try:
        game.sto_selected = game.sto_poke_list[num]
    except IndexError:
        game.sto_selected = None


def mouse_logic(game, x, y, button):
    if button == arcade.MOUSE_BUTTON_LEFT:
        game.sto_sent = None
        if 20 < x < 160 and 530 < y < 580 and game.sto_page > 1:
            game.sto_page -= 1
        elif 380 < x < 520 and 530 < y < 580 and game.sto_page <\
                math.ceil(len(game.sto_poke_list)/9):
            game.sto_page += 1
        elif 20 < x < 170 and 370 < y < 520:
            set_selected(game, 0+(game.sto_page-1)*9)
        elif 195 < x < 345 and 370 < y < 520:
            set_selected(game, 1+(game.sto_page-1)*9)
        elif 370 < x < 520 and 370 < y < 520:
            set_selected(game, 2+(game.sto_page-1)*9)
        elif 20 < x < 170 and 195 < y < 345:
            set_selected(game, 3+(game.sto_page-1)*9)
        elif 195 < x < 345 and 195 < y < 345:
            set_selected(game, 4+(game.sto_page-1)*9)
        elif 370 < x < 520 and 195 < y < 345:
            set_selected(game, 5+(game.sto_page-1)*9)
        elif 20 < x < 170 and 20 < y < 170:
            set_selected(game, 6+(game.sto_page-1)*9)
        elif 195 < x < 345 and 20 < y < 170:
            set_selected(game, 7+(game.sto_page-1)*9)
        elif 370 < x < 520 and 20 < y < 170:
            set_selected(game, 8+(game.sto_page-1)*9)

        if game.sto_selected != None:
            if 540 < x < 740 and 300 < y < 350:
                if len(game.player_sprite.pokemon) < 6:
                    game.player_sprite.pokemon_storage.remove(game.sto_selected)
                    game.player_sprite.pokemon.append(game.sto_selected)
                    game.sto_selected = None

    def on_mouse_release(self, x, y, button, key_modifiers):
        pass


def main():
    window = MyGame(width, height, 'Bootleg Pokemon')
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
