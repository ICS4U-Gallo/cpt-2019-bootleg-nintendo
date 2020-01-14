import arcade
import settings
import pokemon  # temporary maybe

width = 768
height = 640

# poke_list = ["TORKOAL", "GARBAGE", "PIKACHU", "EEVEE", "GARCHOMP", "
# VESPIQUEN", "COMBEE", "RAYQUAZA"]
poke_list = [pokemon.Pokemon.Charmander(), pokemon.Pokemon.Squirtle(),
             pokemon.Pokemon.Bulbasaur(), pokemon.Pokemon.IceCream(),
             pokemon.Pokemon.Garbage(), pokemon.Pokemon.torkoal(),
             pokemon.Pokemon.Klefki(), pokemon.Pokemon.Magikarp(),
             pokemon.Pokemon.Magikarp(), pokemon.Pokemon.Charmander(),
             pokemon.Pokemon.Garbage(), pokemon.Pokemon.Magikarp(),
             pokemon.Pokemon.Magikarp(), pokemon.Pokemon.Squirtle(),
             pokemon.Pokemon.IceCream(), pokemon.Pokemon.torkoal()]


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        self.pointer = 0

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Pokedex", 20, height - 70,
                         arcade.color.BLACK, 50)
        arcade.draw_text("Total Caught:", 20, height - 120,
                         arcade.color.BLACK, 30)
        arcade.draw_text(str(len(poke_list)), 250, height - 120,
                         arcade.color.BLACK, 30)

        arcade.draw_xywh_rectangle_outline(10, height * 2/3 - 20, 450, 70,
                                           arcade.color.GRAY, 3)
        arcade.draw_xywh_rectangle_outline(5, height / 2 - 30, 460, 90,
                                           arcade.color.BLACK, 5)
        arcade.draw_xywh_rectangle_outline(10, height / 3 - 20, 450, 70,
                                           arcade.color.GRAY, 3)

        if self.pointer - 1 != -1:
            arcade.draw_text("{}: {}".format(poke_list[self.pointer - 1].num,
                             poke_list[self.pointer - 1].name), 20,
                             height * 2/3, arcade.color.BLACK, 20)

        arcade.draw_text("{}: {}".format(poke_list[self.pointer].num,
                         poke_list[self.pointer].name), 20,
                         height/2, arcade.color.BLACK, 30)

        if self.pointer + 1 != len(poke_list):
            arcade.draw_text("{}: {}".format(poke_list[self.pointer + 1].num,
                             poke_list[self.pointer + 1].name), 20,
                             height/3, arcade.color.BLACK, 20)

        arcade.draw_triangle_filled(475, height/2+15, 495, height/2-5, 495,
                                    height/2 + 35, arcade.color.BLACK)
        arcade.draw_xywh_rectangle_outline(500, 210, 250, 250,
                                           arcade.color.BLACK, 10)
        arcade.draw_texture_rectangle(625, 335, 240, 240,
                                      poke_list[self.pointer].texture)

    def update(self, delta_time):
        pass

    def binary_search(target, numbers):
        start = 0
        end = len(numbers) - 1

        while end >= start:
            mid = (start + end) // 2

            if numbers[mid] == target:
                return mid
            elif numbers[mid] > target:
                end = mid - 1
            elif numbers[mid] < target:
                start = mid + 1

        return -1

    def merge_sort(numbers):
        if len(numbers) == 1:
            return numbers

        left_side = merge_sort(numbers[:len(numbers)//2])
        right_side = merge_sort(numbers[len(numbers)//2:])

        left_marker, right_marker = 0, 0

        new_list = []

        while left_marker < len(left_side) and right_marker < len(right_side):
            if left_side[left_marker] < right_side[right_marker]:
                new_list.append(left_side[left_marker])
                left_marker += 1
            else:
                new_list.append(right_side[right_marker])
                right_marker += 1

        while right_marker < len(right_side):
            new_list.append(right_side[right_marker])
            right_marker += 1

        while left_marker < len(left_side):
            new_list.append(left_side[left_marker])
            left_marker += 1

        return new_list

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
