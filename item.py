import arcade
import loz
import random


class Item:
    def __init__(self, name: str, amount: int, effect: str):
        self.name = name
        self.amount = amount
        self.effect = effect

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
    def __init__(self, name, effect, amount):
        super().__init__(name, effect)
        self.amount = amount

    def use(self, player, poke):
        if self.name == "pokeball":
            if random.randrange(4) == 0:
                player.pokemon.append(poke)
        elif self.name == "great ball":
            if random.randrange(2) == 0:
                player.pokemon.append(poke)
        elif self.name == "master ball":
            player.pokemon.append(poke)

    @classmethod
    def pokeball(cls):
        item = cls("pokeball", "25% catch rate", 0)
        item.texture = arcade.load_texture("images/pokeballs/pokeball.png")
        return item

    @classmethod
    def greatball(cls):
        item = cls("great ball", "50% catch rate", 0)
        item.texture = arcade.load_texture("images/pokeballs/great_ball.png")
        return item

    @classmethod
    def masterball(cls):
        item = cls("master ball", "100% catch rate", 0)
        item.texture = arcade.load_texture("images/pokeballs/master_ball.png")
        return item


if __name__ == "__main__":
    p = loz.Player()
    p.bag.append(item)
