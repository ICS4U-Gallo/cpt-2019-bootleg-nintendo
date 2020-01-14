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
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.game.move = move
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
        self.i = self.j = 0
        self.action = None
        self.move = None
        self.theme = None
        self.button_list = None

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

    def fight_buttons(self):
        self.button_list = []
        # (300, 115), (500, 115), (300, 40), (500, 40)
        self.button_list.append(actionButton(self, 300, 115, 200, 70, "Fight", self.theme))
        self.button_list.append(actionButton(self, 500, 115, 200, 70, "Switch", self.theme))
        self.button_list.append(actionButton(self, 300, 40, 200, 70, "Bag", self.theme))

    def move_buttons(self):
        self.button_list = []
        poke = self.player.pokemon[self.i]
        self.button_list.append(moveButton(self, 300, 115, 200, 70, poke.moves[0], self.theme))
        self.button_list.append(moveButton(self, 500, 115, 200, 70, poke.moves[1], self.theme))
        self.button_list.append(moveButton(self, 300, 40, 200, 70, poke.moves[2], self.theme))

    def setup(self):
        self.setup_theme()
        self.fight_buttons()

    def on_draw(self):
        arcade.start_render()
        bg = arcade.load_texture("images/battle_background.jpg")
        arcade.draw_texture_rectangle(settings.WIDTH/2, (settings.HEIGHT+150)/2,
                                      settings.WIDTH, settings.HEIGHT-150, bg)
        for button in self.button_list:
            button.draw()

    def update(self, delta_time):
        if self.action == "Fight":
            self.move_buttons()
            if self.move != None:
                fight(self.player.pokemon[self.i], self.enemy.pokemon[self.j], self.move)
                self.action = None
                self.move = None
        
        if self.player.defeated():
            print("p1 lost")
            return
        elif self.enemy.defeated():
            print("p1 won")
            return
        if self.player.pokemon[self.i].is_dead():
            self.i += 1
            print(f"p1 switch to {self.player.pokemon[self.i].name}")
        elif self.enemy.pokemon[self.j].is_dead():
            self.j += 1
            print(f"p2 switch to {self.enemy.pokemon[self.j].name}")

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
    poke3 = pokemon.Pokemon.Charmander()
    poke4 = pokemon.Pokemon.Bulbasaur()
    a.pokemon = [poke1, poke3]
    b.pokemon = [poke2, poke4]

    game = Battle(settings.WIDTH, settings.HEIGHT, "battle", a, b)
    game.setup()
    arcade.run()

    # print(*a.pokemon)
    # print(*b.pokemon)
    # battle(a, b)
    # print(*a.pokemon)
    # print(*b.pokemon)
