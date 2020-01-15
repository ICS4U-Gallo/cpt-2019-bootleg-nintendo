import settings
import pokemon
import random
from arcade.gui import *
import os
import loz

class Player:
    def __init__(self):
        self.pokemon = []

    def defeated(self):
        for poke in self.pokemon:
            if not poke.is_dead():
                return False
        else:
            return True

class Enemy:
    def __init__(self, wild, *poke):
        self.wild = wild
        self.pokemon = [*poke]

    def defeated(self):
        for poke in self.pokemon:
            if not poke.is_dead():
                return False
        else:
            return True

def wild_encounter(game):
    enemy_poke = pokemon.poke_list[random.randrange(len(pokemon.poke_list)-1)]
    enemy_poke.addlevel(random.randrange(2,7))
    enemy = Enemy(True, enemy_poke)
    setup(game, game.player_sprite, enemy)


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
            self.game.battle_action = self.text
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
            self.game.battle_move = self.move
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
            self.game.battle_switchto = self.poke
            self.pressed = False

class backButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="Back", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            action_buttons(self.game)
            self.pressed = False

# class Battle(arcade.Window):
#     def __init__(self, w, h, name, p1, p2):
#         super().__init__(w, h, name)
#
#         # Set the working directory (where we expect to find files) to the same
#         # directory this .py file is in. You can leave this out of your own
#         # code, but it is needed to easily run the examples using "python -m"
#         # as mentioned at the top of this program.
#         file_path = os.path.dirname(os.path.abspath(__file__))
#         os.chdir(file_path)
#
#         arcade.set_background_color(arcade.color.WHITE)
#         self.player = p1
#         self.enemy = p2
#         self.action = None
#         self.move = None
#         self.switchto = None
#         self.theme = None
#         self.button = None
#         self.button_list = None
#         self.pokemon_list = None


def set_button_textures(game):
    normal = ":resources:gui_themes/Fantasy/Buttons/Normal.png"
    hover = ":resources:gui_themes/Fantasy/Buttons/Hover.png"
    clicked = ":resources:gui_themes/Fantasy/Buttons/Clicked.png"
    locked = ":resources:gui_themes/Fantasy/Buttons/Locked.png"
    game.battle_theme.add_button_textures(normal, hover, clicked, locked)


def setup_theme(game):
    game.battle_theme = Theme()
    game.battle_theme.set_font(24, arcade.color.WHITE)
    set_button_textures(game)


def display_pokemon(game):
    poke = game.battle_player.poke
    arcade.draw_xywh_rectangle_filled(125, poke.top+30, 150, 8, arcade.color.RED)
    arcade.draw_xywh_rectangle_filled(125, poke.top+30, 150 * (poke.cur_stats[0]/poke.stats[0]), 8, arcade.color.GREEN)
    arcade.draw_text(f"{poke.name} lvl: {poke.lvl}", 125, poke.top+60, arcade.color.BLACK)
    arcade.draw_text(f"hp: {poke.cur_stats[0]}/{poke.stats[0]}", 125, poke.top+45, arcade.color.BLACK)

    enemy = game.battle_enemy.pokemon[game.battle_enemy.j]
    arcade.draw_xywh_rectangle_filled(525, enemy.bottom-30, 150, 8, arcade.color.RED)
    arcade.draw_xywh_rectangle_filled(525, enemy.bottom-30, 150 * (enemy.cur_stats[0]/enemy.stats[0]), 8, arcade.color.GREEN)
    arcade.draw_text(f"{enemy.name} lvl: {enemy.lvl}", 525, enemy.bottom-45, arcade.color.BLACK)
    arcade.draw_text(f"hp: {enemy.cur_stats[0]}/{enemy.stats[0]}", 525, enemy.bottom-60, arcade.color.BLACK)


def action_buttons(game):
    game.battle_action = None
    game.battle_button_list = []
    # (300, 115), (500, 115), (300, 40), (500, 40)
    game.battle_button_list.append(actionButton(game, 300, 115, 200, 70, "Fight", game.battle_theme))
    game.battle_button_list.append(actionButton(game, 500, 115, 200, 70, "Switch", game.battle_theme))
    game.battle_button_list.append(actionButton(game, 300, 40, 200, 70, "Bag", game.battle_theme))
    game.battle_button_set = "action"


