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


def binary_search(target, numbers):
    start = 0
    end = len(numbers) - 1

    while end >= start:
        mid = (start + end) // 2

        if numbers[mid].num == target:
            return mid
        elif numbers[mid].num > target:
            end = mid - 1
        elif numbers[mid].num < target:
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
        if left_side[left_marker].num < right_side[right_marker].num:
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


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        self.pointer = 0
        self.sort_menu = False
        self.search_menu = False
        self.search_number = ""

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Pokedex", 20, height - 70,
                         arcade.color.BLACK, 50)
        arcade.draw_text("Total Caught:", 20, height - 120,
                         arcade.color.BLACK, 30)
        arcade.draw_text(str(len(poke_list)), 250, height - 120,
                         arcade.color.BLACK, 30)
        arcade.draw_text("Q - Sort", 30, 30, arcade.color.BLACK, 60)
        arcade.draw_text("E - Search", 370, 30, arcade.color.BLACK, 60)

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

        if self.search_menu:
            arcade.draw_xywh_rectangle_filled(100, 100, 568, 440,
                                              arcade.color.BLACK)
            arcade.draw_xywh_rectangle_filled(110, 110, 548, 420,
                                              arcade.color.WHITE)
            arcade.draw_text("Enter Pokemon Number:", 140, 450,
                             arcade.color.BLACK, 35)
            arcade.draw_text(" " + self.search_number, 140, 200,
                             arcade.color.BLACK, 220)
        if self.sort_menu:
            arcade.draw_xywh_rectangle_filled(100, 100, 568, 440,
                                              arcade.color.BLACK)
            arcade.draw_xywh_rectangle_filled(110, 110, 548, 420,
                                              arcade.color.WHITE)
            arcade.draw_text("Do you want to sort", 115, 380,
                             arcade.color.BLACK, 50)
            arcade.draw_text("the Pokedex?", 175, 310, arcade.color.BLACK, 50)

    def update(self, delta_time):
        pass

    def on_key_press(self, key, key_modifiers):
        global poke_list
        if key == arcade.key.W:
            if self.pointer != 0:
                self.pointer -= 1
        elif key == arcade.key.S:
            if self.pointer != len(poke_list) - 1:
                self.pointer += 1
        if key == arcade.key.E or self.search_menu:
            self.search_menu = True
            self.sort_menu = False

            if key == arcade.key.KEY_0:
                if len(self.search_number) < 2:
                    self.search_number += "0"
            elif key == arcade.key.KEY_1:
                if len(self.search_number) < 2:
                    self.search_number += "1"
            elif key == arcade.key.KEY_2:
                if len(self.search_number) < 2:
                    self.search_number += "2"
            elif key == arcade.key.KEY_3:
                if len(self.search_number) < 2:
                    self.search_number += "3"
            elif key == arcade.key.KEY_4:
                if len(self.search_number) < 2:
                    self.search_number += "4"
            elif key == arcade.key.KEY_5:
                if len(self.search_number) < 2:
                    self.search_number += "5"
            elif key == arcade.key.KEY_6:
                if len(self.search_number) < 2:
                    self.search_number += "6"
            elif key == arcade.key.KEY_7:
                if len(self.search_number) < 2:
                    self.search_number += "7"
            elif key == arcade.key.KEY_8:
                if len(self.search_number) < 2:
                    self.search_number += "8"
            elif key == arcade.key.KEY_9:
                if len(self.search_number) < 2:
                    self.search_number += "9"
            elif key == arcade.key.BACKSPACE:
                self.search_number = self.search_number[:-1]

            if key == arcade.key.L and self.search_number != "":
                found = binary_search(int(self.search_number), poke_list)

                if found != -1:
                    self.pointer = found
                self.search_menu = False
                self.search_number = ""

            elif key == arcade.key.K:
                self.search_menu = False
                self.search_number = ""

        if key == arcade.key.Q or self.sort_menu:
            self.sort_menu = True
            self.search_menu = False
            if key == arcade.key.L:
                poke_list = merge_sort(poke_list)
                self.sort_menu = False
            elif key == arcade.key.K:
                self.sort_menu = False


def main():
    game = MyGame(width, height, "My Game")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
