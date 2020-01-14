import arcade
import settings
import pokemon
import random


class Player:
    def __init__(self):
        self.pokemon = []

    def defeated(self):
        for poke in self.pokemon:
            if not poke.is_dead():
                return False
        else:
            return True


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
            return
        opp.attack(poke, opp.moves[random.randrange(len(opp.moves))])
    else:
        opp.attack(poke, opp.moves[random.randrange(len(opp.moves))])
        if poke.is_dead():
            print(f"{poke.name} is dead")
            return
        poke.attack(opp, move)


class Battle(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background = None
        arcade.set_background_color(arcade.color.WHITE)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists here
        self.poke_list = arcade.SpriteList()
        self.opp_list = arcade.SpriteList()

        self.poke_sprite = arcade.Sprite("images/poke_images")
        self.poke_sprite.center_x = 25
        self.poke_sprite.center_y = 25
        self.poke_list.append(self.poke_sprite)

    def on_draw(self):
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame
        arcade.start_render()
        bg = arcade.load_texture("images/battle_background.jpg")
        arcade.draw_texture_rectangle(settings.WIDTH/2, settings.HEIGHT/2,
                                      settings.WIDTH, settings.HEIGHT, bg)
        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        pass

    def on_key_press(self, key, key_modifiers):
        pass

    def on_key_release(self, key, key_modifiers):
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        pass


if __name__ == "__main__":
    # from utils import FakeDirector
    # window = arcade.Window(settings.WIDTH, settings.HEIGHT)
    # my_view = BattleView()
    # my_view.director = FakeDirector(close_on_next_view=True)
    # window.show_view(my_view)
    game = Battle(settings.WIDTH, settings.HEIGHT, "battle")
    game.setup()
    arcade.run()

    print(*a.pokemon)
    print(*b.pokemon)
    battle(a, b)
    print(*a.pokemon)
    print(*b.pokemon)
