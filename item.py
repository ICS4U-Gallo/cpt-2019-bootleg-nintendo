import arcade
import loz
import random


class Item:
    def __init__(self, name: str, effect: str):
        self.name = name
        self.effect = effect

    def use(self, poke):
        if self.name == "potion":
            poke.cur_stats[0] += 20
            if poke.cur_stats[0] > poke.stats[0]:
                poke.cur_stats[0] = poke.stats[0]
        elif self.name == "super potion":
            poke.cur_stats[0] += 20
            if poke.cur_stats[0] > poke.stats[0]:
                poke.cur_stats[0] = poke.stats[0]
        elif self.name == "Steroids":
            poke.atk += 20
        elif self.name == "Leg Day":
            poke.spd += 20

    @classmethod
    def potion(cls):
        item = cls("potion", "Heal hp by 20")
        item.texture = arcade.load_texture("images/heal_images/potion.jpg")
        return item

    @classmethod
    def superpotion(cls):
        item = cls("super potion", "Heal hp by 100")
        item.texture = arcade.load_texture("images/heal_images/potion.jpg")
        return item

    @classmethod
    def steroids(cls):
        item = cls("Steroids", "Increase attack by 20")
        item.texture = arcade.load_texture("images/buff_images/steroid.jpg")
        return item

    @classmethod
    def leg_day(cls):
        item = cls("Leg Day", "Increase speed by 20")
        item.texture = arcade.load_texture("images/buff_images/legs.jpg")
        return item


class PokeBall(Item):
    def __init__(self, name, effect):
        super().__init__(name, effect)

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
        item = cls("pokeball", "25% to catch pokemon")
        item.texture = arcade.load_texture("images/pokeballs/pokeball.png")
        return item

    @classmethod
    def greatball(cls):
        item = cls("great ball", "50% to catch pokemon")
        item.texture = arcade.load_texture("images/pokeballs/great_ball.png")
        return item

    @classmethod
    def masterball(cls):
        item = cls("master ball", "100% to catch pokemon")
        item.texture = arcade.load_texture("images/pokeballs/master_ball.png")
        return item


if __name__ == "__main__":
    p = loz.Player()
    p.bag.append(item)
