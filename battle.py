import pokemon
import random
from arcade.gui import *
import time
import item
from typing import *
from loz import Player


class Enemy(arcade.Sprite):
    """Enemy class
        Attributes:
            wild(bool) = Whether enemy is wild pokemon or not
            left(int) = x coordinate for enemy left
            bottom(int) = y coordinate for enemy bottom
            dir(int) = direction of enemy(0=up, 1=right, 2=down, 3=left)
            pokemon(List["Pokemon"]) = Pokemon the enemy has (only 1 for wild)
        """
    def __init__(self, wild: bool, poke: List["pokemon.Pokemon"],
                 dir: int=0, boss: bool=False):
        super().__init__()
        self.wild = wild
        self.dir = dir
        self.pokemon = poke
        self.boss = boss
        self.check_dir()

    def check_dir(self) -> None:
        """Check enemy director and change image"""
        if self.boss:
            self.texture = arcade.load_texture(
                ":resources:images/alien/alienBlue_front.png")
        if not self.wild and not self.boss:
            if self.dir == 0:
                self.texture = arcade.load_texture(
                    ":resources:images/alien/alienBlue_climb1.png", scale=0.4)
            elif self.dir == 1:
                self.texture = arcade.load_texture(
                    ":resources:images/alien/alienBlue_walk2.png", scale=0.4)
            elif self.dir == 2:
                self.texture = arcade.load_texture(
                    ":resources:images/alien/alienBlue_front.png", scale=0.4)
            elif self.dir == 3:
                self.texture = arcade.load_texture(
                    ":resources:images/alien/alienBlue_walk2.png",
                    mirrored=True, scale=0.4)

    def see_player(self, game: "arcade.Window", player: "Player") -> None:
        """Check encounter between player and enemy"""
        if not self.defeated():
            if self.boss:
                if (abs(self.center_y - player.center_y) < 196 and
                        abs(self.center_x - player.center_x) < 196):
                    setup(game, player, self)
            if self.dir == 2:
                if (-32 < self.center_y - player.center_y < 256 and
                        abs(self.center_x-player.center_x) < 64):
                    setup(game, player, self)
            elif self.dir == 0:
                if (-256 < self.center_y - player.center_y < 32 and
                        abs(self.center_x-player.center_x) < 64):
                    setup(game, player, self)
            elif self.dir == 3:
                if (-32 < self.center_x - player.center_x < 256 and
                        abs(self.center_y-player.center_y) < 64):
                    setup(game, player, self)
            elif self.dir == 1:
                if (-256 < self.center_x - player.center_x < 32 and
                        abs(self.center_y-player.center_y) < 64):
                    setup(game, player, self)

    def defeated(self) -> bool:
        """Check whether enemy is defeated or not"""
        for poke in self.pokemon:
            if not poke.is_dead():
                return False
        else:
            return True


class actionButton(TextButton):
    """Inheritance of arcade built in Text Button"""
    def __init__(self, game: "arcade.Window", x: int=0, y: int=0,
                 width: int=100, height: int=40, text: str="Play",
                 theme: "arcade.Theme"=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self) -> None:
        self.pressed = True

    def on_release(self) -> None:
        if self.pressed:
            self.game.battle_msg = []
            self.game.battle_action = self.text
            self.pressed = False


class moveButton(TextButton):
    """Inheritance of arcade built in Text Button"""
    def __init__(self, game: "arcade.Window", x: int=0, y: int=0,
                 width: int=100, height: int=40, move: "pokemon.Move"=None,
                 theme: "arcade.Theme"=None):
        super().__init__(x, y, width, height,
                         f"{move.get_name()}({move.get_cur_pp()})",
                         theme=theme)
        self.move = move
        self.game = game

    def on_press(self) -> None:
        if self.move.check_pp():
            self.pressed = True

    def on_release(self) -> None:
        if self.pressed:
            self.game.battle_move = self.move
            self.pressed = False


