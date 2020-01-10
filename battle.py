import arcade
import settings
import pokemon
import random


class Player:
    def __init__():
        self.pokemon = []

    def defeated():
        for poke in self.pokemon:
            if poke.cur_stats[0] > 0:
                return False
        return True


a = Player()
b = Player()
poke1 = pokemon.Pokemon.Magikarp()
poke2 = pokemon.Pokemon.IceCream()
a.pokemon = [poke1, poke1]
b.pokemon = [poke2, poke2]


def battle(player, opp):
    i = j = 0
    while opp not deafeated() and player not defeated():
        action(player, opp)


def action(player, opp, i, j):
    if option == "fight":
        fight(player1.pokemon[i], player2.pokemon[j])
    elif option == "switch":
        i = 1
    elif option == "item":
        pass


def check_first(poke, opp):
    if poke.stats[3] >= opp.stats[3]:
        return 0
    else:
        return 1


def choose_move(poke):
    # move_num = int(input("move# :"))
    move = poke.moves[0]
    return move


def fight(poke, opp):
    turn = check_first(poke, opp)
    for i in range(2):
        if turn % 2 == 0:
            move = choose_move(poke)
            poke.attack(opp, move)
            if opp.is_dead():
                print(f"\n{opp.name} is dead")
                break
        else:
            rng = random.randrange(len(opp.moves))
            move = opp.moves[rng]
            opp.attack(poke, move)
            if poke.is_dead():
                print(f"\n{poke.name} is dead")
                break
        turn += 1


class BattleView(arcade.View):
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
    while not poke1.is_dead() and not poke2.is_dead():
        fight(poke1, poke2)
    print(poke1)
    print(poke2)