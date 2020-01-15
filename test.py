from arcade.gui import *
import settings

import os


class Button(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="Play", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.game.action = self.text
            self.pressed = False


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "GUI Text Buton Example")

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        arcade.set_background_color(arcade.color.WHITE)
        self.action  = None
        self.theme = None

    def set_button_textures(self):
        normal = ":resources:gui_themes/Fantasy/Buttons/Normal.png"
        hover = ":resources:gui_themes/Fantasy/Buttons/Hover.png"
        clicked = ":resources:gui_themes/Fantasy/Buttons/Clicked.png"
        locked = ":resources:gui_themes/Fantasy/Buttons/Locked.png"
        self.theme.add_button_textures(normal, hover, clicked, locked)

    def setup_theme(self):
        self.theme = Theme()
        self.theme.set_font(24, arcade.color.WHITE)
        self.set_button_textures()

    def set_buttons(self):
        self.button_list.append(Button(self, 300, 115, 200, 70, "Fight", theme=self.theme))
        self.button_list.append(Button(self, 500, 115, 200, 70, "Switch", theme=self.theme))

    def setup(self):
        self.setup_theme()
        self.set_buttons()

    def on_draw(self):
        arcade.start_render()
        super().on_draw()
        bg = arcade.load_texture("images/battle_background.jpg")
        arcade.draw_texture_rectangle(settings.WIDTH/2, (settings.HEIGHT+150)/2,
                                      settings.WIDTH, settings.HEIGHT-150, bg)

    def update(self, delta_time):
        pass


def main():
    game = MyGame()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
