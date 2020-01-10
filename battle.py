import arcade
import settings
import pokemon
import random


class Player:
    def __init__(self):
        self.pokemon = []

    def not_defeated(self):
        print(self.pokemon)
        for poke in self.pokemon:
            if poke.cur_stats[0] > 0:
                return True
        return False


a = Player()
b = Player()
poke1 = pokemon.Pokemon.Magikarp()
poke2 = pokemon.Pokemon.IceCream()
poke3 = pokemon.Pokemon.Charmander()
poke4 = pokemon.Pokemon.Bulbasaur()
a.pokemon = [poke1, poke3]
b.pokemon = [poke2, poke4]


def battle(p1, p2):
    i = j = 0
    while p1.not_defeated() and p2.not_defeated():
        action(p1, p2, i, j)


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
    move = poke.moves[0]
    return move


def fight(poke, opp, move):
    if move_first(poke, opp):
        poke.attack(opp, move)
        opp.check_dead()
        opp.attack(poke, opp.moves[random.randrange(len(opp.moves))])
        poke.check_dead()
    else:
        opp.attack(poke, opp.moves[random.randrange(len(opp.moves))])
        poke.check_dead()
        poke.attack(opp, move)
        opp.check_dead()


class Battle(arcade.Window):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        bg = arcade.load_texture("images/battle_background.jpg")
        arcade.draw_texture_rectangle(settings.WIDTH // 2,
                                      settings.HEIGHT // 2,
                                      settings.WIDTH, settings.HEIGHT, bg
                                      )

    def on_key_press(self, key, modifiers):
        pass


if __name__ == "__main__":
    # from utils import FakeDirector
    # window = arcade.Window(settings.WIDTH, settings.HEIGHT)
    # my_view = BattleView()
    # my_view.director = FakeDirector(close_on_next_view=True)
    # window.show_view(my_view)
    # arcade.run()
    print(poke1)
    print(poke2)
    # while not poke1.check_dead() and not poke2.check_dead():
    #     move = poke1.moves[0]
    #     fight(poke1, poke2, move)
    battle(a, b)
    print(poke1)
    print(poke2)
