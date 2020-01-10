import images
import arcade

types = ["fire", "water", "grass", "normal"]


class Move:
    def __init__(self, name, pwr, type_, pp, *status):
        self.name = name
        self.pwr = pwr
        self.type = type_
        self.cur_pp = pp
        self.pp = pp
        self.status = [*status]

    def check_pp(self):
        if self.cur_pp == 0:
            return False
        else:
            self.cur_pp -= 1
            return True

    def apply_effect(self, poke, opp):
        if self.status[0] == 0:
            return
        elif self.status[0] == 1:
            print(self.status[1], self.status[2])
            poke.cur_stats[self.status[1]] += self.status[2]
        elif self.status[0] == 2:
            opp.cur_stats[self.status[1]] += self.status[2]

    @classmethod
    def Tackle(cls):
        return cls("Bump", 40, "normal", 40, 0)

    @classmethod
    def Leer(cls):
        return cls("look suggestively", 0, "normal", 40, 2, 2, -10)

    @classmethod
    def Growl(cls):
        return cls("yap", 0, "normal", 40, 2, 1, -10)


class Pokemon(arcade.Sprite):
    def __init__(self, num, name, types, lvl, hp, atk, def_, spd):
        super().__init__()
        self.num = num
        self.name = name
        self.type = types
        self.lvl = lvl
        self.cur_stats = [hp, atk, def_]
        self.stats = [hp, atk, def_, spd]
        self.battle_c = 0

    def levelup(self):
        self.lvl += 1
        self.cur_stats[0] += self.stats[0]*1.5
        for i in range(4):
            self.stats[i] = round(self.stats[i] * 51/50)
        if self.cur_stats[0] > self.stats[0]:
            self.cur_stats[0] = self.stats[0]

    def type_modif(self, opp, move):
        if ((move.type == "fire" and opp.type == "grass") or
                (move.type == "grass" and opp.type == "water") or
                (move.type == "water" and opp.type == "fire")):
            return 1.5
        elif ((move.type == "fire" and opp.type == "water") or
                (move.type == "water" and opp.type == "grass") or
                (move.type == "grass" and opp.type == "fire")):
            return 0.5
        else:
            return 1

    def attack(self, opp, move):
        print(f"\n{self.name} uses {move.name}")
        modif = self.type_modif(opp, move)
        move.apply_effect(self, opp)
        dmg = round(((((self.lvl/2+2)*move.pwr*(self.cur_stats[1]
                    / opp.cur_stats[2]))/50)+2)*modif)
        opp.cur_stats[0] -= dmg
        print(f"{self.name} does {dmg} damage to {opp.name}.")

    def check_dead(self):
        if self.cur_stats[0] <= 0:
            print(f"{self.name} is dead")
            return True
        else:
            return False

    def update(self):
        if self.battle_c % 10 == 0:
            self.levelup()

    def __str__(self):
        return f"{self.name, self.type, *self.cur_stats}"

    @classmethod
    def Charmander(cls):
        poke = cls(1, "Charmander", "fire", 1, 39, 52, 43, 65)
        poke.texture = arcade.load_texture("images/charmander.png")
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        return poke

    @classmethod
    def Squirtle(cls):
        poke = cls(4, "Squirtle", "water", 1, 44, 48, 65, 43)
        poke.texture = arcade.load_texture("images/squirtle.jpg")
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        return poke

    @classmethod
    def Bulbasaur(cls):
        poke = cls(7, "Bulbasaur", "grass", 1, 45, 49, 49, 45)
        poke.texture = arcade.load_texture("images/bulbasaur.png")
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        return poke

    @classmethod
    def IceCream(cls):
        poke = cls(10, "Ice cream", "water", 1, 36, 50, 50, 44)
        poke.texture = arcade.load_texture("images/literal_ice_cream.jpg")
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        return poke

    @classmethod
    def Garbage(cls):
        poke = cls(13, "Literal Garbage", "grass", 1, 50, 50, 62, 67)
        poke.texture = arcade.load_texture("images/garbage.jpg")
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        return poke

    @classmethod
    def torkoal(cls):
        poke = cls(14, "China's air", "fire", 1, 70, 85, 140, 20)
        poke.texture = arcade.load_texture("images/torkoal.jpg")
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        return poke

    @classmethod
    def Klefki(cls):
        poke = cls(15, "Your missing keys", "normal", 1, 57, 80, 91, 75)
        poke.texture = arcade.load_texture("images/key.jpg")
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        return poke

    @classmethod
    def Magikarp(cls):
        poke = cls(16, "Dead fish", "water", 1, 100, 100, 100, 100)
        poke.texture = arcade.load_texture("images/magikarp.jpg")
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        return poke


def main():
    pass


if __name__ == "__main__":
    main()
