import arcade
import settings

width = 768
height = 640

"""
bag
save
exit
"""


def main_menu():
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()

    arcade.draw_text("GAME MENU",
                     width/2, height * 0.95, arcade.color.BLACK, 50,
                     align="center", anchor_x="center", anchor_y="center")

    arcade.draw_xywh_rectangle_outline(width/4-150,
                                       height/2-25, 325, 250,
                                       arcade.color.BLACK, 5)
    arcade.draw_text("BAG", width/4 + 12.5,
                     height * 3/4, arcade.color.BLACK, 45,
                     align="center", anchor_x="center", anchor_y="center")

    arcade.draw_xywh_rectangle_outline(width * 3/4 - 175,
                                       height/2-25, 325, 250,
                                       arcade.color.BLACK, 5)
    arcade.draw_text("SAVE", width * 3/4 - 12.5,
                     height * 3/4, arcade.color.BLACK, 45,
                     align="center", anchor_x="center", anchor_y="center")

    arcade.draw_xywh_rectangle_outline(width/4 - 150,
                                       height/2-300, 325,
                                       250, arcade.color.BLACK, 5)
    arcade.draw_text("EXIT MENU", width/4 + 12.5,
                     height/2-120, arcade.color.BLACK, 45,
                     align="center", anchor_x="center", anchor_y="center")

    arcade.draw_xywh_rectangle_outline(width * 3/4 - 175,
                                       height/2-300, 325,
                                       250, arcade.color.BLACK, 5)
    arcade.draw_text("._.", width * 3/4 - 12.5,
                     height/2-120, arcade.color.BLACK, 45,
                     align="center", anchor_x="center", anchor_y="center")


if __name__ == "__main__":
    window = arcade.Window(width, height)  # temporary

    main_menu()

    arcade.run()
