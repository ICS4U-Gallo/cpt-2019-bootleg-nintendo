import arcade.gui
import os
import math
import map
import battle
import bag
import item
import buffs
import heals
import pokemon
import pokedex
import menu_start
import menu_game
import balls
import pokeBag
import pokeStorage

sprite_scale = 0.5
other_scale = 0.4
native_sprite = 128
sprite_size = int(sprite_scale * native_sprite)

screen_width = sprite_size * 12
screen_height = sprite_size * 10
screen_title = "Hey, stop that"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
view_boundary_yaxis = 294
view_boundary_xaxis = 375

MOVEMENT_SPEED = 10
big_room_list = [0, 3, 4, 5]
small_room_list = [1, 2, 6]

tex_right = 1
tex_left = 0


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()

        # Load a left facing texture and a right facing texture.
        # mirrored=True will mirror the image we load.
        texture = arcade.load_texture("images/character.png",
                                      mirrored=True, scale=sprite_scale)
        self.textures.append(texture)
        texture = arcade.load_texture("images/character.png",
                                      scale=sprite_scale)
        self.textures.append(texture)

        # By default, face right.
        self.face_dir = 1
        # 0 = up, 1 = right, 2 = down, 3 = left
        self.set_texture(tex_right)

        self.pokemon = []
        self.item_bag = []
        self.pokemon_storage = []

    def update(self):

        # Figure out player facing direction
        if self.change_y < 0:
            self.face_dir = 2
        if self.change_y > 0:
            self.face_dir = 0
        if self.change_x < 0:
            self.face_dir = 3
            self.set_texture(tex_left)
        if self.change_x > 0:
            self.face_dir = 1
            self.set_texture(tex_right)

    def defeated(self):
        for poke in self.pokemon:
            if not poke.is_dead():
                return False
        else:
            return True

    def catch(self, game, poke):
        if len(self.pokemon) < 6:
            self.pokemon.append(poke)
            game.battle_msg.append(f"You caught {poke.name}")
            game.battle_msg.append(f"added {poke.name} to bag")
        else:
            self.pokemon_storage.append(poke)
            game.battle_msg.append(f"You caught {poke.name}")
            game.battle_msg.append(f"added {poke.name} to storage")


def check_mouse_press_for_buttons(x, y, button_list):
    for button in button_list:
        if x > button.center_x + button.width / 2:
            continue
        if x < button.center_x - button.width / 2:
            continue
        if y > button.center_y + button.height / 2:
            continue
        if y < button.center_y - button.height / 2:
            continue
        button.on_press()


