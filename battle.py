import arcade
import settings


def check_first(poke, opp):
    if poke1.stats[3] > poke2.stats[3]:
        return 0
    else:
        return 1


def combat(poke, opp):
    move_pokemon = check_first()
    while True:
        if move_pokemon % 2 == 0:
            move = choose_move()
            poke.attack(opp, move)
        else:
            move = None
            opp.attack(poke, move)


class BattleView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        bg = arcade.load_texture("images/battle_background.jpg")
        arcade.draw_texture_rectangle(settings.WIDTH // 2,
                                      settings.HEIGHT // 2,
                                      settings.WIDTH, settings.HEIGHT, bg
                                      )

    def on_key_press(self, key, modifiers):
        pass


if __name__ == "__main__":
    from utils import FakeDirector
    window = arcade.Window(settings.WIDTH, settings.HEIGHT)
    my_view = BattleView()
    my_view.director = FakeDirector(close_on_next_view=True)
    window.show_view(my_view)
    arcade.run()
