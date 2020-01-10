import arcade
import settings
import pokemon  # temporary maybe

width = 768
height = 640

# poke_list = ["TORKOAL", "GARBAGE", "PIKACHU", "EEVEE", "GARCHOMP", "VESPIQUEN", "COMBEE", "RAYQUAZA"]
poke_list = [pokemon.Pokemon.Charmander(), pokemon.Pokemon.Squirtle(),
             pokemon.Pokemon.Bulbasaur(), pokemon.Pokemon.IceCream(),
             pokemon.Pokemon.Garbage(), pokemon.Pokemon.torkoal(),
             pokemon.Pokemon.Klefki(), pokemon.Pokemon.Magikarp()]


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        self.pointer = 0

    def on_draw(self):
        arcade.start_render()

        if self.pointer - 1 != -1:
            arcade.draw_text(poke_list[self.pointer - 1].name, 60,
                             height * 2/3, arcade.color.BLACK, 50)

        arcade.draw_text(poke_list[self.pointer].name, 20,
                         height/2, arcade.color.BLACK, 50)

        if self.pointer + 1 != len(poke_list):
            arcade.draw_text(poke_list[self.pointer + 1].name, 60,
                             height/3, arcade.color.BLACK, 50)

        arcade.draw_texture_rectangle(width/2, height/2, 100, 100, poke_list[self.pointer].texture)

    def update(self, delta_time):
        pass

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.W:
            if self.pointer != 0:
                self.pointer -= 1
        elif key == arcade.key.S:
            if self.pointer != len(poke_list) - 1:
                self.pointer += 1


def main():
    game = MyGame(width, height, "My Game")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
