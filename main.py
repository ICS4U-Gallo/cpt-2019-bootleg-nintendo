import arcade

import settings

from menu_start import MenuView

tex_right = 1
tex_left = 0


class Player(arcade.Sprite):

    def __init__(self):
        super().__init__()
        # Load a left facing texture and a right facing texture.
        # mirrored=True will mirror the image we load.
        texture = arcade.load_texture("images/character.png",
                                      mirrored=True, scale=sprite_scale)
        self.textures.append(texture)
        texture = arcade.load_texture("images/character.png",
                                      scale=sprite_scale)
        self.textures.append(texture)

        # By default, face right.
        self.face_dir = 1
        # 0 = up, 1 = right, 2 = down, 3 = left
        self.set_texture(tex_right)

        self.bag = []
        self.pokemon = []
        self.pokemon_bag = []

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


class Director(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.view_index = 0
        self.views = [
            MenuView,
            Chapter1View
        ]
        self.next_view()

    def next_view(self):
        next_view = self.views[self.view_index]()
        next_view.director = self
        self.show_view(next_view)
        self.view_index = (self.view_index + 1) % len(self.views)


def main():
    window = Director(settings.WIDTH, settings.HEIGHT, "CPT Structure")
    arcade.run()


if __name__ == "__main__":
    main()
