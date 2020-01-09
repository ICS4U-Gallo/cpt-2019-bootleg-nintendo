import random
import arcade
import os

sprite_scale = 0.5
native_sprite = 128
sprite_size = int(sprite_scale * native_sprite)

screen_width = sprite_size * 12
screen_height = sprite_size * 10
screen_title = "Sprite Move with Scrolling Screen Example"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
view_boundary_yaxis = 294
view_boundary_xaxis = 375

MOVEMENT_SPEED = 5


class Room:

    def __init__(self):
        self.wall_list = None
        self.background_list = None


def start_town():
    room = Room()

    room.wall_list = arcade.SpriteList()

    for y in (0, (screen_height * 2) - sprite_size):
        for x in range(0, (screen_width * 2), sprite_size):
            if x != sprite_size * 3 and x != sprite_size * 4:
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    for x in (0, (screen_width * 2) - sprite_size):
        for y in range(sprite_size, (screen_height * 2) - sprite_size, sprite_size):
            if y != sprite_size * 4 and y != sprite_size * 5:
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
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
            if x != sprite_size * 3 and x != sprite_size * 4:
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    for x in (0, (screen_width * 2) - sprite_size):
        for y in range(sprite_size, (screen_height * 2) - sprite_size, sprite_size):
            if y != sprite_size * 4 and y != sprite_size * 5:
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
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

        room = other_town()
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
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # --- Manage Scrolling ---

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
        
        if self.player_sprite.center_x > screen_width and self.current_room == 0:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
        elif self.player_sprite.center_x < 0 and self.current_room == 1:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = screen_width


def main():
    """ Main method """
    window = MyGame(screen_width, screen_height, screen_title)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()