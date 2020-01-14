import random
import arcade
import os
from math import ceil

sprite_scale = 0.5
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


class Room:

    def __init__(self):
        self.wall_list = None
        self.background_list = None


class Player(arcade.Sprite):
    pass


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

    room.background = arcade.load_texture("images/background.jpg")

    return room


def wild_area():
    room = Room()

    room.wall_list = arcade.SpriteList()

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

    room.background = arcade.load_texture("images/background.jpg")
    
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
        for y in range(sprite_size, (screen_height * 2) - sprite_size, sprite_size):
            if (y != sprite_size * 4 and y != sprite_size * 5) or x != 0:
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
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

    room.background = arcade.load_texture("images/background.jpg")

    return room


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
        self.current_room = 0
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
        self.view_bottom = 0
        self.view_left = 0

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("images/character.png", 0.4)
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 500
        self.player_list.append(self.player_sprite)


        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

        self.rooms = []

        room = start_town()
        self.rooms.append(room)

        room = start_room()
        self.rooms.append(room)

        room = poke_lab()
        self.rooms.append(room)

        room = wild_area()
        self.rooms.append(room)

        room = other_town()
        self.rooms.append(room)

        room = gym()
        self.rooms.append(room)

        room = heal_center()
        self.rooms.append(room)

        self.current_room = 0

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

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()
        # --- Manage Scrolling ---
        print(self.player_sprite.center_x, self.player_sprite.center_y)
        # Keep track of if we changed the boundary. We don't want to call the
        # set_viewport command if we didn't change the view port.
        changed = False

        # Scroll left
        left_boundary = self.view_left + view_boundary_xaxis
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + screen_width - view_boundary_xaxis
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + screen_height - view_boundary_yaxis
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + view_boundary_yaxis
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        # Make sure our boundaries are integer values. While the view port does
        # support floating point numbers, for this application we want every pixel
        # in the view port to map directly onto a pixel on the screen. We don't want
        # any rounding errors.
        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        # If we changed the boundary values, update the view port to match
        if changed:
            arcade.set_viewport(self.view_left,
                                screen_width + self.view_left - 1,
                                self.view_bottom,
                                screen_height + self.view_bottom - 1)
        
        if ceil(self.player_sprite.center_x) in range(1000, 1080) and ceil(self.player_sprite.center_y) in range(670, 676) and self.current_room == 0:
            self.current_room = 2
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 383.6
            self.player_sprite.center_y = 40
        elif self.player_sprite.center_y < 35 and self.current_room == 1:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 240
            self.player_sprite.center_y = 656
        elif self.player_sprite.center_y > 1250 and self.current_room == 0:
            self.current_room = 3
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_y = 0
        elif self.player_sprite.center_x > 1500 and self.current_room == 3:
            self.current_room = 4
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
        elif ceil(self.player_sprite.center_x) in range(200, 285) and ceil(self.player_sprite.center_y) in range(670, 676) and self.current_room == 0:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 383.6
            self.player_sprite.center_y = 40
        elif self.player_sprite.center_y < 35 and self.current_room == 2:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 1040
            self.player_sprite.center_y = 656
        elif ceil(self.player_sprite.center_x) in range(1100, 1180) and ceil(self.player_sprite.center_y) in range(670, 676) and self.current_room == 4:
            self.current_room = 5
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 383.6
            self.player_sprite.center_y = 40
        elif ceil(self.player_sprite.center_x) in range(180, 270) and ceil(self.player_sprite.center_y) in range(670, 676) and self.current_room == 4:
            self.current_room = 6
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 383.6
            self.player_sprite.center_y = 40
        elif self.player_sprite.center_y < 35 and self.current_room == 5:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 1040
            self.player_sprite.center_y = 656
        elif self.player_sprite.center_y < 35 and self.current_room == 6:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 1040
            self.player_sprite.center_y = 656
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