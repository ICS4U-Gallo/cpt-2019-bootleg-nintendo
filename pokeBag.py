import arcade
import loz
import pokemon
import random
import math

width = 768
height = 640


def sort_pokemon(poke):
    # sort pokemon storage by number, then level
    if len(poke) <= 1:
        return poke

    midpoint = len(poke) // 2
    left_side = sort_pokemon(poke[:midpoint])
    right_side = sort_pokemon(poke[midpoint:])
    sorted_poke = []

    left_marker = 0
    right_marker = 0
    while left_marker < len(left_side) and right_marker < len(right_side):
        if left_side[left_marker].num < right_side[right_marker].num:
            sorted_poke.append(left_side[left_marker])
            left_marker += 1
        elif left_side[left_marker].num == right_side[right_marker].num:
            if left_side[left_marker].lvl < right_side[right_marker].lvl:
                sorted_poke.append(left_side[left_marker])
                left_marker += 1
            else:
                sorted_poke.append(right_side[right_marker])
                right_marker += 1
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
    # search pokemon by number, return list of pokemon
    result = []
    for poke in poke_list:
        if poke.num == target:
            result.append(poke)

    return result


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        self.p = loz.Player()
        self.page = 1
        self.poke_list = self.p.pokemon_storage
        self.selected = None
        self.searching = False
        self.search_number = 0

        for i in range(20):
            poke = pokemon.Pokemon.random_poke()
            poke.addlevel(random.randrange(1,50))
            self.p.pokemon_storage.append(poke)
        for i in self.p.pokemon_storage:
            print(i)

    def draw_button(self):
        arcade.draw_xywh_rectangle_outline(20, 530, 140, 50, arcade.color.BLACK, 3)
        arcade.draw_text("Prev Page", 90, 555, arcade.color.BLACK, 25, align="center", anchor_x="center",
                         anchor_y="center")

        arcade.draw_xywh_rectangle_outline(380, 530, 140, 50, arcade.color.BLACK, 3)
        arcade.draw_text("Next Page", 450, 555, arcade.color.BLACK, 25, align="center", anchor_x="center",
                         anchor_y="center")

        for i in range(9):
            arcade.draw_xywh_rectangle_outline(20+i%3*175, 370-i//3*175, 150, 150, arcade.color.BLACK, 2)

    def draw_pokemon(self):
        if len(self.poke_list)//9 >= self.page:
            end = self.page*9
        else:
            end = len(self.poke_list)
        for i in range((self.page-1)*9, end):
            self.poke_list[i].center_x = 95 + (i%9)%3*175
            self.poke_list[i].center_y = 445 - (i%9)//3*175
            self.poke_list[i].draw()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Pokemon Storage", width/2, height-20, arcade.color.BLACK, 40, align="center",
                         anchor_x="center", anchor_y="center")
        arcade.draw_text("Q to sort by #", 270, 567, arcade.color.BLACK, 20, align="center",
                         anchor_x="center", anchor_y="center")
        arcade.draw_text("E to search by #", 270, 543, arcade.color.BLACK, 20, align="center",
                         anchor_x="center", anchor_y="center")

        self.draw_pokemon()
        self.draw_button()

        if self.selected != None:
            arcade.draw_text(self.selected.name, 540, 480, arcade.color.BLACK, 20)
            arcade.draw_text(f"# {self.selected.num}", 540, 460, arcade.color.BLACK, 20)
            arcade.draw_text(f"lvl: {self.selected.lvl}", 540, 440, arcade.color.BLACK, 20)
            arcade.draw_text(f"hp: {self.selected.cur_stats[0]} / {self.selected.stats[0]}", 540, 420, arcade.color.BLACK, 20)
            arcade.draw_text(f"atk: {self.selected.stats[1]}", 540, 400, arcade.color.BLACK, 20)
            arcade.draw_text(f"def: {self.selected.stats[2]}", 540, 380, arcade.color.BLACK, 20)
            arcade.draw_text(f"spd: {self.selected.stats[3]}", 540, 360, arcade.color.BLACK, 20)
        else:
            arcade.draw_text("No Pokemon Selected", 540, 480, arcade.color.BLACK, 20)

        if self.searching:
            arcade.draw_text("Escape to back", 540, 560, arcade.color.BLACK, 20)
            arcade.draw_text(f"Searching for", 540, 530, arcade.color.BLACK, 20)
            arcade.draw_text(f"pokemon #{self.search_number}", 540, 510, arcade.color.BLACK, 20)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.Q:
            self.p.pokemon_storage = sort_pokemon(self.p.pokemon_storage)
        elif key == arcade.key.E:
            self.searching = True

        if self.searching:
            if arcade.key.KEY_0 <= key <= arcade.key.KEY_9:
                self.search_number = self.search_number*10 + (key-arcade.key.KEY_0)
            elif key == arcade.key.BACKSPACE:
                self.search_number = self.search_number//10
            elif key == arcade.key.ESCAPE:
                self.searching = False
                self.poke_list = self.p.pokemon_storage

    def on_key_release(self, key, modifiers):
        pass

    def update(self, delta_time):
        if self.searching:
            self.poke_list = search_pokemon(self.p.pokemon_storage, self.search_number)

    def set_selected(self, num):
        try:
            self.selected = self.poke_list[num]
        except IndexError:
            self.selected = None

    def on_mouse_press(self, x, y, button, key_modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            if 20 < x < 160 and 530 < y < 580 and self.page > 1:
                self.page -= 1
            elif 380 < x < 520 and 530 < y < 580 and self.page < math.ceil(len(self.poke_list)/9):
                self.page += 1
            elif 20 < x < 170 and 370 < y < 520:
                self.set_selected(0+(self.page-1)*9)
            elif 195 < x < 345 and 370 < y < 520:
                self.set_selected(1+(self.page-1)*9)
            elif 370 < x < 520 and 370 < y < 520:
                self.set_selected(2+(self.page-1)*9)
            elif 20 < x < 170 and 195 < y < 345:
                self.set_selected(3+(self.page-1)*9)
            elif 195 < x < 345 and 195 < y < 345:
                self.set_selected(4+(self.page-1)*9)
            elif 370 < x < 520 and 195 < y < 345:
                self.set_selected(5+(self.page-1)*9)
            elif 20 < x < 170 and 20 < y < 170:
                self.set_selected(6+(self.page-1)*9)
            elif 195 < x < 345 and 20 < y < 170:
                self.set_selected(7+(self.page-1)*9)
            elif 370 < x < 520 and 20 < y < 170:
                self.set_selected(8+(self.page-1)*9)



    def on_mouse_release(self, x, y, button, key_modifiers):
        pass


def main():
    window = MyGame(width, height, 'Bootleg Pokemon')
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
