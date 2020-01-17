import arcade
import random

types = ["fire", "water", "grass", "normal"]

class Move:
    def __init__(self, name, pwr, type_, pp, status):
        self._name = name
        self._pwr = pwr
        self._type = type_
        self._cur_pp = pp
        self._pp = pp
        self._status = status

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_pwr(self, pwr):
        self._pwr = pwr

    def get_pwr(self):
        return self._pwr

    def set_type(self, type):
        self._type = type

    def get_type(self):
        return self._type

    def set_cur_pp(self, cur_pp):
        self._cur_pp = cur_pp

    def get_cur_pp(self):
        return self._cur_pp

    def set_pp(self, pp):
        self._pp = pp

    def get_pp(self):
        return self._pp

    def set_status(self, status):
        self._status = status

    def get_status(self):
        return self._status

    def check_pp(self):
        if self.get_cur_pp() == 0:
            return False
        else:
            self.set_cur_pp(self.get_cur_pp()-1)
            return True

    def apply_effect(self, poke, opp):
        if self.get_status() == None:
            return
        elif self.get_status() == "reduce def":
            opp.cur_stats[2] -= 10
            if opp.cur_stats[2] <= 0:
                opp.cur_stats[2] = 1
        elif self.get_status() == "reduce atk":
            opp.cur_stats[1] -= 10
            if opp.cur_stats[1] <= 0:
                opp.cur_stats[1] = 1
        elif self.get_status() == "burn":
            opp.effect = "burn"

    @classmethod
    def Tackle(cls):
        return cls("Bump", 40, "normal", 40, None)

    @classmethod
    def Leer(cls):
        return cls("Leer", 0, "normal", 40, "reduce def")

    @classmethod
    def Growl(cls):
        return cls("yap", 0, "normal", 40, "reduce atk")

    @classmethod
    def WaterGun(cls):
        return cls("Not Splash", 80, "water", 40, None)

    @classmethod
    def FlameThrower(cls):
        return cls("FlameThrower", 60, "fire", 40, "burn")

    @classmethod
    def LeafBeam(cls):
        return cls("LeafBeam", 80, "grass", 40, None)

    @classmethod
    def Bite(cls):
        return cls("Bite", 80, "normal", 40, None)

    @classmethod
    def Splash(cls):
        return cls("Splash", 100, "water", 100, None)


class Pokemon(arcade.Sprite):
    def __init__(self, num, name, types, lvl, hp, atk, def_, spd):
        super().__init__()
        self.num = num
        self.name = name
        self.type = types
        self.lvl = lvl
        self.cur_stats = [hp, atk, def_]
        self.stats = [hp, atk, def_, spd]
        self.effect = None
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
        if ((move.get_type() == "fire" and opp.type == "grass") or
                (move.get_type() == "grass" and opp.type == "water") or
                (move.get_type() == "water" and opp.type == "fire")):
            return 1.5
        elif ((move.get_type() == "fire" and opp.type == "water") or
                (move.get_type() == "water" and opp.type == "grass") or
                (move.get_type() == "grass" and opp.type == "fire")):
            return 0.5
        else:
            return 1

    def check_effect(self):
        if self.effect == "burn":
            self.cur_stats[0] = round(self.cur_stats[0]*0.95)
            self.effect = None

    def attack(self, opp, move, game):
        game.battle_msg.append(f"\n{self.name} uses {move.get_name()}")
        modif = self.type_modif(opp, move)
        move.apply_effect(self, opp)
        dmg = round(((((self.lvl/2+2)*move.get_pwr()*(self.cur_stats[1]
                    / opp.cur_stats[2]))/50)+2)*modif)
        opp.cur_stats[0] -= dmg
        opp.check_effect()
        game.battle_msg.append(f"{self.name} does {dmg} damage to {opp.name}.")

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
        poke.texture = arcade.load_texture("images/poke_images/charizard.jpg", scale=0.4)
        return poke


    @classmethod
    def Squirtle(cls):
        poke = cls(3, "Squirtle", "water", 1, 44, 48, 65, 43)
        poke.texture = arcade.load_texture("images/poke_images/squirtle.jpg", scale=0.9)
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        poke.avalible_move = {12: Move.WaterGun()}
        poke.avalible_evo = {25: Pokemon.Squir2()}
        return poke

    @classmethod
    def Squir2(cls):
        poke = cls(4, "Slightly Better Squirtle", "water", None, None, None, None, None)
        poke.texture = arcade.load_texture("images/poke_images/squirtle_evo.jpg", scale=0.75)
        return poke

    @classmethod
    def Bulbasaur(cls):
        poke = cls(5, "Bulbasaur", "grass", 1, 45, 49, 49, 45)
        poke.texture = arcade.load_texture("images/poke_images/bulbasaur.jpg", scale=0.8)
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        poke.avalible_move = {12: Move.LeafBeam()}
        poke.avalible_evo = {25: Pokemon.Bulb2()}
        return poke

    @classmethod
    def Bulb2(cls):
        poke = cls(6, "Slightly Better Bulbasaur", "grass", None, None, None, None, None)
        poke.texture = arcade.load_texture("images/poke_images/venesaur.jpg", scale=0.75)
        return poke

    @classmethod
    def IceCream(cls):
        poke = cls(7, "Ice cream", "water", 1, 36, 50, 50, 44)
        poke.texture = arcade.load_texture("images/poke_images/"
                                           "literal_ice_cream.jpg", scale=0.9)
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        poke.avalible_move = {12: Move.WaterGun()}
        poke.avalible_evo = {25: Pokemon.Ice2()}
        return poke

    @classmethod
    def Ice2(cls):
        poke = cls(8, "Still an Ice Cream", "water", None, None, None, None, None)
        poke.texture = arcade.load_texture("images/poke_images/fallen_ice_cream.jpg", scale=0.6)
        return poke

    @classmethod
    def Garbage(cls):
        poke = cls(9, "Literal Garbage", "grass", 1, 50, 50, 62, 67)
        poke.texture = arcade.load_texture("images/poke_images/garbage.jpg", scale=1.15)
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

