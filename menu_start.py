import arcade

sprite_scale = 0.5
native_sprite = 128
sprite_size = int(sprite_scale * native_sprite)

SCREEN_WIDTH = 768
SCREEN_HEIGHT = 640


# class MyGame(arcade.Window):
#
#     def __init__(self, width, height, title):
#         super().__init__(width, height, title)
#         self.mouse_x = 0
#         self.mouse_y = 0
#         self.mouse_click = False
def setup(game):
    game.start = False  # just for start menu aesthetic
    game.load = True  # existing game
    game.cur_screen = None  # variable to indicate if game started

    game.start_clock = 30  # animation purposes
    game.start_y = -1000


def on_mouse_press(game, x, y, button):
    if button == arcade.MOUSE_BUTTON_LEFT:
        if (game.width / 2 + 150 > game.mouse_x > game.width / 2 - 150 and
                game.height / 2 + 100 > game.mouse_y > game.height / 2 + 25 and
                game.cur_screen == "start"):
            game.setup()
        if (game.width / 2 + 75 / 2 > x > game.width / 2 - 75 / 2 and
                game.height / 2 - 150 > y > game.height / 2 - 225 and
                game.cur_screen == "start"):
            game.load = False
            print("deleted previous game cuz ur bad lmao")


def on_mouse_release(game, x, y, button, modifiers):
    pass


def on_mouse_motion(game, x, y, dx, dy):
    game.mouse_x = x
    game.mouse_y = y


def on_update(game):
    if game.start_clock > 0:
        game.start_clock -= 1
        game.start_y = (game.start_clock**2)/1.5
    else:
        game.start_y = 0


def on_draw(game):
    # Draw Main menu
    arcade.set_background_color(arcade.color.WHITE)
    arcade.draw_text("Pokemon", game.width/2, 480,
                     arcade.color.BLACK, 70,
                     align="center", anchor_x="center", anchor_y="center")
    # start button v
    arcade.draw_text("Start New Game", game.width/2,
                     game.height/2+63-game.start_y, arcade.color.BLACK, 30,
                     align="center", anchor_x="center",
                     anchor_y="center")

    if (game.width / 2 + 150 > game.mouse_x > game.width / 2 -
            150 and game.height / 2 + 100 -
            game.start_y > game.mouse_y > game.height /
            2 + 25 - game.start_y):
        arcade.draw_xywh_rectangle_outline(game.width/2 - 150 - 4,
                                           game.height / 2 + 25 -
                                           4 - game.start_y,
                                           300 + 8, 75 + 8,
                                           arcade.color.RED, 7)
    else:
        arcade.draw_xywh_rectangle_outline(game.width/2 - 150,
                                           game.height/2 + 25-game.start_y,
                                           300, 75, arcade.color.BLACK, 5)

    # start button ^ load button v
    if game.load is False:
        arcade.draw_text("Load Game", game.width / 2,
                         game.height/2 + 63 - 125 - game.start_y,
                         arcade.color.GRAY, 30,
                         align="center", anchor_x="center",
                         anchor_y="center")

        arcade.draw_xywh_rectangle_outline(game.width / 2 - 150,
                                           game.height/2 - 100-game.start_y,
                                           300, 75, arcade.color.GRAY, 5)

        arcade.draw_xywh_rectangle_outline(game.width/2 - 75 / 2,
                                           game.height/2 - 225 - game.start_y,
                                           75, 75, arcade.color.GRAY, 5)

    else:
        arcade.draw_text("Load Game", game.width / 2,
                         game.height/2 + 63 - 125 - game.start_y,
                         arcade.color.BLACK, 30,
                         align="center", anchor_x="center",
                         anchor_y="center")

        if (game.width / 2 + 150 > game.mouse_x > game.width / 2 - 150 and
                game.height/2 - 25 > game.mouse_y > game.height/2 - 100):
            arcade.draw_xywh_rectangle_outline(game.width / 2 - 150 - 4,
                                               game.height/2 - 100 - 4 -
                                               game.start_y, 300 + 8,
                                               75 + 8, arcade.color.RED, 7)

        else:
            arcade.draw_xywh_rectangle_outline(game.width / 2 - 150,
                                               game.height/2 - 100 -
                                               game.start_y, 300,
                                               75, arcade.color.BLACK, 5)

        if (game.width / 2 + 75 / 2 > game.mouse_x > game.width / 2 - 75 /
                2 and game.height / 2 - 150 > game.mouse_y > game.height /
                2 - 225):
            arcade.draw_xywh_rectangle_outline(game.width / 2 - 75 / 2 - 4,
                                               game.height / 2 - 225 - 4 -
                                               game.start_y, 75 + 8, 75 + 8,
                                               arcade.color.RED, 7)

        else:
            arcade.draw_xywh_rectangle_outline(game.width / 2 - 75 / 2,
                                               game.height / 2 - 225 -
                                               game.start_y, 75,
                                               75, arcade.color.BLACK, 5)

        # end of menu code


def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, 'Bootleg Pokemon')
    arcade.run()


if __name__ == "__main__":
    main()
