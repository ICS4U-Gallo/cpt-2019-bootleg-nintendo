import arcade

sprite_scale = 0.5
native_sprite = 128
sprite_size = int(sprite_scale * native_sprite)

SCREEN_WIDTH = 768
SCREEN_HEIGHT = 640

pause = True


def main_menu():
    # Draw Main menu
    arcade.set_background_color(arcade.color.WHITE)
    arcade.draw_text("Pokeman",
                     SCREEN_WIDTH/2, 480, arcade.color.BLACK, 70,
                     align="center", anchor_x="center", anchor_y="center")
    if pause is True:
        arcade.draw_text("Plae", SCREEN_WIDTH/2,
                        SCREEN_HEIGHT/2+13, arcade.color.BLACK, 30,
                        align="center", anchor_x="center", anchor_y="center")

    else:
        arcade.draw_text("lmao u touched me", SCREEN_WIDTH/2,
                        SCREEN_HEIGHT/2+13, arcade.color.BLACK, 30,
                        align="center", anchor_x="center", anchor_y="center")
    
    arcade.draw_xywh_rectangle_outline(SCREEN_WIDTH/2-150,
                                       SCREEN_HEIGHT/2-25, 300, 75,
                                       arcade.color.BLACK, 5)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color([0, 0, 0])

    def on_mouse_press(self, x, y, button, modifiers):

        global pause

        if button == (arcade.MOUSE_BUTTON_LEFT and
                      SCREEN_WIDTH/2+150 > x > SCREEN_WIDTH/2-150 and
                      SCREEN_HEIGHT/2+50 > y > SCREEN_HEIGHT/2-25):
            print('bruh', x, y)
            pause = not pause

    def on_draw(delta_time):
        arcade.start_render()
        main_menu()


def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, 'Ponkymohn')
    arcade.run()


if __name__ == "__main__":
    main()
