import arcade
import loz
import pokemon
import random
import math

width = 768
height = 640


def search_for(poke_list, target):
    for i, poke in enumerate(poke_list):
        if target == poke:
            return i

# class MyGame(arcade.Window):
#
#     def __init__(self, width, height, title):
#         super().__init__(width, height, title)
#         arcade.set_background_color(arcade.color.WHITE)
#


def setup(game):
    game.selected = None
    game.switch_pos = False
    game.switched = False


def on_draw(game):
    arcade.start_render()
    arcade.draw_text("Pokemon", width / 2, height - 20,
                     arcade.color.BLACK, 40, align="center",
                     anchor_x="center", anchor_y="center")

    for i in range(len(game.player_sprite.pokemon)):
        game.player_sprite.pokemon[i].center_x = 125 +\
                                                 i % 2 * 175
        game.player_sprite.pokemon[i].center_y = 445 - i // 2 * 175
        game.player_sprite.pokemon[i].draw()

    for i in range(6):
        arcade.draw_xywh_rectangle_outline(50 + i % 2 * 175,
                                           370 - i // 2 * 175,
                                           150, 150,
                                           arcade.color.BLACK, 2)

    if game.selected != None:
        arcade.draw_text(game.selected.name, 440,
                         480, arcade.color.BLACK, 20)
        arcade.draw_text(f"# {game.selected.num}",
                         440, 460, arcade.color.BLACK, 20)
        arcade.draw_text(f"lvl: {game.selected.lvl}", 440,
                         440, arcade.color.BLACK, 20)
        arcade.draw_text(f"hp: {game.selected.cur_stats[0]} /"
                         f" {game.selected.stats[0]}", 440, 420,
                         arcade.color.BLACK, 20)
        arcade.draw_text(f"atk: {game.selected.stats[1]}", 440,
                         400, arcade.color.BLACK, 20)
        arcade.draw_text(f"def: {game.selected.stats[2]}", 440,
                         380, arcade.color.BLACK, 20)
        arcade.draw_text(f"spd: {game.selected.stats[3]}", 440,
                         360, arcade.color.BLACK, 20)

        arcade.draw_xywh_rectangle_outline(440, 270, 200, 50,
                                           arcade.color.BLACK, 3)
        arcade.draw_text("switch", 540, 295, arcade.color.BLACK,
                         25, align="center", anchor_x="center",
                         anchor_y="center")
        arcade.draw_xywh_rectangle_outline(440, 200, 200, 50,
                                           arcade.color.BLACK, 3)
        arcade.draw_text("send to storage", 540, 225,
                         arcade.color.BLACK, 24, align="center",
                         anchor_x="center", anchor_y="center")
    else:
        arcade.draw_text("No Pokemon Selected", 440,
                         480, arcade.color.BLACK, 20)

    if game.switch_pos:
        arcade.draw_text("Switching", 440, 510,
                         arcade.color.BLACK, 20)


def key_logic(game, key):
    if key == arcade.key.K:
        game.cur_screen = "bag"


def on_key_release(game, key, modifiers):
    pass


def update(game, delta_time):
    pass


def set_selected(game, num):
    try:
        game.selected = game.player_sprite.pokemon[num]
    except IndexError:
        game.selected = None


def click_on_pokemon(game, x, y):
    if 20 < x < 170 and 370 < y < 520:
        set_selected(game, 0)
    elif 195 < x < 345 and 370 < y < 520:
        set_selected(game, 1)
    elif 20 < x < 170 and 195 < y < 345:
        set_selected(game, 2)
    elif 195 < x < 345 and 195 < y < 345:
        set_selected(game, 3)
    elif 20 < x < 170 and 20 < y < 170:
        set_selected(game, 4)
    elif 195 < x < 345 and 20 < y < 170:
        set_selected(game, 5)
    if game.switch_pos:
        game.switched = True


def mouse_logic(game, x, y, button):
    if button == arcade.MOUSE_BUTTON_LEFT:
        click_on_pokemon(game, x, y)
        if game.selected != None:
            if 400 < x < 600 and 270 < y < 320:
                game.switch_pos = True
                game.switch_from = game.selected
            elif 400 < x < 600 and 200 < y < 250:
                game.player_sprite.pokemon.remove(game.selected)
                game.player_sprite.pokemon_storage.append(game.selected)
                game.selected = None
        if game.switch_pos:
            if game.switched:
                j = search_for(game.player_sprite.pokemon,
                               game.selected)
                game.player_sprite.pokemon[search_for(game.player_sprite.pokemon,
                                                      game.switch_from)], game.player_sprite.pokemon[j] = game.selected, game.switch_from
                game.switch_pos = False
                game.switched = False


def on_mouse_release(self, x, y, button, key_modifiers):
    pass


def main():
    window = MyGame(width, height, 'Bootleg Pokemon')
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
