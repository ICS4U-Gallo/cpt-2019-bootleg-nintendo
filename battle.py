import settings
import pokemon
import random
from arcade.gui import *
import os


class Player:
    def __init__(self):
        self.pokemon = []

    def defeated(self):
        for poke in self.pokemon:
            if not poke.is_dead():
                return False
        else:
            return True


def battle(p1, p2):
    i = j = 0
    print("Hello World")
    while True:
        action(p1, p2, i, j)
        if p1.defeated():
            print("p1 lost")
            break
        elif p2.defeated():
            print("p1 won")
            break
        if p1.pokemon[i].is_dead():
            i += 1
            print(f"p1 switch to {p1.pokemon[i].name}")
        elif p2.pokemon[j].is_dead():
            j += 1
            print(f"p2 switch to {p2.pokemon[j].name}")
    else:
        pass


def action(p1, p2, i, j):
    option = "fight"
    if option == "fight":
        move = choose_move(p1.pokemon[i])
        fight(p1.pokemon[i], p2.pokemon[j], move)
    elif option == "switch":
        i = 1
        opp = p2.pokemon[j]
        opp.attack(poke, opp.moves[random.randrange(len(opp.moves))])
    elif option == "item":
        pass


def move_first(poke, opp):
    if poke.stats[3] >= opp.stats[3]:
        return True
    else:
        return False


def choose_move(poke):
    move_num = int(input("move# :"))
    move = poke.moves[move_num]
    return move


def fight(poke, opp, move):
    if move_first(poke, opp):
        poke.attack(opp, move)
        if opp.is_dead():
            print(f"{opp.name} is dead")
            poke.gainkill()
            return
        opp.attack(poke, opp.moves[random.randrange(len(opp.moves))])
    else:
        opp.attack(poke, opp.moves[random.randrange(len(opp.moves))])
        if poke.is_dead():
            print(f"{poke.name} is dead")
            return
        poke.attack(opp, move)
        if opp.is_dead():
            print(f"{opp.name} is dead")
            poke.gainkill()


class actionButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="Play", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.game.action = self.text
            self.pressed = False


class moveButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, move=None, theme=None):
        super().__init__(x, y, width, height, move.name, theme=theme)
        self.move = move
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.game.move = self.move
            self.pressed = False


class switchButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, poke=None, theme=None):
        super().__init__(x, y, width, height, poke.name, theme=theme)
        self.poke = poke
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.game.switchto = self.poke
            self.pressed = False


