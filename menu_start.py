import arcade

sprite_scale = 0.5
native_sprite = 128
sprite_size = int(sprite_scale * native_sprite)

SCREEN_WIDTH = 768
SCREEN_HEIGHT = 640

game = False


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color([0, 0, 0])
        self.mouse_x = 0
        self.mouse_y = 0

    def on_mouse_press(self, x, y, button, modifiers):

        global game

        if button == (arcade.MOUSE_BUTTON_LEFT and
                      SCREEN_WIDTH/2+150 > x > SCREEN_WIDTH/2-150 and
                      SCREEN_HEIGHT/2+100 > y > SCREEN_HEIGHT/2+25
                      and game is False):
            game = not game

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_x = x
        self.mouse_y = y

    def on_draw(self):
        arcade.start_render()
        # Draw Main menu
        arcade.set_background_color(arcade.color.WHITE)
        arcade.draw_text("PokeMan",
                        SCREEN_WIDTH/2, 480, arcade.color.BLACK, 70,
                        align="center", anchor_x="center", anchor_y="center")
        
        if game is False:
            arcade.draw_text("Stawt New Gaym", SCREEN_WIDTH/2,
                            SCREEN_HEIGHT/2+63, arcade.color.BLACK, 30,
                            align="center", anchor_x="center", anchor_y="center")

            if (SCREEN_WIDTH/2+150 > self.mouse_x > SCREEN_WIDTH/2-150 and
                SCREEN_HEIGHT/2+100 > self.mouse_y > SCREEN_HEIGHT/2+25 and
                    game is False):
                arcade.draw_xywh_rectangle_outline(SCREEN_WIDTH/2-150-4,
                                        SCREEN_HEIGHT/2+25-4, 300+8, 75+8,
                                        arcade.color.RED, 5)
            else:
                arcade.draw_xywh_rectangle_outline(SCREEN_WIDTH/2-150,
                                        SCREEN_HEIGHT/2+25, 300, 75,
                                        arcade.color.BLACK, 5)
                    
        else:
            arcade.draw_text("lmao u touched me", SCREEN_WIDTH/2,
                            SCREEN_HEIGHT/2+63, arcade.color.BLACK, 30,
                            align="center", anchor_x="center", anchor_y="center")


def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, 'Ponkymohn')
    arcade.run()


if __name__ == "__main__":
    main()
