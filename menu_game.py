import arcade
import settings

width = 768
height = 640

select_x = 0
select_y = 0

dex_color = arcade.color.BLACK
bag_color = arcade.color.GRAY
save_color = arcade.color.GRAY
exit_color = arcade.color.GRAY


def main_menu():
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()

    arcade.draw_text("GAME MENU",
                     width/2, height * 0.95, arcade.color.BLACK, 50,
                     align="center", anchor_x="center", anchor_y="center")

    arcade.draw_xywh_rectangle_outline(width/4-150,
                                       height/2-25, 325, 250,
                                       dex_color, 5)
    arcade.draw_text("POKEDEX", width/4 + 12.5,
                     height * 3/4, dex_color, 45,
                     align="center", anchor_x="center", anchor_y="center")

    arcade.draw_xywh_rectangle_outline(width * 3/4 - 175,
                                       height/2-25, 325, 250,
                                       bag_color, 5)
    arcade.draw_text("BAG", width * 3/4 - 12.5,
                     height * 3/4, bag_color, 45,
                     align="center", anchor_x="center", anchor_y="center")

    arcade.draw_xywh_rectangle_outline(width/4 - 150,
                                       height/2-300, 325,
                                       250, save_color, 5)
    arcade.draw_text("SAVE", width/4 + 12.5,
                     height/2-120, save_color, 45,
                     align="center", anchor_x="center", anchor_y="center")

    arcade.draw_xywh_rectangle_outline(width * 3/4 - 175,
                                       height/2-300, 325,
                                       250, exit_color, 5)
    arcade.draw_text("EXIT", width * 3/4 - 12.5,
                     height/2-120, exit_color, 45,
                     align="center", anchor_x="center", anchor_y="center")


def on_key_press(self, key, modifiers):
    pass


def on_key_release(self, key, modifiers):
    pass


if __name__ == "__main__":
    window = arcade.Window(width, height)  # temporary
    # arcade.schedule(main_menu, 1/60)

    main_menu()

    arcade.run()
