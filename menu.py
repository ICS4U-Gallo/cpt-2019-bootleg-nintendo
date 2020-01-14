#Improved Start Animated Menu

import arcade

sprite_scale = 0.5
native_sprite = 128
sprite_size = int(sprite_scale * native_sprite)

SCREEN_WIDTH = 768
SCREEN_HEIGHT = 640

start = False
game = False


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

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_x = x
        self.mouse_y = y

    def on_draw(delta_time):
        arcade.start_render()
        arcade.set_background_color([255, 255, 255])


def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, 'Bootleg Pokemon')
    arcade.run()


if __name__ == "__main__":
    main()
