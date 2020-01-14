import arcade
import random
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Poke Me"


class TextButton:

    def __init__(self, center_x, center_y, width, height, text, font_size=18,
                 font_face="Arial", face_color=arcade.color.LIGHT_GRAY,
                 highlight_color=arcade.color.WHITE,
                 shadow_color=arcade.color.GRAY, button_height=2):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font_face = font_face
        self.pressed = False
        self.face_color = face_color
        self.highlight_color = highlight_color
        self.shadow_color = shadow_color
        self.button_height = button_height

    def draw(self):
        """ Draw the button """
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width,
                                     self.height, self.face_color)

        if not self.pressed:
            color = self.shadow_color
        else:
            color = self.highlight_color

        # Bottom horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y -
                         self.height / 2, self.center_x + self.width / 2,
                         self.center_y - self.height / 2, color,
                         self.button_height)

        # Right vertical
        arcade.draw_line(self.center_x + self.width / 2, self.center_y -
                         self.height / 2, self.center_x + self.width / 2,
                         self.center_y + self.height / 2, color,
                         self.button_height)

        if not self.pressed:
            color = self.highlight_color
        else:
            color = self.shadow_color

        # Top horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y +
                         self.height / 2, self.center_x + self.width / 2,
                         self.center_y + self.height / 2, color,
                         self.button_height)

        # Left vertical
        arcade.draw_line(self.center_x - self.width / 2, self.center_y -
                         self.height / 2, self.center_x - self.width / 2,
                         self.center_y + self.height / 2, color,
                         self.button_height)

        x = self.center_x
        y = self.center_y
        if not self.pressed:
            x -= self.button_height
            y += self.button_height

        arcade.draw_text(self.text, x, y,
                         arcade.color.BLACK, font_size=self.font_size,
                         width=self.width, align="center",
                         anchor_x="center", anchor_y="center")

    def on_press(self):
        self.pressed = True

    def on_release(self):
        self.pressed = False


def check_mouse_press_for_buttons(x, y, button_list):
    """ Given an x, y, see if we need to register any button clicks. """
    for button in button_list:
        if x > button.center_x + button.width / 2:
            continue
        if x < button.center_x - button.width / 2:
            continue
        if y > button.center_y + button.height / 2:
            continue
        if y < button.center_y - button.height / 2:
            continue
        button.on_press()


def check_mouse_release_for_buttons(_x, _y, button_list):
    for button in button_list:
        if button.pressed:
            button.on_release()


class Resume(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Resume", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Heals(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Heals", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function


class Buff_items(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Buffs", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function


class Balls(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Balls", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        arcade.set_background_color(arcade.color.GRAY)

        self.pause = False
        self.button_list = None

    def setup(self):

        self.button_list = []

        play_button = Resume(60, 570, self.resume_program)
        self.button_list.append(play_button)

        heals_button = Heals(60, 515, self.heals_button)
        self.button_list.append(heals_button)

        balls_button = Balls(60, 460, self.balls_button)
        self.button_list.append(balls_button)

        buff_button = Buff_items(60, 405, self.buff_button)
        self.button_list.append(buff_button)

    def on_draw(self):

        arcade.start_render()

        for button in self.button_list:
            button.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        check_mouse_press_for_buttons(x, y, self.button_list)

    def on_mouse_release(self, x, y, button, key_modifiers):
        check_mouse_release_for_buttons(x, y, self.button_list)

    def resume_program(self):
        self.pause = False

    def heals_button(self):
        pass

    def balls_button(self):
        pass

    def buff_button(self):
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
