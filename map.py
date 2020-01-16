import random
import arcade
import os
from math import ceil
import battle

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


class Room:

    def __init__(self):
        self.wall_list = None
        self.background_list = None
        self.grass_list = None


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


def start_town():
    room = Room()

    room.wall_list = arcade.SpriteList()

    for y in (0, (screen_height * 2) - sprite_size):
        for x in range(0, (screen_width * 2), sprite_size):
            if (x != sprite_size * 3 and x != sprite_size * 4) or y != (screen_height * 2 - sprite_size):
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    for x in (0, (screen_width * 2) - sprite_size):
        for y in range(sprite_size, (screen_height * 2) - sprite_size, sprite_size):
            wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    house = arcade.Sprite("images/house.png", 6)
    house.left = 900
    house.bottom = 700
    room.wall_list.append(house)

    house2 = arcade.Sprite("images/house.png", 6)
    house2.left = 100
    house2.bottom = 700
    room.wall_list.append(house2)

    room.background = arcade.load_texture("images/background.jpg")

    return room


def start_room():
    room = Room()

    room.wall_list = arcade.SpriteList()

    for x in (0, screen_width - sprite_size):
        for y in range(0, screen_height, sprite_size):
            wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    for y in (0, screen_height - sprite_size):
        for x in range(0, screen_width, sprite_size):
            if (x != sprite_size * 5 and x != sprite_size * 6) or y != 0:
                wall = arcade.Sprite("images/boxCrate_double.png",
                                     sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    table = arcade.Sprite("images/table.png", 2)
    table.left = 500
    table.bottom = 350
    room.wall_list.append(table)

    bed = arcade.Sprite("images/bed.png", 2)
    bed.left = 100
    bed.bottom = 300
    room.wall_list.append(bed)

    room.background = arcade.load_texture("images/background.jpg")

    return room


def poke_lab():
    room = Room()

    room.wall_list = arcade.SpriteList()

    for x in (0, screen_width - sprite_size):
        for y in range(0, screen_height, sprite_size):
            wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    for y in (0, screen_height - sprite_size):
        for x in range(0, screen_width, sprite_size):
            if (x != sprite_size * 5 and x != sprite_size * 6) or y != 0:
                wall = arcade.Sprite("images/boxCrate_double.png",
                                     sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    table = arcade.Sprite("images/table.png", 2)
    table.left = 300
    table.bottom = 350
    room.wall_list.append(table)

    room.background = arcade.load_texture("images/background.jpg")

    return room


def wild_area():
    room = Room()

    room.wall_list = arcade.SpriteList()
    room.grass_list = arcade.SpriteList()

    for x in (0, (screen_width * 2) - sprite_size):
        for y in range(0, (screen_height * 2), sprite_size):
            if (y != sprite_size * 4 and y != sprite_size * 5) or x == 0:
                wall = arcade.Sprite("images/boxCrate_double.png",
                                     sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    for y in (0, (screen_height * 2) - sprite_size):
        for x in range(0, (screen_width * 2), sprite_size):
            if (x != sprite_size * 3 and x != sprite_size * 4) or y != 0:
                wall = arcade.Sprite("images/boxCrate_double.png",
                                     sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    for x in range(sprite_size, (screen_width * 2) - (sprite_size),
                   sprite_size):
        for y in range(sprite_size, (screen_height * 2) - (sprite_size),
                       sprite_size):
            grass = arcade.Sprite("images/grass.png", sprite_scale)
            grass.left = x
            grass.bottom = y
            room.grass_list.append(grass)

    room.background = arcade.load_texture("images/floors.jpg")
    return room


def other_town():
    room = Room()

    room.wall_list = arcade.SpriteList()

    for y in (0, (screen_height * 2) - sprite_size):
        for x in range(0, (screen_width * 2), sprite_size):
            wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    for x in (0, (screen_width * 2) - sprite_size):
        for y in range(sprite_size, (screen_height * 2) - sprite_size,
                       sprite_size):
            if (y != sprite_size * 4 and y != sprite_size * 5) or x != 0:
                wall = arcade.Sprite("images/boxCrate_double.png",
                                     sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    gym = arcade.Sprite("images/gym.png", 6)
    gym.left = 700
    gym.bottom = 700
    room.wall_list.append(gym)

    pokecen = arcade.Sprite("images/pokecen.png", 6)
    pokecen.left = 100
    pokecen.bottom = 700
    room.wall_list.append(pokecen)

    room.background = arcade.load_texture("images/background.jpg")

    return room


def gym():
    room = Room()

    room.wall_list = arcade.SpriteList()

    for x in (0, (screen_width * 2) - sprite_size):
        for y in range(0, (screen_height * 2), sprite_size):
            wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    for y in (0, (screen_height * 2) - sprite_size):
        for x in range(0, (screen_width * 2), sprite_size):
            if (x != sprite_size * 5 and x != sprite_size * 6) or y != 0:
                wall = arcade.Sprite("images/boxCrate_double.png",
                                     sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    room.background = arcade.load_texture("images/background.jpg")

    return room


def heal_center():
    room = Room()

    room.wall_list = arcade.SpriteList()

    for x in (0, screen_width - sprite_size):
        for y in range(0, screen_height, sprite_size):
            wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    for y in (0, screen_height - sprite_size):
        for x in range(0, screen_width, sprite_size):
            if (x != sprite_size * 5 and x != sprite_size * 6) or y != 0:
                wall = arcade.Sprite("images/boxCrate_double.png",
                                     sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    healstation = arcade.Sprite("images/heal_station.png", 5)
    healstation.left = 200
    healstation.bottom = 330
    room.wall_list.append(healstation)

    room.background = arcade.load_texture("images/background.jpg")

    return room

def room_logic(player):
    if ceil(player.player_sprite.center_x) in range(1000, 1080) and ceil(player.player_sprite.center_y) in range(670, 676) and player.current_room == 0:
        player.current_room = 2
        player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                         player.rooms[player.current_room].wall_list)
        player.player_sprite.center_x = 383.6
        player.player_sprite.center_y = 40
    elif player.player_sprite.center_y < 35 and player.current_room == 1:
        player.current_room = 0
        player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                         player.rooms[player.current_room].wall_list)
        player.player_sprite.center_x = 240
        player.player_sprite.center_y = 656
    elif player.player_sprite.center_y > 1250 and player.current_room == 0:
        player.current_room = 3
        player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                         player.rooms[player.current_room].wall_list)
        player.player_sprite.center_y = 30
    elif player.player_sprite.center_x > 1500 and player.current_room == 3:
        player.current_room = 4
        player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                         player.rooms[player.current_room].wall_list)
        player.player_sprite.center_x = 30
    elif ceil(player.player_sprite.center_x) in range(200, 285) and ceil(player.player_sprite.center_y) in range(670, 676) and player.current_room == 0:
        player.current_room = 1
        player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                         player.rooms[player.current_room].wall_list)
        player.player_sprite.center_x = 383.6
        player.player_sprite.center_y = 40
    elif player.player_sprite.center_y < 35 and player.current_room == 2:
        player.current_room = 0
        player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                         player.rooms[player.current_room].wall_list)
        player.player_sprite.center_x = 1040
        player.player_sprite.center_y = 656
    elif ceil(player.player_sprite.center_x) in range(1100, 1180) and ceil(player.player_sprite.center_y) in range(670, 676) and player.current_room == 4:
        player.current_room = 5
        player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                         player.rooms[player.current_room].wall_list)
        player.player_sprite.center_x = 383.6
        player.player_sprite.center_y = 40
    elif ceil(player.player_sprite.center_x) in range(180, 270) and ceil(player.player_sprite.center_y) in range(670, 676) and player.current_room == 4:
        player.current_room = 6
        player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                         player.rooms[player.current_room].wall_list)
        player.player_sprite.center_x = 383.6
        player.player_sprite.center_y = 40
    elif player.player_sprite.center_y < 35 and player.current_room == 5:
        player.current_room = 4
        player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                         player.rooms[player.current_room].wall_list)
        player.player_sprite.center_x = 1140
        player.player_sprite.center_y = 656
    elif player.player_sprite.center_y < 35 and player.current_room == 6:
        player.current_room = 4
        player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                         player.rooms[player.current_room].wall_list)
        player.player_sprite.center_x = 240
        player.player_sprite.center_y = 656
    elif player.player_sprite.center_y < 20 and player.current_room == 3:
        player.current_room = 0
        player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                         player.rooms[player.current_room].wall_list)
        player.player_sprite.center_y = ((screen_height * 2) - sprite_size)
    elif player.player_sprite.center_x < 20 and player.current_room == 4:
        player.current_room = 3
        player.physics_engine = arcade.PhysicsEngineSimple(player.player_sprite,
                                                         player.rooms[player.current_room].wall_list)
        player.player_sprite.center_x = ((screen_width * 2) - sprite_size)

    if player.current_room == 3:
        grass_hit = arcade.check_for_collision_with_list(player.player_sprite, player.rooms[player.current_room].grass_list)
        if len(grass_hit) > 0:
            encounter = random.randint(0, 69)
            if encounter == 1 and not player.player_sprite.defeated():
                print("pokemon")
                battle.wild_encounter(player)


