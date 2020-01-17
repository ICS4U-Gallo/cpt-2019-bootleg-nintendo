import arcade
import settings
import item  # temporary maybe

width = 768
height = 640

# buff_list = ["TORKOAL", "GARBAGE", "PIKACHU", "EEVEE", "GARCHOMP", "
# VESPIQUEN", "COMBEE", "RAYQUAZA"]


def binary_search(target, numbers):
    start = 0
    end = len(numbers) - 1

    while end >= start:
        mid = (start + end) // 2

        if numbers[mid].effect == target:
            return mid
        elif numbers[mid].effect > target:
            end = mid - 1
        elif numbers[mid].effect < target:
            start = mid + 1

    return -1


def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers

    left_side = merge_sort(numbers[:len(numbers)//2])
    right_side = merge_sort(numbers[len(numbers)//2:])

    left_marker, right_marker = 0, 0

    new_list = []

    while left_marker < len(left_side) and right_marker < len(right_side):
        if left_side[left_marker].effect < right_side[right_marker].effect:
            new_list.append(left_side[left_marker])
            left_marker += 1
        else:
            new_list.append(right_side[right_marker])
            right_marker += 1

    while right_marker < len(right_side):
        new_list.append(right_side[right_marker])
        right_marker += 1

    while left_marker < len(left_side):
        new_list.append(left_side[left_marker])
        left_marker += 1

    return new_list


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        self._pointer = 0
        self.sort_menu = False
        self.search_menu = False

        self.buff_list = [item.Item.steroids(), item.Item.leg_day()]

    def get_pointer(self):
        return self._pointer

    def edit_pointer(self, value):
        self._pointer = value

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Buffs", 20, 570, arcade.color.BLACK, 50)
        arcade.draw_text("Item Count:", 20, 520, arcade.color.BLACK, 30)
        arcade.draw_text(str(len(self.buff_list)), 250, 520,
                         arcade.color.BLACK, 30)
        arcade.draw_text("Q - Sort", 30, 30, arcade.color.BLACK, 60)
        arcade.draw_text("E - Search", 370, 30, arcade.color.BLACK, 60)

        arcade.draw_xywh_rectangle_outline(10, 405, 450, 70,
                                           arcade.color.GRAY, 3)
        arcade.draw_xywh_rectangle_outline(5, 290, 460, 90,
                                           arcade.color.BLACK, 5)
        arcade.draw_xywh_rectangle_outline(10, 193, 450, 70,
                                           arcade.color.GRAY, 3)

        if self.get_pointer() - 1 != -1:
            arcade.draw_text("{}: {}".format(self.buff_list
                             [self.get_pointer() - 1].name,
                             self.buff_list[self.get_pointer() - 1].effect), 20,
                             425, arcade.color.BLACK, 20)

        arcade.draw_text("{}: {}".format(self.buff_list
                         [self.get_pointer()].name,
                         self.buff_list[self.get_pointer()].effect), 20,
                         320, arcade.color.BLACK, 20)

        if self.get_pointer() + 1 != len(self.buff_list):
            arcade.draw_text("{}: {}".format(self.buff_list
                             [self.get_pointer() + 1].name,
                             self.buff_list[self.get_pointer() + 1].effect), 20,
                             213, arcade.color.BLACK, 20)

        arcade.draw_triangle_filled(475, 335, 495, 315, 495,
                                    355, arcade.color.BLACK)
        arcade.draw_xywh_rectangle_outline(500, 210, 250, 250,
                                           arcade.color.BLACK, 10)
        arcade.draw_texture_rectangle(625, 335, 240, 240, self.buff_list
                                      [self.get_pointer()].texture)
        arcade.draw_text("Amount: {}".format(str(self.buff_list[self.get_pointer()].amount)), 465, 150, arcade.color.BLACK, 50)

        if self.search_menu:
            arcade.draw_xywh_rectangle_filled(100, 100, 568, 440,
                                              arcade.color.BLACK)
            arcade.draw_xywh_rectangle_filled(110, 110, 548, 420,
                                              arcade.color.WHITE)
            arcade.draw_text("Enter Pokemon Number:", 140, 450,
                             arcade.color.BLACK, 35)
            arcade.draw_text(" " + self.search_number, 140, 200,
                             arcade.color.BLACK, 220)
        if self.sort_menu:
            arcade.draw_xywh_rectangle_filled(100, 100, 568, 440,
                                              arcade.color.BLACK)
            arcade.draw_xywh_rectangle_filled(110, 110, 548, 420,
                                              arcade.color.WHITE)
            arcade.draw_text("Do you want to sort", 115, 380,
                             arcade.color.BLACK, 50)
            arcade.draw_text("the bag?", 175, 310, arcade.color.BLACK, 50)

    def update(self, delta_time):
        pass

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.W:
            if self.get_pointer() != 0:
                self.edit_pointer(self.get_pointer() - 1)
        elif key == arcade.key.S:
            if self.get_pointer() != len(self.buff_list) - 1:
                self.edit_pointer(self.get_pointer() + 1)
        if key == arcade.key.E or self.search_menu:
            self.search_menu = True
            self.sort_menu = False

            if key == arcade.key.KEY_0:
                if len(self.search_number) < 2:
                    self.search_number += "0"
            elif key == arcade.key.KEY_1:
                if len(self.search_number) < 2:
                    self.search_number += "1"
            elif key == arcade.key.KEY_2:
                if len(self.search_number) < 2:
                    self.search_number += "2"
            elif key == arcade.key.KEY_3:
                if len(self.search_number) < 2:
                    self.search_number += "3"
            elif key == arcade.key.KEY_4:
                if len(self.search_number) < 2:
                    self.search_number += "4"
            elif key == arcade.key.KEY_5:
                if len(self.search_number) < 2:
                    self.search_number += "5"
            elif key == arcade.key.KEY_6:
                if len(self.search_number) < 2:
                    self.search_number += "6"
            elif key == arcade.key.KEY_7:
                if len(self.search_number) < 2:
                    self.search_number += "7"
            elif key == arcade.key.KEY_8:
                if len(self.search_number) < 2:
                    self.search_number += "8"
            elif key == arcade.key.KEY_9:
                if len(self.search_number) < 2:
                    self.search_number += "9"
            elif key == arcade.key.BACKSPACE:
                self.search_number = self.search_number[:-1]

            if key == arcade.key.L and self.search_number != "":
                found = binary_search(int(self.search_number), self.buff_list)

                if found != -1:
                    self.edit_pointer(found)
                self.search_menu = False
                self.search_number = ""

            elif key == arcade.key.K:
                self.search_menu = False
                self.search_number = ""

        if key == arcade.key.Q or self.sort_menu:
            self.sort_menu = True
            self.search_menu = False
            if key == arcade.key.L:
                self.buff_list = merge_sort(self.buff_list)
                self.sort_menu = False
            elif key == arcade.key.K:
                self.sort_menu = False


def main():
    game = MyGame(width, height, "Buffs")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