class Battle(arcade.Window):
    def __init__(self, w, h, name, p1, p2):
        super().__init__(w, h, name)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        arcade.set_background_color(arcade.color.WHITE)
        self.player = p1
        self.enemy = p2
        self.action = None
        self.move = None
        self.switchto = None
        self.theme = None
        self.button = None
        self.button_list = None
        self.pokemon_list = None

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

    def display_pokemon(self):
        poke = self.player.poke
        arcade.draw_xywh_rectangle_filled(125, poke.top+30, 150, 8, arcade.color.RED)
        arcade.draw_xywh_rectangle_filled(125, poke.top+30, 150 * (poke.cur_stats[0]/poke.stats[0]), 8, arcade.color.GREEN)
        arcade.draw_text(f"{poke.name} lvl: {poke.lvl}", 125, poke.top+60, arcade.color.BLACK)
        arcade.draw_text(f"hp: {poke.cur_stats[0]}/{poke.stats[0]}", 125, poke.top+45, arcade.color.BLACK)

        enemy = self.enemy.pokemon[self.enemy.j]
        arcade.draw_xywh_rectangle_filled(525, enemy.bottom-30, 150, 8, arcade.color.RED)
        arcade.draw_xywh_rectangle_filled(525, enemy.bottom-30, 150 * (enemy.cur_stats[0]/enemy.stats[0]), 8, arcade.color.GREEN)
        arcade.draw_text(f"{enemy.name} lvl: {enemy.lvl}", 525, enemy.bottom-45, arcade.color.BLACK)
        arcade.draw_text(f"hp: {enemy.cur_stats[0]}/{enemy.stats[0]}", 525, enemy.bottom-60, arcade.color.BLACK)

    def action_buttons(self):
        self.action = None
        self.button_list = []
        # (300, 115), (500, 115), (300, 40), (500, 40)
        self.button_list.append(actionButton(self, 300, 115, 200, 70, "Fight", self.theme))
        self.button_list.append(actionButton(self, 500, 115, 200, 70, "Switch", self.theme))
        self.button_list.append(actionButton(self, 300, 40, 200, 70, "Bag", self.theme))
        self.button_set = "action"

    def move_buttons(self):
        self.button_list = []
        poke = self.player.poke
        for i in range(len(poke.moves)):
            self.button_list.append(moveButton(self, 300+(i%2)*200, 115-(i//2)*75, 200, 70, poke.moves[i], self.theme))
        self.button_set = "move"

    def switch_buttons(self):
        self.button_list = []
        for i in range(len(self.player.pokemon)):
            self.button_list.append(switchButton(self, 300+(i%3)*200, 115-(i//3)*75, 200, 70, self.player.pokemon[i], self.theme))
        self.button_set = "switch"

    def setup(self):
        self.setup_theme()
        self.action_buttons()

        self.player_x = 200
        self.player_y = 300
        self.enemy_x = 600
        self.enemy_y = 450

        self.enemy.j = 0
        self.player.poke = self.player.pokemon[0]
        self.enemy.poke = self.enemy.pokemon[0]
        self.pokemon_list = arcade.SpriteList()

        self.pokemon_list.append(self.player.poke)
        self.player.poke.center_x = self.player_x
        self.player.poke.center_y = self.player_y
        self.pokemon_list.append(self.enemy.poke)
        self.enemy.poke.center_x = self.enemy_x
        self.enemy.poke.center_y = self.enemy_y

    def on_draw(self):
        arcade.start_render()
        bg = arcade.load_texture("images/battle_background.jpg")
        arcade.draw_texture_rectangle(settings.WIDTH/2, (settings.HEIGHT+150)/2,
                                      settings.WIDTH, settings.HEIGHT-150, bg)
        for button in self.button_list:
            button.draw()

        self.pokemon_list.draw()
        self.display_pokemon()

    def update(self, delta_time):
        if self.player.defeated():
            print("p1 lost")
            return
        elif self.enemy.defeated():
            print("p1 won")
            return

        if self.action == "Fight":
            if self.button_set != "move":
                self.move_buttons()
            if self.move != None:
                fight(self.player.poke, self.enemy.pokemon[self.enemy.j], self.move)
                self.action_buttons()
                self.move = None
        elif self.action == "Switch":
            if self.button_set != "switch":
                self.switch_buttons()
            if self.switchto != None and self.switchto != self.player.poke:
                self.pokemon_list.remove(self.player.poke)
                for poke in self.pokemon_list:
                    print(poke)
                self.player.poke = self.switchto
                self.pokemon_list.append(self.player.poke)
                self.player.poke.center_x = self.player_x
                self.player.poke.center_y = self.player_y
                self.action_buttons()
                self.switchto = None
                move = self.enemy.poke.moves[random.randrange(len(self.enemy.poke.moves))]
                self.enemy.poke.attack(self.player.poke, move)
            
        if self.player.poke.is_dead():
            self.action = "Switch"
        elif self.enemy.pokemon[self.enemy.j].is_dead():
            self.pokemon_list.remove(self.enemy.poke)
            self.enemy.j += 1
            self.enemy.poke = self.enemy.pokemon[self.enemy.j]
            self.pokemon_list.append(self.enemy.poke)
            self.enemy.poke.center_x = self.enemy_x
            self.enemy.poke.center_y = self.enemy_y
            print(f"p2 switch to {self.enemy.pokemon[self.enemy.j].name}")

if __name__ == "__main__":
    # from utils import FakeDirector
    # window = arcade.Window(settings.WIDTH, settings.HEIGHT)
    # my_view = BattleView()
    # my_view.director = FakeDirector(close_on_next_view=True)
    # window.show_view(my_view)
    a = Player()
    b = Player()
    poke1 = pokemon.Pokemon.Magikarp()
    poke1.addlevel(4)
    poke2 = pokemon.Pokemon.IceCream()
    poke2.addlevel(4)
    poke3 = pokemon.Pokemon.Charmander()
    poke3.addlevel(4)
    poke4 = pokemon.Pokemon.Bulbasaur()
    poke4.addlevel(4)
    poke5 = pokemon.Pokemon.Squirtle()
    poke5.addlevel(4)
    a.pokemon = [poke1, poke3, poke5]
    b.pokemon = [poke2, poke4]

    game = Battle(settings.WIDTH, settings.HEIGHT, "battle", a, b)
    game.setup()
    arcade.run()

    # print(*a.pokemon)
    # print(*b.pokemon)
    # battle(a, b)
    # print(*a.pokemon)
    # print(*b.pokemon)
