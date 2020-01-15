import arcade

sprite_scale = 0.5
native_sprite = 128
sprite_size = int(sprite_scale * native_sprite)

SCREEN_WIDTH = 768
SCREEN_HEIGHT = 640

start = False  # just for start menu aesthetic

load = True  # existing game

game = False  # variable to indicate if game started

start_clock = 30
start_y = -1000
global_clock = 0


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color([0, 0, 0])
        self.mouse_x = 0
        self.mouse_y = 0
        self.mouse_click = False

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.mouse_click = True

    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.mouse_click = False

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_x = x
        self.mouse_y = y

    def on_update(self, delta_time):
        global game, start, start_clock, start_y

        if start is False:
            if self.mouse_click is True:
                start = True
        else:
            if start_clock > 0:
                start_clock -= 1
                start_y = (start_clock**2)/1.5
            else:
                start_y = 0
            print(start_clock)
            if (SCREEN_WIDTH/2+150 > self.mouse_x > SCREEN_WIDTH/2-150 and
                    SCREEN_HEIGHT/2+100-start_y > self.mouse_y > SCREEN_HEIGHT/2+25-start_y and
                    self.mouse_click is True and game is False):
                game = True

    def on_draw(self):
        arcade.start_render()
        # Draw Main menu
        arcade.set_background_color(arcade.color.WHITE)
        arcade.draw_text("Pokemon", SCREEN_WIDTH/2, 480, 
                         arcade.color.BLACK, 70,
                         align="center", anchor_x="center", anchor_y="center")

        if start is False:
            pass
        else:
            if game is False:
                # start button v
                arcade.draw_text("Start New Game", SCREEN_WIDTH/2,
                                 SCREEN_HEIGHT/2+63-start_y, arcade.color.BLACK, 30,
                                 align="center", anchor_x="center",
                                 anchor_y="center")

                if (SCREEN_WIDTH/2+150 > self.mouse_x > SCREEN_WIDTH/2-150 and
                    SCREEN_HEIGHT/2+100-start_y > self.mouse_y > SCREEN_HEIGHT/2+25-start_y):
                    arcade.draw_xywh_rectangle_outline(SCREEN_WIDTH/2-150-4,
                                                       SCREEN_HEIGHT/2+25-4-start_y,
                                                       300+8, 75+8,
                                                       arcade.color.RED, 7)
                else:
                    arcade.draw_xywh_rectangle_outline(SCREEN_WIDTH/2-150,
                                                       SCREEN_HEIGHT/2+25-start_y, 300,
                                                       75, arcade.color.BLACK,
                                                       5)
                
                # start button ^ load button v
                if load is False:
                    arcade.draw_text("Load Game", SCREEN_WIDTH/2,
                                    SCREEN_HEIGHT/2+63-125-start_y, arcade.color.GRAY, 30,
                                    align="center", anchor_x="center",
                                    anchor_y="center")

                    arcade.draw_xywh_rectangle_outline(SCREEN_WIDTH/2-150,
                                                   SCREEN_HEIGHT/2-100-start_y, 300, 
                                                   75, arcade.color.GRAY, 5)

                else:
                    arcade.draw_text("Load Game", SCREEN_WIDTH/2,
                                    SCREEN_HEIGHT/2+63-125-start_y, arcade.color.BLACK, 30,
                                    align="center", anchor_x="center",
                                    anchor_y="center")

                    if (SCREEN_WIDTH/2+150 > self.mouse_x > SCREEN_WIDTH/2-150 and
                    SCREEN_HEIGHT/2-25 > self.mouse_y > SCREEN_HEIGHT/2-100):
                        arcade.draw_xywh_rectangle_outline(SCREEN_WIDTH/2-150-4,
                                                    SCREEN_HEIGHT/2-100-4-start_y, 300+8, 
                                                    75+8, arcade.color.RED, 7)

                    else:
                        arcade.draw_xywh_rectangle_outline(SCREEN_WIDTH/2-150,
                                                    SCREEN_HEIGHT/2-100-start_y, 300, 
                                                    75, arcade.color.BLACK, 5)
                    # load button ^ delete button v

                if (SCREEN_WIDTH/2+75/2 > self.mouse_x > SCREEN_WIDTH/2-75/2 and
                    SCREEN_HEIGHT/2-150 > self.mouse_y > SCREEN_HEIGHT/2-225):
                    arcade.draw_xywh_rectangle_outline(SCREEN_WIDTH/2-75/2-4,
                                                   SCREEN_HEIGHT/2-225-4-start_y, 75+8,
                                                   75+8, arcade.color.RED, 7)
                else:
                    arcade.draw_xywh_rectangle_outline(SCREEN_WIDTH/2-75/2,
                                                   SCREEN_HEIGHT/2-225-start_y, 75,
                                                   75, arcade.color.BLACK, 5)

            # end of menu code
            else:
                arcade.draw_text("Game started wow", SCREEN_WIDTH/2,
                                SCREEN_HEIGHT/2+63, arcade.color.BLACK, 30,
                                align="center", anchor_x="center", anchor_y="center")


def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, 'Bootleg Pokemon')
    arcade.run()


if __name__ == "__main__":
    main()
