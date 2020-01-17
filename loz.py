import arcade.gui
import os
import math
import map
import battle
import pokemon

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


def sort_pokemon(poke):
    # sort pokemon storage by level
    if len(poke) == 1:
        return poke

    midpoint = len(poke) // 2
    left_side = sort_pokemon(poke[:midpoint])
    right_side = sort_pokemon(poke[midpoint:])
    sorted_poke = []

    left_marker = 0
    right_marker = 0
    while left_marker < len(left_side) and right_marker < len(right_side):
        if left_side[left_marker].lvl < right_side[right_marker].lvl:
            sorted_poke.append(left_side[left_marker])
            left_marker += 1
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
    # search pokemon by name, return list of pokemon
    result = []
    for poke in poke_list:
        if poke.name == target:
            result.append(poke)

    return result


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()

        # Load a left facing texture and a right facing texture.
        # mirrored=True will mirror the image we load.
        texture = arcade.load_texture("images/character.png",
                                      mirrored=True, scale=other_scale)
        self.textures.append(texture)
        texture = arcade.load_texture("images/character.png",
                                      scale=other_scale)
        self.textures.append(texture)

        # By default, face right.
        self.face_dir = 1
        # 0 = up, 1 = right, 2 = down, 3 = left
        self.set_texture(tex_right)

        self.pokemon = []
        self.pokeball_bag = []
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

    def catch(self, poke):
        if poke.wild:
            if len(self.pokemon) < 6:
                self.pokemon.append(poke)
            else:
                self.pokemon_storage.append(poke)
        else:
            print("cannot catch")


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
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.cur_screen = None
        self.current_room = 1
        self.coin_list = None

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
        self.battle_theme = None
        self.battle_button = None
        self.battle_button_list = None
        self.battle_pokemon_list = None

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

        poke = pokemon.Pokemon.Magikarp()
        poke.addlevel(18)
        self.player_sprite.pokemon.append(poke)
        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

        self.rooms = map.create()

        self.current_room = 1

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        if self.cur_screen == "game":
            arcade.draw_texture_rectangle(screen_width, screen_height,
                                          screen_width * 2, screen_height * 2,
                                          self.rooms[self.current_room].
                                          background)
            self.rooms[self.current_room].wall_list.draw()
            self.player_list.draw()
            if self.current_room == 3:
                self.rooms[self.current_room].grass_list.draw()
        elif self.cur_screen == "battle":
            battle.on_draw(self)
        elif self.cur_screen == "bag":
            print("bag")

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
        elif self.cur_screen == "balls":
            print("balls")

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
        if self.cur_screen == "battle":
            check_mouse_press_for_buttons(x, y, self.battle_button_list)

    def on_mouse_release(self, x, y, button, key_modifiers):
        if self.cur_screen == "battle":
            check_mouse_release_for_buttons(x, y, self.battle_button_list)

    def on_update(self, delta_time):
        """ Movement and game logic """
        if self.cur_screen == "game":
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

            if math.ceil(self.player_sprite.center_x) in range(200, 530) and math.ceil(self.player_sprite.center_y) in range(300,310) and self.current_room == 6:
                if self.act_pressed == True:
                    print('healed')
                    for poke in self.player_sprite.pokemon:
                        poke.cur_stats[0] = poke.stats[0]

            # Call update on all sprites (The sprites don't do much in this
            # example though.)
            self.physics_engine.update()
            self.player_list.update()
            # --- Manage Scrolling ---
            # Keep track of if we changed the boundary. We don't want to call the
            # set_viewport command if we didn't change the view port.

            map.view_logic(self)
            map.room_logic(self)
        elif self.cur_screen == "battle":

            battle.update(self)
            arcade.set_viewport(0, screen_width, 0, screen_height)
        # 1000-1080, 674.4
        # 383.6, 40
        # if player in room then make the viewport 0 and set the screen


def main():
    """ Main method """
    window = MyGame(screen_width, screen_height, screen_title)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
