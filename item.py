import arcade
import loz
import random
import battle


class Item:
    """ Class for items
    Attributes:
            name(str) = Name of item
            amount(int): Number of item held
            effect(str): Effect of item
    """
    def __init__(self, name: str, amount: int, effect: str):
        self.name = name
        self.amount = amount
        self.effect = effect

    def use(self, game: arcade.Window, poke):
        if self.amount >= 1:
            if self.name == "Potion":
                poke.cur_stats[0] += 20
                if poke.cur_stats[0] > poke.stats[0]:
                    poke.cur_stats[0] = poke.stats[0]
                if game.cur_screen == "battle":
                    game.battle_msg.append(f"{poke.name} is now at {poke.cur_stats[0]} hp")
            elif self.name == "Super Potion":
                poke.cur_stats[0] += 50
                if poke.cur_stats[0] > poke.stats[0]:
                    poke.cur_stats[0] = poke.stats[0]
                if game.cur_screen == "battle":
                    game.battle_msg.append(f"{poke.name} is now at {poke.cur_stats[0]} hp")
            elif self.name == "Steroids":
                poke.cur_stats[1] += 20
                if game.cur_screen == "battle":
                    game.battle_msg.append(f"{poke.name}'s' attack is now at {poke.cur_stats[1]}")
            elif self.name == "Leg Day":
                if game.cur_screen == "battle":
                    game.battle_msg.append(f"{poke.name}'s' speed is now at {poke.cur_stats[3]}")
                poke.cur_stats[3] += 20
            self.amount -= 1

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
    """Class for pokeballs; inherits from Item class"""
    def __init__(self, name, amount, effect):
        super().__init__(name, amount, effect)

    def ball_use(self, player, poke):
        if self.name == "poke ball" and self.amount != 0:
            if random.randrange(4) == 0:
                player.player_sprite.catch(player, poke)
                player.battle_caught = True
            else:
                player.battle_msg.append(f"failed to catch {poke.name}")
            self.amount -= 1
        elif self.name == "great ball" and self.amount != 0:
            if random.randrange(2) == 0:
                player.player_sprite.catch(player, poke)
                player.battle_caught = True
            else:
                player.battle_msg.append(f"failed to catch {poke.name}")
            self.amount -= 1
        elif self.name == "master ball" and self.amount != 0:
            player.player_sprite.catch(player, poke)
            self.amount -= 1
            player.battle_caught = True

    @classmethod
    def pokeball(cls):
        item = cls("poke ball", 10, "25% catch rate")
        item.texture = arcade.load_texture("images/pokeballs/pokeball.png")
        return item

    @classmethod
    def greatball(cls):
        item = cls("great ball", 5, "50% catch rate")
        item.texture = arcade.load_texture("images/pokeballs/great_ball.png")
        return item

    @classmethod
    def masterball(cls):
        item = cls("master ball", 1, "100% catch rate")
        item.texture = arcade.load_texture("images/pokeballs/master_ball.png")
        return item


if __name__ == "__main__":
    p = loz.Player()
    pass