def view_logic(player):
    changed = False

    # Scroll left
    if player.current_room in big_room_list:
        left_boundary = player.view_left + view_boundary_xaxis
        if player.player_sprite.left < left_boundary:
            player.view_left -= left_boundary - player.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = player.view_left + screen_width - view_boundary_xaxis
        if player.player_sprite.right > right_boundary:
            player.view_left += player.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = player.view_bottom + screen_height - view_boundary_yaxis
        if player.player_sprite.top > top_boundary:
            player.view_bottom += player.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = player.view_bottom + view_boundary_yaxis
        if player.player_sprite.bottom < bottom_boundary:
            player.view_bottom -= bottom_boundary - player.player_sprite.bottom
            changed = True

        # Make sure our boundaries are integer values. While the view port does
        # support floating point numbers, for this application we want every pixel
        # in the view port to map directly onto a pixel on the screen. We don't want
        # any rounding errors.
        player.view_left = int(player.view_left)
        player.view_bottom = int(player.view_bottom)

        # If we changed the boundary values, update the view port to match
        if changed:
            arcade.set_viewport(player.view_left,
                                screen_width + player.view_left - 1,
                                player.view_bottom,
                                screen_height + player.view_bottom - 1)
    if player.current_room in small_room_list:
        arcade.set_viewport(0, screen_width, 0, screen_height)