def move_buttons(game):
    game.battle_button_list = []
    poke = game.battle_player.poke
    for i in range(len(poke.moves)):
        game.battle_button_list.append(moveButton(game, 300+(i%2)*200, 115-(i//2)*75, 200, 70, poke.moves[i], game.battle_theme))
    game.battle_button_list.append(backButton(game, 700, 40, 200, 70, theme=game.battle_theme))
    game.battle_button_set = "move"


def switch_buttons(game):
    game.battle_button_list = []
    for i in range(len(game.battle_player.pokemon)):
        game.battle_button_list.append(switchButton(game, 100+(i%3)*200, 115-(i//3)*75, 200, 70, game.battle_player.pokemon[i], game.battle_theme))
    game.battle_button_list.append(backButton(game, 700, 40, 200, 70, theme=game.battle_theme))
    game.battle_button_set = "switch"


def setup(game, player, enemy):
    game.cur_screen = "battle"
    setup_theme(game)
    action_buttons(game)
    game.battle_player = player
    game.battle_enemy = enemy

    game.battle_player_x = 200
    game.battle_player_y = 300
    game.battle_enemy_x = 600
    game.battle_enemy_y = 450

    game.battle_enemy.j = 0
    game.battle_player.poke = game.battle_player.pokemon[0]
    game.battle_enemy.poke = game.battle_enemy.pokemon[0]
    game.battle_pokemon_list = arcade.SpriteList()

    game.battle_pokemon_list.append(game.battle_player.poke)
    game.battle_player.poke.center_x = game.battle_player_x
    game.battle_player.poke.center_y = game.battle_player_y
    game.battle_pokemon_list.append(game.battle_enemy.poke)
    game.battle_enemy.poke.center_x = game.battle_enemy_x
    game.battle_enemy.poke.center_y = game.battle_enemy_y


def on_draw(game):
    arcade.start_render()
    bg = arcade.load_texture("images/battle_background.jpg")
    arcade.draw_texture_rectangle(game.width/2, (game.height+150)/2,
                                  game.width, game.height-150, bg)
    for button in game.battle_button_list:
        button.draw()

    game.battle_pokemon_list.draw()
    display_pokemon(game)


def update(game):
    if game.battle_player.defeated():
        for poke in game.battle_player.pokemon:
            poke.cur_stats[1] = poke.stats[1]
            poke.cur_stats[2] = poke.stats[2]
        game.cur_screen = "game"
        return
    elif game.battle_enemy.defeated():
        for poke in game.battle_player.pokemon:
            poke.cur_stats[1] = poke.stats[1]
            poke.cur_stats[2] = poke.stats[2]
        game.cur_screen = "game"
        return
    if game.battle_player.poke.is_dead():
        game.battle_action = "Switch"
    elif game.battle_enemy.pokemon[game.battle_enemy.j].is_dead():
        game.battle_pokemon_list.remove(game.battle_enemy.poke)
        game.battle_enemy.j += 1
        game.battle_enemy.poke = game.battle_enemy.pokemon[game.battle_enemy.j]
        game.battle_pokemon_list.append(game.battle_emeny.poke)
        game.battle_enemy.poke.center_x = game.battle_enemy_x
        game.battle_enemy.poke.center_y = game.battle_enemy_y
        print(f"p2 switch to {game.battle_enemy.pokemon[game.battle_enemy.j].name}")

    if game.battle_action == "Fight":
        if game.battle_button_set != "move":
            move_buttons(game)
        if game.battle_move != None:
            fight(game.battle_player.poke, game.battle_enemy.pokemon[game.battle_enemy.j], game.battle_move)
            action_buttons(game)
            game.battle_move = None
    elif game.battle_action == "Switch":
        if game.battle_button_set != "switch":
            switch_buttons(game)
        if game.battle_switchto != None and game.battle_switchto != game.battle_player.poke:
            game.battle_pokemon_list.remove(game.battle_player.poke)
            for poke in game.battle_pokemon_list:
                print(poke)
            game.battle_player.poke = game.battle_switchto
            game.battle_pokemon_list.append(game.battle_player.poke)
            game.battle_player.poke.center_x = game.battle_player_x
            game.battle_player.poke.center_y = game.battle_player_y
            action_buttons(game)
            game.battle_switchto = None
            move = game.battle_enemy.poke.moves[random.randrange(len(game.battle_enemy.poke.moves))]
            game.battle_enemy.poke.attack(game.battle_player.poke, move)
            

if __name__ == "__main__":
    # from utils import FakeDirector
    # window = arcade.Window(settings.WIDTH, settings.HEIGHT)
    # my_view = BattleView()
    # my_view.director = FakeDirector(close_on_next_view=True)
    # window.show_view(my_view)
    a = loz.Player()
    b = loz.Player()
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
