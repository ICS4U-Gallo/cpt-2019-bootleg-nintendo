import arcade
import settings

width = settings.WIDTH
height = settings.HEIGHT

"""
bag
save
exit
"""


def main_menu():
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()

    arcade.draw_text("Pause Menu",
                     width/2, height * 0.95, arcade.color.BLACK, 50,
                     align="center", anchor_x="center", anchor_y="center")
    arcade.draw_xywh_rectangle_outline(width/2-150,
                                       height/2-25, 300, 75,
                                       arcade.color.BLACK, 5)
    arcade.draw_text("Play", width/2,
                     height/2+13, arcade.color.BLACK, 30,
                     align="center", anchor_x="center", anchor_y="center")
    arcade.draw_xywh_rectangle_outline(width/2-150,
                                       height/2-125, 300,
                                       75, arcade.color.BLACK, 5)
    arcade.draw_text("How to Play", width/2,
                     height/2-87, arcade.color.BLACK, 30,
                     align="center", anchor_x="center", anchor_y="center")


if __name__ == "__main__":
    window = arcade.Window(width, height)  # temporary

    main_menu()

    arcade.run()