def check_mouse_release_for_buttons(_x, _y, button_list):
    for button in button_list:
        if button.pressed:
            button.on_release()


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, antialiasing=False)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        arcade.set_background_color(arcade.color.WHITE)

        # Sprite lists
        self.cur_screen = None
        self.current_room = 1
        self.coin_list = None

        # Set up start menu
        self.start = None
        self.start_clock = None
        self.start_y = None
        self.load = None
        self.mouse_x = None
        self.mouse_y = None

        # Set up the player
        self.rooms = None
        self.player_sprite = None
        self.player_list = None
        self.physics_engine = None
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.act_pressed = False
        self.view_bottom = 0
        self.view_left = 0

        # Set up for battle
        self.battle_player = None
        self.battle_enemy = None
        self.battle_action = None
        self.battle_move = None
        self.battle_switchto = None
        self.battle_bag = None
        self.battle_item = None
        self.battle_theme = None
        self.battle_button = None
        self.battle_button_list = None
        self.battle_pokemon_list = None
        self.battle_msg = None
        self.battle_caught = False

        # Set up bag
        self.bag_button_list = None
        self._pointer = 0
        self.search_menu = False
        self.sort_menu = False
        self.search_number = ""
        self.search_letter = ""
        self.ball_list = [item.PokeBall.pokeball(),
                          item.PokeBall.greatball(),
                          item.PokeBall.masterball()]
        self.buff_list = [item.Item.steroids(),
                          item.Item.leg_day()]
        self.heal_list = [item.Item.potion(),
                          item.Item.superpotion()]
        self.poke_list = [pokemon.Pokemon.Charmander(),
                          pokemon.Pokemon.Charm2(),
                          pokemon.Pokemon.Squirtle(),
                          pokemon.Pokemon.Squir2(),
                          pokemon.Pokemon.Bulbasaur(),
                          pokemon.Pokemon.Bulb2(),
                          pokemon.Pokemon.IceCream(),
                          pokemon.Pokemon.Ice2(),
                          pokemon.Pokemon.Garbage(),
                          pokemon.Pokemon.Torkoal(),
                          pokemon.Pokemon.Klefki(),
                          pokemon.Pokemon.Magikarp(),
                          pokemon.Pokemon.PinkMagikarp()]

        # Set up Game menu
        self.select_x = 0
        self.select_y = 0
        self.dex_color = None
        self.bag_color = None
        self.save_color = None
        self.exit_color = None
        self.dex_sprite = None
        self.bag_sprite = None
        self.save_sprite = None
        self.exit_sprite = None

        # Pokemon Bag is the 6 pokemon being used
        # Pokemon Storage is the rest of the pokemon
        # Set up Pokemon Bag
        self.selected = None
        self.switch_pos = None
        self.switched = None

        # Set up Pokemon Storage
        self.sto_page = None
        self.sto_poke_list = None
        self.sto_selected = None
        self.sto_searching = False
        self.sto_search_number = None

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.cur_screen = "game"

        # Sprite lists
        self.player_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = Player()
        self.player_sprite.center_x = 250
        self.player_sprite.center_y = 400
        self.player_list.append(self.player_sprite)
        self.player_sprite.item_bag = [self.ball_list,
                                       self.buff_list,
                                       self.heal_list]

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

        bag.setup(self)
        menu_game.setup(self)
        pokeBag.setup(self)
        pokeStorage.setup(self)

        self.rooms = map.create()

        self.current_room = 1

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         (self.rooms
                                                          [self.
                                                           current_room].
                                                          wall_list))

    def get_pointer(self):
        return self._pointer

    def edit_pointer(self, value):
        self._pointer = value

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        if self.cur_screen == "start":
            menu_start.on_draw(self)
        elif self.cur_screen == "game":
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_texture_rectangle(screen_width,
                                          screen_height,
                                          screen_width * 2,
                                          screen_height * 2,
                                          self.rooms[self.current_room].
                                          background)
            self.rooms[self.current_room].wall_list.draw()
            self.player_list.draw()
            if self.current_room == 3:
                self.rooms[self.current_room].grass_list.draw()
            elif self.current_room == 5:
                self.rooms[self.current_room].enemy_list.draw()
            elif self.current_room == 2:
                self.rooms[self.current_room].pokeball.draw()
        elif self.cur_screen == "battle":
            battle.on_draw(self)
        elif self.cur_screen == "bag":
            bag.on_draw(self)
        elif self.cur_screen == "buff":
            buffs.on_draw(self)
        elif self.cur_screen == "balls":
            balls.on_draw(self)
        elif self.cur_screen == "heal":
            heals.on_draw(self)
        elif self.cur_screen == "game menu":
            menu_game.on_draw(self)
        elif self.cur_screen == "pokedex":
            pokedex.on_draw(self)
        elif self.cur_screen == "pokemon":
            pokeBag.on_draw(self)
        elif self.cur_screen == "pokebag":
            pokeStorage.on_draw(self)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if self.cur_screen == "game":
            if key == arcade.key.W:
                self.up_pressed = True
            elif key == arcade.key.S:
                self.down_pressed = True
            elif key == arcade.key.A:
                self.left_pressed = True
            elif key == arcade.key.D:
                self.right_pressed = True
            if key == arcade.key.L:
                self.act_pressed = True
            elif key == arcade.key.K:
                self.cur_screen = "game menu"
        elif self.cur_screen == "balls":
            balls.search_logic(self, key)
        elif self.cur_screen == "buff":
            buffs.search_logic(self, key)
        elif self.cur_screen == "heal":
            heals.search_logic(self, key)
        elif self.cur_screen == "game menu":
            menu_game.key_logic(self, key)
        elif self.cur_screen == "pokedex":
            pokedex.key_logic(self, key)
        elif self.cur_screen == "pokemon":
            pokeBag.key_logic(self, key)
        elif self.cur_screen == "pokebag":
            pokeStorage.key_logic(self, key)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.W:
            self.up_pressed = False
        elif key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.D:
            self.right_pressed = False
        if key == arcade.key.L:
            self.act_pressed = False

    def on_mouse_press(self, x, y, button, key_modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            if self.cur_screen == "start":
                menu_start.on_mouse_press(self, x, y, button)
            elif self.cur_screen == "battle":
                check_mouse_press_for_buttons(x, y, self.battle_button_list)
            elif self.cur_screen == "bag":
                check_mouse_press_for_buttons(x, y, self.bag_button_list)
            elif self.cur_screen == "pokemon":
                pokeBag.mouse_logic(self, x, y, button)
            elif self.cur_screen == "pokebag":
                pokeStorage.mouse_logic(self, x, y, button)
            if self.start is False:
                self.start = True
                self.cur_screen = "start"

    def on_mouse_release(self, x, y, button, key_modifiers):
        if self.cur_screen == "battle":
            check_mouse_release_for_buttons(x, y, self.battle_button_list)
        elif self.cur_screen == "bag":
            check_mouse_release_for_buttons(x, y, self.bag_button_list)

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_x = x
        self.mouse_y = y

    def on_update(self, delta_time):
        """ Movement and game logic """
        if self.cur_screen == "start":
            menu_start.on_update(self)
        elif self.cur_screen == "game":
            self.player_sprite.change_x = 0
            self.player_sprite.change_y = 0

            if self.up_pressed and not self.down_pressed:
                self.player_sprite.change_y = MOVEMENT_SPEED
            elif self.down_pressed and not self.up_pressed:
                self.player_sprite.change_y = -MOVEMENT_SPEED
            if self.left_pressed and not self.right_pressed:
                self.player_sprite.change_x = -MOVEMENT_SPEED
            elif self.right_pressed and not self.left_pressed:
                self.player_sprite.change_x = MOVEMENT_SPEED

            if (math.ceil(self.player_sprite.center_x) in range(200, 530) and
                    math.ceil(self.player_sprite.center_y) in
                    range(290, 300) and
                    self.current_room == 6):
                if self.act_pressed is True:
                    print('healed')
                    for poke in self.player_sprite.pokemon:
                        poke.cur_stats[0] = poke.stats[0]
                        for move in poke.moves:
                            move.set_cur_pp(move.get_pp())

            # Call update on all sprites (The sprites don't do much in this
            # example though.)
            self.physics_engine.update()
            self.player_list.update()
            # --- Manage Scrolling ---
            # Keep track of if we changed the boundary.

            map.view_logic(self)
            map.room_logic(self)
        elif self.cur_screen == "battle":

            battle.update(self)
            arcade.set_viewport(0, screen_width, 0, screen_height)

        elif self.cur_screen == "game menu":

            menu_game.update(self)
            arcade.set_viewport(0, screen_width, 0, screen_height)

        elif self.cur_screen == "pokebag":
            pokeStorage.update(self)

    def resume_program(self):
        self.cur_screen = "game"

    def heal_part(self):
        self.cur_screen = "heal"
        self.edit_pointer(0)

    def ball_part(self):
        self.cur_screen = "balls"
        self.edit_pointer(0)

    def buff_part(self):
        self.cur_screen = "buff"
        self.edit_pointer(0)

    def poke_part(self):
        self.cur_screen = "pokemon"

    def pokebag_part(self):
        self.cur_screen = "pokebag"


def main():
    """ Main method """
    window = MyGame(screen_width, screen_height, screen_title)
    menu_start.setup(window)
    arcade.run()


if __name__ == "__main__":
    main()