def create():
    room_list = []

    room = start_town()
    room_list.append(room)

    room = start_room()
    room_list.append(room)

    room = poke_lab()
    room_list.append(room)

    room = wild_area()
    room_list.append(room)

    room = other_town()
    room_list.append(room)

    room = gym()
    room_list.append(room)

    room = heal_center()
    room_list.append(room)

    return room_list


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

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = Player()
        self.player_sprite.center_x = 250
        self.player_sprite.center_y = 400
        self.player_list.append(self.player_sprite)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

        self.rooms = []



        self.current_room = 1

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        arcade.draw_texture_rectangle(screen_width, screen_height,
                                      screen_width * 2, screen_height * 2, self.rooms[self.current_room].background)
        self.rooms[self.current_room].wall_list.draw()
        self.player_list.draw()
        if self.current_room == 3:
            self.rooms[self.current_room].grass_list.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

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

    def on_update(self, delta_time):
        """ Movement and game logic """

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

        if ceil(self.player_sprite.center_x) in range(200, 530) and ceil(self.player_sprite.center_y) in range(300, 310) and self.current_room == 6:
            if self.act_pressed == True:
                print('healed')

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()
        self.player_list.update()
        # --- Manage Scrolling ---
        # Keep track of if we changed the boundary. We don't want to call the
        # set_viewport command if we didn't change the view port.

        view_logic(self)
        room_logic(self)

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