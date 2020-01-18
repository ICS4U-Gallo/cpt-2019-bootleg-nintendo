import arcade

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
        self.bag_color = arcade.color.BLACK
        self.save_color = arcade.color.BLACK
        self.exit_color = arcade.color.BLACK

        self.dex_sprite = arcade.load_texture("images/game_menu_images/"
                                              "pokedex.png")
        self.bag_sprite = arcade.load_texture("images/game_menu_images/"
                                              "bag.jpg")
        self.save_sprite = arcade.load_texture("images/game_menu_images/"
                                               "save.png")
        self.exit_sprite = arcade.load_texture("images/game_menu_images/"
                                               "exit.jpeg")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("GAME MENU", 384, 608, arcade.color.BLACK, 50,
                         align="center", anchor_x="center", anchor_y="center")

        arcade.draw_xywh_rectangle_outline(42, 295, 325, 250,
                                           self.dex_color, 5)
        arcade.draw_text("POKEDEX", 204, 480, self.dex_color, 45,
                         align="center", anchor_x="center", anchor_y="center")
        arcade.draw_texture_rectangle(192, 380, 190, 140, self.dex_sprite)

        arcade.draw_xywh_rectangle_outline(401, 295, 325, 250,
                                           self.bag_color, 5)
        arcade.draw_text("BAG", 564, 480, self.bag_color, 45,
                         align="center", anchor_x="center", anchor_y="center")
        arcade.draw_texture_rectangle(556, 380, 190, 140, self.bag_sprite)

        arcade.draw_xywh_rectangle_outline(42, 20, 325, 250,
                                           self.save_color, 5)
        arcade.draw_text("SAVE", 204, 200, self.save_color, 45,
                         align="center", anchor_x="center", anchor_y="center")
        arcade.draw_texture_rectangle(192, 91, 190, 140, self.save_sprite)

        arcade.draw_xywh_rectangle_outline(401, 20, 325, 250,
                                           self.exit_color, 5)
        arcade.draw_text("EXIT", 564, 200, self.exit_color, 45,
                         align="center", anchor_x="center", anchor_y="center")
        arcade.draw_texture_rectangle(556, 91, 150, 100, self.exit_sprite)

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
        elif key == arcade.key.K:
            print("exit")


def main():
    game = MyGame(width, height, "Game Menu")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
