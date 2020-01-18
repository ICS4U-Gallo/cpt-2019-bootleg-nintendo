import arcade
import loz
import pokemon
import random
import math

width = 768
height = 640

def search_for(poke_list, target):
    for i, poke in enumerate(poke_list):
        if target == poke:
            return i

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        self.p = loz.Player()
        self.selected = None
        self.switch_pos = False
        self.switched = False

        for i in range(6):
            poke = pokemon.Pokemon.random_poke()
            poke.addlevel(random.randrange(1,50))
            self.p.pokemon.append(poke)


    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Pokemon", width/2, height-20, arcade.color.BLACK, 40, align="center",
                         anchor_x="center", anchor_y="center")


        for i in range(len(self.p.pokemon)):
            self.p.pokemon[i].center_x = 125 + i % 2 * 175
            self.p.pokemon[i].center_y = 445 - i // 2 * 175
            self.p.pokemon[i].draw()

        for i in range(6):
            arcade.draw_xywh_rectangle_outline(50+i%2*175, 370-i//2 * 175, 150, 150, arcade.color.BLACK, 2)

        if self.selected != None:
            arcade.draw_text(self.selected.name, 440, 480, arcade.color.BLACK, 20)
            arcade.draw_text(f"# {self.selected.num}", 440, 460, arcade.color.BLACK, 20)
            arcade.draw_text(f"lvl: {self.selected.lvl}", 440, 440, arcade.color.BLACK, 20)
            arcade.draw_text(f"hp: {self.selected.cur_stats[0]} / {self.selected.stats[0]}", 440, 420, arcade.color.BLACK, 20)
            arcade.draw_text(f"atk: {self.selected.stats[1]}", 440, 400, arcade.color.BLACK, 20)
            arcade.draw_text(f"def: {self.selected.stats[2]}", 440, 380, arcade.color.BLACK, 20)
            arcade.draw_text(f"spd: {self.selected.stats[3]}", 440, 360, arcade.color.BLACK, 20)

            arcade.draw_xywh_rectangle_outline(440, 270, 200, 50, arcade.color.BLACK, 3)
            arcade.draw_text("switch", 540, 295, arcade.color.BLACK, 25, align="center", anchor_x="center",
                             anchor_y="center")
            arcade.draw_xywh_rectangle_outline(440, 200, 200, 50, arcade.color.BLACK, 3)
            arcade.draw_text("send to storage", 540, 225, arcade.color.BLACK, 24, align="center", anchor_x="center",
                             anchor_y="center")
        else:
            arcade.draw_text("No Pokemon Selected", 440, 480, arcade.color.BLACK, 20)

        if self.switch_pos:
            arcade.draw_text("Switching", 440, 510, arcade.color.BLACK, 20)


    def on_key_press(self, key, modifiers):
        pass

    def on_key_release(self, key, modifiers):
        pass

    def update(self, delta_time):
        pass

    def set_selected(self, num):
        try:
            self.selected = self.p.pokemon[num]
        except IndexError:
            self.selected = None

    def click_on_pokemon(self, x, y):
        if 20 < x < 170 and 370 < y < 520:
            self.set_selected(0)
        elif 195 < x < 345 and 370 < y < 520:
            self.set_selected(1)
        elif 20 < x < 170 and 195 < y < 345:
            self.set_selected(2)
        elif 195 < x < 345 and 195 < y < 345:
            self.set_selected(3)
        elif 20 < x < 170 and 20 < y < 170:
            self.set_selected(4)
        elif 195 < x < 345 and 20 < y < 170:
            self.set_selected(5)
        if self.switch_pos:
            self.switched = True

    def on_mouse_press(self, x, y, button, key_modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.click_on_pokemon(x, y)
            if self.selected != None:
                if 400 < x < 600 and 270 < y < 320:
                    self.switch_pos = True
                    self.switch_from = self.selected
                elif 400 < x < 600 and 200 < y < 250:
                    self.p.pokemon.remove(self.selected)
                    self.p.pokemon_storage.append(self.selected)
            if self.switch_pos:
                if self.switched:
                    j = search_for(self.p.pokemon, self.selected)
                    self.p.pokemon[search_for(self.p.pokemon, self.switch_from)], self.p.pokemon[j] = self.selected, self.switch_from
                    self.switch_pos = False
                    self.switched = False





    def on_mouse_release(self, x, y, button, key_modifiers):
        pass


def main():
    window = MyGame(width, height, 'Bootleg Pokemon')
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
