import random
import arcade
from math import ceil
import battle
from pokemon import Pokemon

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
        self.enemy_list = None
        self.pokeball = None


def start_town():
    room = Room()

    room.wall_list = arcade.SpriteList()

    for y in (0, (screen_height * 2) - sprite_size):
        for x in range(0, (screen_width * 2), sprite_size):
            if ((x != sprite_size * 3 and x != sprite_size * 4) or
                    y != (screen_height * 2 - sprite_size)):
                wall = arcade.Sprite(":resources:images/tiles/cactus.png",
                                     sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    for x in (0, (screen_width * 2) - sprite_size):
        for y in range(sprite_size,
                       (screen_height * 2) - sprite_size, sprite_size):
            wall = arcade.Sprite(":resources:images/tiles/cactus.png",
                                 sprite_scale)
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

    room.background = arcade.load_texture("images/home_floor.jpg")

    return room


def poke_lab():
    room = Room()

    room.wall_list = arcade.SpriteList()
    room.pokeball = arcade.SpriteList()

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
    table.center_x = screen_width/2
    table.bottom = 350
    room.wall_list.append(table)

    ball = arcade.Sprite("images/pokeballs/pokeball.png", 0.3)
    ball.center_x = screen_width/2
    ball.center_y = 425
    room.pokeball.append(ball)

    room.background = arcade.load_texture("images/background.jpg")

    return room


def wild_area():
    room = Room()

    room.wall_list = arcade.SpriteList()
    room.grass_list = arcade.SpriteList()

    for x in (0, (screen_width * 2) - sprite_size):
        for y in range(0, (screen_height * 2), sprite_size):
            if (y != sprite_size * 4 and y != sprite_size * 5) or x == 0:
                wall = arcade.Sprite(":resources:images/tiles/cactus.png",
                                     sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    for y in (0, (screen_height * 2) - sprite_size):
        for x in range(0, (screen_width * 2), sprite_size):
            if (x != sprite_size * 3 and x != sprite_size * 4) or y != 0:
                wall = arcade.Sprite(":resources:images/tiles/cactus.png",
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

    room.background = arcade.load_texture("images/background.jpg")
    return room


def other_town():
    room = Room()

    room.wall_list = arcade.SpriteList()

    for y in (0, (screen_height * 2) - sprite_size):
        for x in range(0, (screen_width * 2), sprite_size):
            wall = arcade.Sprite(":resources:images/tiles/cactus.png",
                                 sprite_scale)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    for x in (0, (screen_width * 2) - sprite_size):
        for y in range(sprite_size, (screen_height * 2) - sprite_size,
                       sprite_size):
            if (y != sprite_size * 4 and y != sprite_size * 5) or x != 0:
                wall = arcade.Sprite(":resources:images/tiles/cactus.png",
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
    room.enemy_list = arcade.SpriteList()

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

    for x in range(sprite_size, (screen_width*2)-(sprite_size*6), sprite_size):
        wall = arcade.Sprite("images/boxCrate_double.png",
                             sprite_scale)
        wall.left = x
        wall.bottom = sprite_size*6
        room.wall_list.append(wall)

    for y in range(sprite_size*7, (screen_height*2)-(sprite_size*5),
                   sprite_size):
        wall = arcade.Sprite("images/boxCrate_double.png",
                             sprite_scale)
        wall.left = sprite_size*17
        wall.bottom = y
        room.wall_list.append(wall)

    for y in range(sprite_size*7, (screen_height*2)-sprite_size, sprite_size):
        wall = arcade.Sprite("images/boxCrate_double.png",
                             sprite_scale)
        wall.left = sprite_size*7
        wall.bottom = y
        room.wall_list.append(wall)

    loc = [[3, 3, 1], [8, 1, 0], [13, 5, 2], [18, 1, 0], [18, 6, 1],
           [22, 10, 3], [18, 14, 1], [17, 18, 2], [16, 14, 3]]
    for i in range(len(loc)):
        poke_list = []
        for j in range(2):
            poke = Pokemon.Magikarp()
            poke.addlevel(5*(i+1)+j)
            poke_list.append(poke)
        enemy = battle.Enemy(False, poke_list, loc[i][2], False)
        enemy.left = loc[i][0]*64
        enemy.bottom = loc[i][1]*64
        room.enemy_list.append(enemy)

    poke_list = []
    for i in range(6):
        poke = Pokemon.Magikarp()
        poke.addlevel(50+i)
        poke_list.append(poke)
    boss = battle.Enemy(False, poke_list, 0, True)
    boss.center_x = screen_width
    boss.center_y = screen_height
    room.enemy_list.append(boss)

    room.background = arcade.load_texture("images/home_floor.jpg")

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

    room.background = arcade.load_texture("images/home_floor.jpg")

    return room


def room_logic(player):
    if (ceil(player.player_sprite.center_x) in range(1000, 1080) and
            ceil(player.player_sprite.center_y) in range(660, 676) and
            player.current_room == 0):
        player.current_room = 2
        player.physics_engine = arcade.PhysicsEngineSimple((player.
                                                            player_sprite),
                                                           (player.rooms
                                                           [player.
                                                            current_room].
                                                            wall_list))
        player.player_sprite.center_x = 383.6
        player.player_sprite.center_y = 40
    elif player.player_sprite.center_y < 35 and player.current_room == 1:
        player.current_room = 0
        player.physics_engine = arcade.PhysicsEngineSimple((player.
                                                            player_sprite),
                                                           (player.rooms
                                                            [player.
                                                             current_room].
                                                            wall_list))
        player.player_sprite.center_x = 240
        player.player_sprite.center_y = 656
    elif player.player_sprite.center_y > 1250 and player.current_room == 0:
        player.current_room = 3
        player.physics_engine = arcade.PhysicsEngineSimple((player.
                                                            player_sprite),
                                                           (player.rooms
                                                            [player.
                                                             current_room].
                                                            wall_list))
        player.player_sprite.center_y = 30
    elif player.player_sprite.center_x > 1500 and player.current_room == 3:
        player.current_room = 4
        player.physics_engine = arcade.PhysicsEngineSimple((player.
                                                            player_sprite),
                                                           (player.rooms
                                                            [player.
                                                             current_room].
                                                            wall_list))
        player.player_sprite.center_x = 30
    elif (ceil(player.player_sprite.center_x) in range(200, 285) and
          ceil(player.player_sprite.center_y) in range(660, 676) and
          player.current_room == 0):
        player.current_room = 1
        player.physics_engine = arcade.PhysicsEngineSimple((player.
                                                            player_sprite),
                                                           (player.rooms
                                                            [player.
                                                             current_room].
                                                            wall_list))
        player.player_sprite.center_x = 383.6
        player.player_sprite.center_y = 40
    elif player.player_sprite.center_y < 35 and player.current_room == 2:
        player.current_room = 0
        player.physics_engine = arcade.PhysicsEngineSimple((player.
                                                            player_sprite),
                                                           (player.rooms
                                                            [player.
                                                             current_room].
                                                            wall_list))
        player.player_sprite.center_x = 1040
        player.player_sprite.center_y = 656
    elif (ceil(player.player_sprite.center_x) in range(1100, 1180) and
          ceil(player.player_sprite.center_y) in range(660, 676) and
          player.current_room == 4):
        player.current_room = 5
        player.physics_engine = arcade.PhysicsEngineSimple((player.
                                                            player_sprite),
                                                           (player.rooms
                                                            [player.
                                                             current_room].
                                                            wall_list))
        player.player_sprite.center_x = 383.6
        player.player_sprite.center_y = 40
    elif (ceil(player.player_sprite.center_x) in range(180, 270) and
          ceil(player.player_sprite.center_y) in range(660, 676) and
          player.current_room == 4):
        player.current_room = 6
        player.physics_engine = arcade.PhysicsEngineSimple((player.
                                                            player_sprite),
                                                           (player.rooms
                                                            [player.
                                                             current_room].
                                                            wall_list))
        player.player_sprite.center_x = 383.6
        player.player_sprite.center_y = 40
    elif player.player_sprite.center_y < 35 and player.current_room == 5:
        player.current_room = 4
        player.physics_engine = arcade.PhysicsEngineSimple((player.
                                                            player_sprite),
                                                           (player.rooms
                                                            [player.
                                                             current_room].
                                                            wall_list))
        player.player_sprite.center_x = 1140
        player.player_sprite.center_y = 656
    elif player.player_sprite.center_y < 35 and player.current_room == 6:
        player.current_room = 4
        player.physics_engine = arcade.PhysicsEngineSimple((player.
                                                            player_sprite),
                                                           (player.rooms
                                                            [player.
                                                             current_room].
                                                            wall_list))
        player.player_sprite.center_x = 240
        player.player_sprite.center_y = 656
    elif player.player_sprite.center_y < 20 and player.current_room == 3:
        player.current_room = 0
        player.physics_engine = arcade.PhysicsEngineSimple((player.
                                                            player_sprite),
                                                           (player.rooms
                                                            [player.
                                                             current_room].
                                                            wall_list))
        player.player_sprite.center_y = ((screen_height * 2) - sprite_size)
    elif player.player_sprite.center_x < 20 and player.current_room == 4:
        player.current_room = 3
        player.physics_engine = arcade.PhysicsEngineSimple((player.
                                                            player_sprite),
                                                           (player.rooms
                                                            [player.
                                                             current_room].
                                                            wall_list))
        player.player_sprite.center_x = ((screen_width * 2) - sprite_size)

    if player.current_room == 3:
        grass_hit = arcade.check_for_collision_with_list(player.player_sprite,
                                                         player.rooms
                                                         [player.current_room].
                                                         grass_list)
        if len(grass_hit) > 0:
            encounter = random.randint(0, 69)
            if encounter == 1 and not player.player_sprite.defeated():
                print("pokemon")
                battle.wild_encounter(player)
    elif player.current_room == 5:
        for enemy in player.rooms[player.current_room].enemy_list:
            if not player.player_sprite.defeated():
                enemy.see_player(player, player.player_sprite)
    elif player.current_room == 2:
        if (len(player.rooms[player.current_room].pokeball) == 1 and
            player.act_pressed):
            poke_list = [Pokemon.Charmander(), Pokemon.Squirtle(),
                         Pokemon.Bulbasaur(), Pokemon.Magikarp()]
            for poke in poke_list:
                poke.addlevel(4)
                player.player_sprite.pokemon.append(poke)
            player.rooms[player.current_room].pokeball = arcade.SpriteList()


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

        # Make sure our boundaries are integer values.
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


def main():
    """ Main method """
    pass


if __name__ == "__main__":
    main()
