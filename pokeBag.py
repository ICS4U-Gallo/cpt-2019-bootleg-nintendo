import arcade
import loz
import pokemon
import random

width = 768
height = 640


def sort_pokemon(poke):
    # sort pokemon storage by level
    if len(poke) == 1:
        return poke

    midpoint = len(poke) // 2
    left_side = sort_pokemon(poke[:midpoint])
    right_side = sort_pokemon(poke[midpoint:])
    sorted_poke = []

    left_marker = 0
    right_marker = 0
    while left_marker < len(left_side) and right_marker < len(right_side):
        if left_side[left_marker].num <= right_side[right_marker].num:
            sorted_poke.append(left_side[left_marker])
            left_marker += 1
        else:
            sorted_poke.append(right_side[right_marker])
            right_marker += 1

    while right_marker < len(right_side):
        sorted_poke.append(right_side[right_marker])
        right_marker += 1

    while left_marker < len(left_side):
        sorted_poke.append(left_side[left_marker])
        left_marker += 1

    return sorted_poke


def search_pokemon(poke_list, target):
    # search pokemon by name, return list of pokemon
    result = []
    for poke in poke_list:
        if poke.name == target:
            result.append(poke)

    return result


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        self.p = loz.Player()

        for i in range(10):
            poke = pokemon.Pokemon.random_poke()
            poke.addlevel(random.randrange(1,50))
            self.p.pokemon_storage.append(poke)
        for i in self.p.pokemon_storage:
            print(i)

    def on_draw(self):
        arcade.start_render()
        for i in range(len(self.p.pokemon_storage)):
            self.p.pokemon_storage[i].center_x = 100 + i%3*200
            self.p.pokemon_storage[i].center_y = 500 - i//3*200
            self.p.pokemon_storage[i].draw()
            
    def on_key_press(self, key, modifiers):
        if key == arcade.key.Q:
            self.p.pokemon_storage = sort_pokemon(self.p.pokemon_storage)

    def update(self, delta_time):
        pass


def main():
    window = MyGame(width, height, 'Bootleg Pokemon')
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
