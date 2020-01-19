import arcade

width = 768
height = 640


def setup(player):
    player.select_x = 0
    player.select_y = 1

    player.dex_color = arcade.color.BLACK
    player.bag_color = arcade.color.BLACK
    player.save_color = arcade.color.BLACK
    player.exit_color = arcade.color.BLACK

    player.dex_sprite = arcade.load_texture("images/game_menu_images/"
                                            "pokedex.png")
    player.bag_sprite = arcade.load_texture("images/game_menu_images/"
                                            "bag.jpg")
    player.save_sprite = arcade.load_texture("images/game_menu_images/"
                                             "save.png")
    player.exit_sprite = arcade.load_texture("images/game_menu_images/"
                                             "exit.jpeg")


def on_draw(player):
    arcade.start_render()
    arcade.set_background_color(arcade.color.WHITE)
    arcade.draw_text("GAME MENU", 384, 608, arcade.color.BLACK, 50,
                     align="center", anchor_x="center", anchor_y="center")

    arcade.draw_xywh_rectangle_outline(42, 295, 325, 250,
                                       player.dex_color, 5)
    arcade.draw_text("POKEDEX", 204, 480, player.dex_color, 45,
                     align="center", anchor_x="center", anchor_y="center")
    arcade.draw_texture_rectangle(192, 380, 190, 140, player.dex_sprite)

    arcade.draw_xywh_rectangle_outline(401, 295, 325, 250,
                                       player.bag_color, 5)
    arcade.draw_text("BAG", 564, 480, player.bag_color, 45,
                     align="center", anchor_x="center", anchor_y="center")
    arcade.draw_texture_rectangle(556, 380, 190, 140, player.bag_sprite)

    arcade.draw_xywh_rectangle_outline(42, 20, 325, 250,
                                       player.save_color, 5)
    arcade.draw_text("SAVE", 204, 200, player.save_color, 45,
                     align="center", anchor_x="center", anchor_y="center")
    arcade.draw_texture_rectangle(192, 91, 190, 140, player.save_sprite)

    arcade.draw_xywh_rectangle_outline(401, 20, 325, 250,
                                       player.exit_color, 5)
    arcade.draw_text("EXIT", 564, 200, player.exit_color, 45,
                     align="center", anchor_x="center", anchor_y="center")
    arcade.draw_texture_rectangle(556, 91, 150, 100, player.exit_sprite)


def update(player):
    if player.select_x == 0 and player.select_y == 1:
        player.dex_color = arcade.color.BLACK
    elif player.select_x == 1 and player.select_y == 1:
        player.bag_color = arcade.color.BLACK
    elif player.select_x == 0 and player.select_y == 0:
        player.save_color = arcade.color.BLACK
    elif player.select_x == 1 and player.select_y == 0:
        player.exit_color = arcade.color.BLACK


def key_logic(player, key):
    if key == arcade.key.W:
        if player.select_y < 1:
            player.select_y += 1
    elif key == arcade.key.S:
        if player.select_y > 0:
            player.select_y -= 1
    elif key == arcade.key.D:
        if player.select_x < 1:
            player.select_x += 1
    elif key == arcade.key.A:
        if player.select_x > 0:
            player.select_x -= 1

    player.dex_color = arcade.color.GRAY
    player.bag_color = arcade.color.GRAY
    player.save_color = arcade.color.GRAY
    player.exit_color = arcade.color.GRAY

    if key == arcade.key.L:
        if player.select_x == 0 and player.select_y == 1:  # pokedex
            player.cur_screen = "pokedex"
        elif player.select_x == 1 and player.select_y == 1:  # bag
            player.cur_screen = "bag"
        elif player.select_x == 0 and player.select_y == 0:  # save
            print("save")
        elif player.select_x == 1 and player.select_y == 0:  # exit
            player.cur_screen = "game"
    elif key == arcade.key.K:
        player.cur_screen = "game"


def main():
    game = MyGame(width, height, "Game Menu")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
