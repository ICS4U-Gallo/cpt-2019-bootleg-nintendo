import arcade
import loz
import random
import battle


class Item:
    def __init__(self, name: str, amount: int, effect: str):
        self.name = name
        self.amount = amount
        self.effect = effect
        self.amount = amount

    def use(self, poke):
        if self.name == "Potion":
            poke.cur_stats[0] += 20
            if poke.cur_stats[0] > poke.stats[0]:
                poke.cur_stats[0] = poke.stats[0]
        elif self.name == "Super Potion":
            poke.cur_stats[0] += 20
            if poke.cur_stats[0] > poke.stats[0]:
                poke.cur_stats[0] = poke.stats[0]
        elif self.name == "Steroids":
            poke.atk += 20
        elif self.name == "Leg Day":
            poke.spd += 20

    @classmethod
    def potion(cls):
        item = cls("Potion", 5, "Heal hp by 20")
        item.texture = arcade.load_texture("images/heal_images/potion.jpg")
        return item

    @classmethod
    def superpotion(cls):
        item = cls("Super Potion", 5, "Heal hp by 100")
        item.texture = arcade.load_texture("images/heal_images/super_potion.jpg")
        return item

    @classmethod
    def steroids(cls):
        item = cls("Steroids", 5, "Increase attack by 20")
        item.texture = arcade.load_texture("images/buff_images/steroid.jpg")
        return item

    @classmethod
    def leg_day(cls):
        item = cls("Leg Day", 5, "Increase speed by 20")
        item.texture = arcade.load_texture("images/buff_images/legs.jpg")
        return item


class PokeBall(Item):
    def __init__(self, name, amount, effect):
        super().__init__(name, amount, effect)

    def use(self, player, poke):
        if self.name == "pokeball" and self.amount != 0:
            if random.randrange(4) == 0:
                player.pokemon.append(poke)
                player.cur_screen = "game"
            else:
                player.cur_screen = "battle"
            self.amount -= 1
        elif self.name == "great ball" and self.amount != 0:
            if random.randrange(2) == 0:
                player.pokemon.append(poke)
                player.cur_screen = "game"
            else:
                player.cur_screen = "battle"
            self.amount -= 1
        elif self.name == "master ball" and self.amount != 0:
            player.pokemon.append(poke)
            self.amount -= 1
            player.cur_screen = "game"

    @classmethod
    def pokeball(cls):
        item = cls("pokeball", 0, "25% catch rate")
        item.texture = arcade.load_texture("images/pokeballs/pokeball.png")
        return item

    @classmethod
    def greatball(cls):
        item = cls("great ball", 0, "50% catch rate")
        item.texture = arcade.load_texture("images/pokeballs/great_ball.png")
        return item

    @classmethod
    def masterball(cls):
        item = cls("master ball", 0, "100% catch rate")
        item.texture = arcade.load_texture("images/pokeballs/master_ball.png")
        return item


if __name__ == "__main__":
    p = loz.Player()
    pass
