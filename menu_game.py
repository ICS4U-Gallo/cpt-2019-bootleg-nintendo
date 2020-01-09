import arcade
import settings

width = 768
height = 640


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        self.select_x = 0
        self.select_y = 1

        self.dex_color = arcade.color.BLACK
        self.bag_color = arcade.color.GRAY
        self.save_color = arcade.color.GRAY
        self.exit_color = arcade.color.GRAY

        """self.dex_sprite = arcade.load_texture("images/pokedex.jpeg")
        self.bag_sprite = arcade.load_texture("images/bag.jpg")
        self.save_sprite = arcade.load_texture("images/save.png")
        self.exit_sprite = arcade.load_texture("images/exit.jpg")"""

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("GAME MENU",
                         width/2, height * 0.95, arcade.color.BLACK, 50,
                         align="center", anchor_x="center", anchor_y="center")

        arcade.draw_xywh_rectangle_outline(width/4-150,
                                           height/2-25, 325, 250,
                                           self.dex_color, 5)
        arcade.draw_text("POKEDEX", width/4 + 12.5,
                         height * 3/4, self.dex_color, 45,
                         align="center", anchor_x="center", anchor_y="center")

        arcade.draw_xywh_rectangle_outline(width * 3/4 - 175,
                                           height/2-25, 325, 250,
                                           self.bag_color, 5)
        arcade.draw_text("BAG", width * 3/4 - 12.5,
                         height * 3/4, self.bag_color, 45,
                         align="center", anchor_x="center", anchor_y="center")

        arcade.draw_xywh_rectangle_outline(width/4 - 150,
                                           height/2-300, 325,
                                           250, self.save_color, 5)
        arcade.draw_text("SAVE", width/4 + 12.5,
                         height/2-120, self.save_color, 45,
                         align="center", anchor_x="center", anchor_y="center")

        arcade.draw_xywh_rectangle_outline(width * 3/4 - 175,
                                           height/2-300, 325,
                                           250, self.exit_color, 5)
        arcade.draw_text("EXIT", width * 3/4 - 12.5,
                         height/2-120, self.exit_color, 45,
                         align="center", anchor_x="center", anchor_y="center")

    def update(self, delta_time):
        if self.select_x == 0 and self.select_y == 1:
            self.dex_color = arcade.color.BLACK
        elif self.select_x == 1 and self.select_y == 1:
            self.bag_color = arcade.color.BLACK
        elif self.select_x == 0 and self.select_y == 0:
            self.save_color = arcade.color.BLACK
        elif self.select_x == 1 and self.select_y == 0:
            self.exit_color = arcade.color.BLACK

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.W:
            if self.select_y < 1:
                self.select_y += 1
        elif key == arcade.key.S:
            if self.select_y > 0:
                self.select_y -= 1
        elif key == arcade.key.D:
            if self.select_x < 1:
                self.select_x += 1
        elif key == arcade.key.A:
            if self.select_x > 0:
                self.select_x -= 1

        self.dex_color = arcade.color.GRAY
        self.bag_color = arcade.color.GRAY
        self.save_color = arcade.color.GRAY
        self.exit_color = arcade.color.GRAY

        if key == arcade.key.L:
            if self.select_x == 0 and self.select_y == 1:  # pokedex
                print("pokedex")
            elif self.select_x == 1 and self.select_y == 1:  # bag
                print("bag")
            elif self.select_x == 0 and self.select_y == 0:  # save
                print("save")
            elif self.select_x == 1 and self.select_y == 0:  # exit
                print("exit")


def main():
    game = MyGame(width, height, "My Game")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