class switchButton(TextButton):
    """Inheritance of arcade built in Text Button"""
    def __init__(self, game: "arcade.Window", x: int=0, y: int=0,
                 width: int=100, height: int=40, poke: "pokemon.Pokemon"=None,
                 theme: "arcade.Theme"=None):
        super().__init__(x, y, width, height,
                         f"{poke.name}({poke.cur_stats[0]}/{poke.stats[0]})",
                         theme=theme)
        self.poke = poke
        self.game = game

    def on_press(self) -> None:
        if not self.poke.is_dead():
            self.pressed = True

    def on_release(self) -> None:
        if self.pressed:
            self.game.battle_switchto = self.poke
            self.pressed = False


class bagButton(TextButton):
    """Inheritance of arcade built in Text Button"""
    def __init__(self, game: "arcade.Window", x: int=0, y: int=0,
                 width: int=100, height: int=40, text: str=None,
                 theme: "arcade.Window"=None, bag: List["item.Item"]=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game
        self.bag = bag

    def on_press(self) -> None:
        self.pressed = True

    def on_release(self) -> None:
        if self.pressed:
            self.game.battle_bag = self.bag
            self.pressed = False


class itemButton(TextButton):
    """Inheritance of arcade built in Text Button"""
    def __init__(self, game: "arcade.Window", x: int=0, y: int=0,
                 width: int=100, height: int=40, item: "item.Item"=None,
                 theme: "arcade.Theme"=None):
        super().__init__(x, y, width, height, f"{item.name}({item.amount})",
                         theme=theme)
        self.game = game
        self.item = item

    def on_press(self) -> None:
        if self.item.amount >= 1:
            self.pressed = True

    def on_release(self) -> None:
        if self.pressed:
            self.game.battle_item = self.item
            self.pressed = False


class backButton(TextButton):
    """Inheritance of arcade built in Text Button"""
    def __init__(self, game: "arcade.Window", x: int=0, y: int=0,
                 width: int=100, height: int=40, text: str="Back",
                 theme: "arcade.Theme"=None, backto: str="action"):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game
        self.backto = backto

    def on_press(self) -> None:
        self.pressed = True

    def on_release(self) -> None:
        if self.pressed:
            if self.backto == "action":
                action_buttons(self.game)
            elif self.backto == "bag":
                bag_buttons(self.game)
            self.pressed = False


def set_button_textures(game: "arcade.Window") -> None:
    """Set up textures for buttons"""
    normal = ":resources:gui_themes/Fantasy/Buttons/Normal.png"
    hover = ":resources:gui_themes/Fantasy/Buttons/Hover.png"
    clicked = ":resources:gui_themes/Fantasy/Buttons/Clicked.png"
    locked = ":resources:gui_themes/Fantasy/Buttons/Locked.png"
    game.battle_theme.add_button_textures(normal, hover, clicked, locked)


def setup_theme(game: "arcade.Window") -> None:
    """Set up theme for buttons"""
    game.battle_theme = Theme()
    game.battle_theme.set_font(24, arcade.color.WHITE)
    set_button_textures(game)


def display_pokemon(game: "arcade.Window") -> None:
    """Display pokemon name and hp on screen"""
    poke = game.battle_player.poke
    arcade.draw_xywh_rectangle_filled(125, poke.top + 30, 150, 8,
                                      arcade.color.RED)
    arcade.draw_xywh_rectangle_filled(125, poke.top + 30,
                                      150*(poke.cur_stats[0]/poke.stats[0]),
                                      8, arcade.color.GREEN)
    arcade.draw_text(f"{poke.name} lvl: {poke.lvl}", 125, poke.top + 60,
                     arcade.color.BLACK)
    arcade.draw_text(f"hp: {poke.cur_stats[0]}/{poke.stats[0]}", 125,
                     poke.top + 45, arcade.color.BLACK)

    enemy = game.battle_enemy.pokemon[game.battle_enemy.j]
    arcade.draw_xywh_rectangle_filled(525, enemy.bottom - 30, 150, 8,
                                      arcade.color.RED)
    arcade.draw_xywh_rectangle_filled(525, enemy.bottom - 30,
                                      150*(enemy.cur_stats[0]/enemy.stats[0]),
                                      8, arcade.color.GREEN)
    arcade.draw_text(f"{enemy.name} lvl: {enemy.lvl}", 525, enemy.bottom - 45,
                     arcade.color.BLACK)
    arcade.draw_text(f"hp: {enemy.cur_stats[0]}/{enemy.stats[0]}", 525,
                     enemy.bottom - 60, arcade.color.BLACK)


def action_buttons(game: "arcade.Window") -> None:
    """Set up buttons for action"""
    game.battle_action = None
    game.battle_button_list = []
    game.battle_button_list.append(actionButton(game, game.width / 2 - 96, 115,
                                   192, 70, "Fight", game.battle_theme))
    game.battle_button_list.append(actionButton(game, game.width / 2 + 96, 115,
                                   192, 70, "Switch", game.battle_theme))
    game.battle_button_list.append(actionButton(game, game.width / 2 - 96, 40,
                                   192, 70, "Bag", game.battle_theme))
    game.battle_button_list.append(actionButton(game, game.width / 2 + 96, 40,
                                   192, 70, "Run", game.battle_theme))
    game.battle_button_set = "action"


def move_buttons(game: "arcade.Window") -> None:
    """Set up buttons for pokemon moves"""
    game.battle_move = None
    game.battle_button_list = []
    poke = game.battle_player.poke
    for i in range(len(poke.moves)):
        game.battle_button_list.append(
            moveButton(game, game.width / 2 - 96 + (i % 2) * 192,
                       115 - (i // 2) * 75, 192, 70, poke.moves[i],
                       game.battle_theme))
    game.battle_button_list.append(backButton(game, game.width / 2 + 288, 40,
                                              192, 70,
                                              theme=game.battle_theme))
    game.battle_button_set = "move"


def switch_buttons(game: "arcade.Window") -> None:
    """Set up buttons for switching pokemon"""
    theme = Theme()
    theme.set_font(15, arcade.color.WHITE)
    set_button_textures(game)
    normal = ":resources:gui_themes/Fantasy/Buttons/Normal.png"
    hover = ":resources:gui_themes/Fantasy/Buttons/Hover.png"
    clicked = ":resources:gui_themes/Fantasy/Buttons/Clicked.png"
    locked = ":resources:gui_themes/Fantasy/Buttons/Locked.png"
    theme.add_button_textures(normal, hover, clicked, locked)

    game.battle_switchto = None
    game.battle_button_list = []
    for i in range(len(game.battle_player.pokemon)):
        game.battle_button_list.append(
            switchButton(game, game.width / 2 - 288 + (i % 3) * 192,
                         115 - (i // 3) * 75, 192, 70,
                         game.battle_player.pokemon[i], theme))
    game.battle_button_list.append(backButton(game, game.width / 2 + 288, 40,
                                   192, 70, theme=game.battle_theme))
    game.battle_button_set = "switch"


def bag_buttons(game: "arcade.Window") -> None:
    """Set up buttons for bag"""
    game.battle_bag = None
    game.battle_button_list = []
    game.battle_button_list.append(
        bagButton(game, game.width / 2 - 96, 115, 192, 70, "ball",
                  game.battle_theme, game.battle_player.item_bag[0]))
    game.battle_button_list.append(
        bagButton(game, game.width / 2 + 96, 115, 192, 70, "buff",
                  game.battle_theme, game.battle_player.item_bag[1]))
    game.battle_button_list.append(
        bagButton(game, game.width / 2 - 96, 40, 192, 70, "heal",
                  game.battle_theme, game.battle_player.item_bag[2]))
    game.battle_button_list.append(backButton(game, game.width / 2 + 288, 40,
                                   192, 70, theme=game.battle_theme))
    game.battle_button_set = "bag"


def item_buttons(game: "arcade.Window") -> None:
    """Set up buttons for items in bag"""
    game.battle_item = None
    game.battle_button_list = []
    for i in range(len(game.battle_bag)):
        game.battle_button_list.append(
            itemButton(game, game.width / 2 - 96 + (i % 2) * 192,
                       115 - (i // 2) * 75, 192, 70, game.battle_bag[i],
                       game.battle_theme))
    game.battle_button_list.append(
        backButton(game, game.width / 2 + 288, 40, 192, 70,
                   theme=game.battle_theme, backto="bag"))
    game.battle_button_set = "item"


def setup(game: "arcade.Window", player: "Player", enemy: "Enemy") -> None:
    """Set up the battle player and enemy"""
    game.cur_screen = "battle"
    game.battle_caught = False
    setup_theme(game)
    action_buttons(game)
    game.battle_player = player
    game.battle_enemy = enemy
    game.battle_msg = []

    game.battle_player_x = 200
    game.battle_player_y = 300
    game.battle_enemy_x = 600
    game.battle_enemy_y = 450

    game.battle_enemy.j = 0
    for poke in game.battle_player.pokemon:
        if not poke.is_dead():
            game.battle_player.poke = poke
            break
    game.battle_enemy.poke = game.battle_enemy.pokemon[0]
    game.battle_pokemon_list = arcade.SpriteList()

    game.battle_pokemon_list.append(game.battle_player.poke)
    game.battle_player.poke.center_x = game.battle_player_x
    game.battle_player.poke.center_y = game.battle_player_y
    game.battle_pokemon_list.append(game.battle_enemy.poke)
    game.battle_enemy.poke.center_x = game.battle_enemy_x
    game.battle_enemy.poke.center_y = game.battle_enemy_y


def on_draw(game: "arcade.Window") -> None:
    """Display info on screen"""
    arcade.start_render()
    bg = arcade.load_texture("images/battle_background.jpg")
    arcade.draw_texture_rectangle(game.width / 2, (game.height + 150) / 2,
                                  game.width, game.height - 150, bg)
    for button in game.battle_button_list:
        button.draw()

    game.battle_pokemon_list.draw()
    display_pokemon(game)

    for i in range(len(game.battle_msg)):
        arcade.draw_text(game.battle_msg[i], 350, 250 - i * 20,
                         arcade.color.WHITE_SMOKE)

    if game.battle_enemy.defeated():
        arcade.draw_text("You won!", 350, 240 - len(game.battle_msg) * 20-10,
                         arcade.color.WHITE, 30)
    elif game.battle_player.defeated():
        arcade.draw_text("You lost!", 350, 240 - len(game.battle_msg) * 20-10,
                         arcade.color.WHITE, 30)


def exit_battle(game: "arcade.Window") -> None:
    """Reset pokemon stats change (except hp) and return to game screen"""
    for poke in game.battle_player.pokemon:
        poke.cur_stats[1] = poke.stats[1]
        poke.cur_stats[2] = poke.stats[2]
        poke.cur_stats[3] = poke.stats[3]
        poke.effect = None
    game.cur_screen = "game"


def update(game: "arcade.Window") -> None:
    """Logic for battle"""
    if game.battle_player.defeated():
        exit_battle(game)
        time.sleep(1)
        return

    elif game.battle_enemy.defeated():
        exit_battle(game)
        time.sleep(1)
        return

    elif game.battle_caught:
        exit_battle(game)
        time.sleep(1)
        return

    if game.battle_player.poke.is_dead():
        game.battle_action = "Switch"
        game.battle_msg = [f"{game.battle_player.poke.name} is dead"]

    elif game.battle_enemy.pokemon[game.battle_enemy.j].is_dead():
        game.battle_pokemon_list.remove(game.battle_enemy.poke)
        game.battle_enemy.j += 1
        game.battle_enemy.poke = game.battle_enemy.pokemon[game.battle_enemy.j]
        game.battle_pokemon_list.append(game.battle_enemy.poke)
        game.battle_enemy.poke.center_x = game.battle_enemy_x
        game.battle_enemy.poke.center_y = game.battle_enemy_y
        game.battle_msg.append(f"enemy switch to \
{game.battle_enemy.pokemon[game.battle_enemy.j].name}")

    if game.battle_action == "Fight":

        if game.battle_button_set != "move":
            move_buttons(game)

        if game.battle_move is not None:
            fight(game.battle_player.poke,
                  game.battle_enemy.pokemon[game.battle_enemy.j],
                  game.battle_move, game)
            action_buttons(game)
            game.battle_move = None

    elif game.battle_action == "Switch":

        if game.battle_button_set != "switch":
            switch_buttons(game)

        if (game.battle_switchto is not None and
                game.battle_switchto != game.battle_player.poke):
            game.battle_pokemon_list.remove(game.battle_player.poke)
            game.battle_player.poke = game.battle_switchto
            game.battle_pokemon_list.append(game.battle_player.poke)
            game.battle_player.poke.center_x = game.battle_player_x
            game.battle_player.poke.center_y = game.battle_player_y
            action_buttons(game)
            game.battle_switchto = None
            move = game.battle_enemy.poke.moves[
                random.randrange(len(game.battle_enemy.poke.moves))]
            game.battle_enemy.poke.attack(game.battle_player.poke, move, game)

    elif game.battle_action == "Bag":

        if (game.battle_button_set != "bag" and
                game.battle_button_set != "item"):
            bag_buttons(game)

        if game.battle_bag is not None and game.battle_button_set != "item":
            item_buttons(game)

        if game.battle_item is not None:
            game.battle_msg.append(f"You used {game.battle_item.name}")
            if type(game.battle_item) == item.PokeBall:
                if game.battle_enemy.wild:
                    game.battle_item.ball_use(game, game.battle_enemy.poke)
                else:
                    game.battle_msg.append("not wild pokemon")

            else:
                game.battle_item.use(game, game.battle_player.poke)
            game.battle_bag = None
            game.battle_item = None
            action_buttons(game)

            if not game.battle_caught:
                move = game.battle_enemy.poke.moves[
                    random.randrange(len(game.battle_enemy.poke.moves))]
                game.battle_enemy.poke.attack(game.battle_player.poke, move,
                                              game)
    elif game.battle_action == "Run":
        if game.battle_enemy.wild:
            if random.randrange(2) == 0:
                game.battle_msg.append("you ran")
                exit_battle(game)
                return

            else:
                game.battle_msg.append("you failed to run away")
                game.battle_action = None
                move = game.battle_enemy.poke.moves[
                    random.randrange(len(game.battle_enemy.poke.moves))]
                game.battle_enemy.poke.attack(game.battle_player.poke, move,
                                              game)


def avg_lvl(poke_list: List["pokemon.Pokemon"]) -> int:
    """Calculate the average level in a list of pokemon"""
    total = 0
    for poke in poke_list:
        total += poke.lvl
    avg = round(total/len(poke_list))

    return avg


def wild_encounter(game: "arcade.Window") -> None:
    """Randomize pokemon when encounter a wild pokemon"""
    enemy_poke = pokemon.Pokemon.random_poke()
    avg = avg_lvl(game.player_sprite.pokemon)
    if avg < 5:
        enemy_poke.addlevel(random.randrange(0, avg+5))
    else:
        enemy_poke.addlevel(random.randrange(avg-5, avg+5))
    enemy = Enemy(True, [enemy_poke])
    setup(game, game.player_sprite, enemy)


def move_first(poke: "pokemon.Pokemon", opp: "pokemon.Pokemon") -> bool:
    """Check whether player or enemy move first"""
    if poke.cur_stats[3] >= opp.cur_stats[3]:
        return True
    else:
        return False


def fight(poke: "pokemon.Pokemon", opp: "pokemon.Pokemon",
          move: "pokemon.Move", game: "arcade.Window") -> None:
    """Logic for fighting """
    if move_first(poke, opp):
        poke.attack(opp, move, game)
        if opp.is_dead():
            poke.gainkill(game)
            return
        opp.attack(poke, opp.moves[random.randrange(len(opp.moves))], game)
        if poke.is_dead():
            return
    else:
        opp.attack(poke, opp.moves[random.randrange(len(opp.moves))], game)
        if poke.is_dead():
            return
        poke.attack(opp, move, game)
        if opp.is_dead():
            poke.gainkill(game)


if __name__ == "__main__":
    pass
