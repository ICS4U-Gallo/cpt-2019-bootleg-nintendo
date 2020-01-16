import arcade
import random

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
            poke.cur_stats[self.status[1]] += self.status[2]
        elif self.status[0] == 2:
            opp.cur_stats[self.status[1]] += self.status[2]
            if opp.cur_stats[self.status[1]] <= 0:
                opp.cur_stats[self.status[1]] = 1

    @classmethod
    def Tackle(cls):
        return cls("Bump", 40, "normal", 40, 0)

    @classmethod
    def Leer(cls):
        return cls("Leer", 0, "normal", 40, 2, 2, -10)

    @classmethod
    def Growl(cls):
        return cls("yap", 0, "normal", 40, 2, 1, -10)

    @classmethod
    def WaterGun(cls):
        return cls("Not Splash", 80, "water", 40, 0)

    @classmethod
    def FlameThrower(cls):
        return cls("FlameThrower", 80, "fire", 40, 0)

    @classmethod
    def LeafBeam(cls):
        return cls("LeafBeam", 80, "grass", 40, 0)

    @classmethod
    def Bite(cls):
        return cls("Bite", 120, "normal", 40, 0)

    @classmethod
    def Splash(cls):
        return cls("Splash", 200, "water", 100, 0)


class Pokemon(arcade.Sprite):
    def __init__(self, num, name, types, lvl, hp, atk, def_, spd):
        super().__init__()
        self.num = num
        self.name = name
        self.type = types
        self.lvl = lvl
        self.cur_stats = [hp, atk, def_]
        self.stats = [hp, atk, def_, spd]
        self.avalible_move = {}
        self.avalible_evo = {}
        self.killcount = 0

    def addlevel(self, lvl):
        for i in range(lvl):
            self.levelup()

    def levelup(self):
        self.lvl += 1
        for i in range(3):
            self.stats[i] = round(self.stats[i] * 51/50)
        for i in range(3):
            self.cur_stats[i] += round(self.stats[i]*1.5*0.02)
            if self.cur_stats[i] > self.stats[i]:
                self.cur_stats[i] = self.stats[i]
        if self.lvl in self.avalible_move.keys():
            self.moves.append(self.avalible_move[self.lvl])
        if self.lvl in self.avalible_evo.keys():
            self.evo()

    def evo(self):
        for i in range(3):
            self.stats[i] = round(self.stats[i]*1.25)
            self.cur_stats[i] = self.stats[i]
        self.stats[3] = round(self.stats[3]*1.25)
        self.num = self.avalible_evo[self.lvl].num
        self.name = self.avalible_evo[self.lvl].name
        self.texture = self.avalible_evo[self.lvl].texture

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

    def is_dead(self):
        if self.cur_stats[0] <= 0:
            self.cur_stats[0] = 0
            return True
        else:
            return False

    def gainkill(self):
        self.killcount += 1
        if self.killcount == 1:
            self.killcount = 0
            self.levelup()

    def update(self):
        pass
        
    def __str__(self):
        return f"{self.name, self.type, self.lvl, *self.cur_stats}"

    @classmethod
    def random_poke(cls):
        rng = random.randrange(7)
        if rng == 0:
            return cls.Charmander()
        elif rng == 1:
            return cls.Squirtle()
        elif rng == 2:
            return cls.Bulbasaur()
        elif rng == 3:
            return cls.IceCream()
        elif rng == 4:
            return cls.Garbage()
        elif rng == 5:
            return cls.Torkoal()
        elif rng == 6:
            return cls.Klefki()

    @classmethod
    def Charmander(cls):
        poke = cls(1, "Charmander", "fire", 1, 39, 52, 43, 65)
        poke.texture = arcade.load_texture("images/poke_images/charmander.png")
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        poke.avalible_move = {12: Move.FlameThrower()}
        poke.avalible_evo = {25: Pokemon.Charm2()}
        return poke

    @classmethod
    def Charm2(cls):
        poke = cls(2, "Slightly Better Charmnder", "fire", None, None, None, None, None)
        poke.texture = arcade.load_texture("images/poke_images/charizard.jpg")
        return poke


    @classmethod
    def Squirtle(cls):
        poke = cls(3, "Squirtle", "water", 1, 44, 48, 65, 43)
        poke.texture = arcade.load_texture("images/poke_images/squirtle.jpg")
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        poke.avalible_move = {12: Move.WaterGun()}
        poke.avalible_evo = {25: Pokemon.Squir2()}
        return poke

    @classmethod
    def Squir2(cls):
        poke = cls(4, "Slightly Better Squirtle", "water", None, None, None, None, None)
        poke.texture = arcade.load_texture("images/poke_images/squirtle_evo.jpg")
        return poke

    @classmethod
    def Bulbasaur(cls):
        poke = cls(5, "Bulbasaur", "grass", 1, 45, 49, 49, 45)
        poke.texture = arcade.load_texture("images/poke_images/bulbasaur.jpg")
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        poke.avalible_move = {12: Move.LeafBeam()}
        poke.avalible_evo = {25: Pokemon.Bulb2()}
        return poke

    @classmethod
    def Bulb2(cls):
        poke = cls(6, "Slightly Better Bulbasaur", "grass", None, None, None, None, None)
        poke.texture = arcade.load_texture("images/poke_images/venesaur.jpg")
        return poke

    @classmethod
    def IceCream(cls):
        poke = cls(7, "Ice cream", "water", 1, 36, 50, 50, 44)
        poke.texture = arcade.load_texture("images/poke_images/"
                                           "literal_ice_cream.jpg")
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        poke.avalible_move = {12: Move.WaterGun()}
        poke.avalible_evo = {25: Pokemon.Ice2()}
        return poke

    @classmethod
    def Ice2(cls):
        poke = cls(8, "Still an Ice Cream", "water", None, None, None, None, None)
        poke.texture = arcade.load_texture("images/poke_images/fallen_ice_cream.jpg")
        return poke

    @classmethod
    def Garbage(cls):
        poke = cls(9, "Literal Garbage", "grass", 1, 50, 50, 62, 67)
        poke.texture = arcade.load_texture("images/poke_images/garbage.jpg")
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        poke.avalible_move = {12: Move.LeafBeam()}
        return poke

    @classmethod
    def Torkoal(cls):
        poke = cls(10, "China's air", "fire", 1, 70, 85, 140, 20)
        poke.texture = arcade.load_texture("images/poke_images/torkoal.jpg")
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        poke.avalible_move = {12: Move.FlameThrower()}
        return poke

    @classmethod
    def Klefki(cls):
        poke = cls(11, "Your missing keys", "normal", 1, 57, 80, 91, 75)
        poke.texture = arcade.load_texture("images/poke_images/key.jpg")
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        poke.avalible_move = {12: Move.Bite()}
        return poke

    @classmethod
    def Magikarp(cls):
        poke = cls(12, "Dead fish", "water", 1, 100, 100, 100, 100)
        poke.texture = arcade.load_texture("images/poke_images/magikarp.jpg")
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        poke.avalible_move = {15: Move.Splash()}
        poke.avalible_evo = {20: Pokemon.PinkMagikarp()}
        return poke

    @classmethod
    def PinkMagikarp(cls):
        poke = cls(13, "Slightly Less Dead fish", "water", None, None, None, None, None)
        poke.texture = arcade.load_texture("images/poke_images/dead_fish.png", mirrored=True ,scale=0.25)
        return poke


poke_list = [Pokemon.Charmander(), Pokemon.Squirtle(),
             Pokemon.Bulbasaur(), Pokemon.IceCream(),
             Pokemon.Garbage(), Pokemon.Torkoal(),
             Pokemon.Klefki(), Pokemon.Magikarp()]


def main():
    pass


if __name__ == "__main__":
    main()

