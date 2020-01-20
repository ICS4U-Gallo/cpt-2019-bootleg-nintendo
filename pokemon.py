import arcade
import random
import typing

types = ["fire", "water", "grass", "normal"]


class Move:
    """Move class
    Attributes:
        name(str): Name of the move
        pwr(int): Power of the move
        type_(str): Type of the move
        cur_pp(int): Current power point of the move
        pp(int): Max power point of the move
        status(str): Effect applied of the move
    """
    def __init__(self, name: str, pwr: int, type_: str, pp: int, status: str):
        self._name = name
        self._pwr = pwr
        self._type = type_
        self._cur_pp = pp
        self._pp = pp
        self._status = status

    def set_name(self, name: str) -> None:
        self._name = name

    def get_name(self) -> str:
        return self._name

    def set_pwr(self, pwr: int) -> None:
        self._pwr = pwr

    def get_pwr(self) -> int:
        return self._pwr

    def set_type(self, type: str) -> None:
        self._type = type

    def get_type(self) -> str:
        return self._type

    def set_cur_pp(self, cur_pp: int) -> None:
        self._cur_pp = cur_pp

    def get_cur_pp(self) -> int:
        return self._cur_pp

    def set_pp(self, pp: int) -> None:
        self._pp = pp

    def get_pp(self) -> int:
        return self._pp

    def set_status(self, status: str) -> None:
        self._status = status

    def get_status(self) -> str:
        return self._status

    def check_pp(self) -> bool:
        """Check if there is any pp for the move"""
        if self.get_cur_pp() == 0:
            return False
        else:
            return True

    def apply_effect(self, poke, opp) -> None:
        """Apply effect of the move to enemy"""
        if self.get_status() is None:
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
    def Tackle(cls) -> "Move":
        return cls("Bump", 40, "normal", 40, None)

    @classmethod
    def Leer(cls) -> "Move":
        return cls("Leer", 0, "normal", 40, "reduce def")

    @classmethod
    def Growl(cls) -> "Move":
        return cls("yap", 0, "normal", 40, "reduce atk")

    @classmethod
    def WaterGun(cls) -> "Move":
        return cls("Not Splash", 80, "water", 40, None)

    @classmethod
    def FlameThrower(cls) -> "Move":
        return cls("FlameThrower", 60, "fire", 40, "burn")

    @classmethod
    def LeafBeam(cls) -> "Move":
        return cls("LeafBeam", 80, "grass", 40, None)

    @classmethod
    def Bite(cls) -> "Move":
        return cls("Bite", 80, "normal", 40, None)

    @classmethod
    def Splash(cls) -> "Move":
        return cls("Splash", 100, "water", 100, None)


class Pokemon(arcade.Sprite):
    """Pokemon class
    Attributes:
        num(int): Pokemon ID
        name(str): Name of the pokemon
        type(str): Type of the pokemon
        lvl(int): Level of the pokemon
        cur_stats(List[int]): Current hp/attack/defence/speed of the pokemon
        stats(List[int]): Max hp/attack/defence/speed of the pokemon
        effect(str): Effect applied from enemy moves
        moves(List["Move"]): List of moves available to use
        available_move(dict): Available moves for pokemon to learn
        available_evo(dict): Available evolve of the pokemon
        killcount(int): Amount of kills pokemon have since leveled up
    """
    def __init__(self, num, name, types, lvl, hp, atk, def_, spd):
        super().__init__()
        self.num = num
        self.name = name
        self.type = types
        self.lvl = lvl
        self.cur_stats = [hp, atk, def_, spd]
        self.stats = [hp, atk, def_, spd]
        self.effect = None
        self.moves = []
        self.available_move = {}
        self.available_evo = {}
        self.killcount = 0

    def addlevel(self, lvl: int) -> None:
        """Add more than 1 level to pokemon"""
        for i in range(lvl):
            self.levelup()

    def levelup(self, game: "arcade.Window"=None) -> None:
        """Level up pokemon and check for available moves/evolves"""
        self.lvl += 1
        if game is not None:
            game.battle_msg.append(f"{self.name} level up to lvl {self.lvl}")
        for i in range(3):
            self.stats[i] = round(self.stats[i] * 51/50)
        for i in range(3):
            self.cur_stats[i] += round(self.stats[i]*1.5*0.02)
            if self.cur_stats[i] > self.stats[i]:
                self.cur_stats[i] = self.stats[i]
        if self.lvl in self.available_move.keys():
            self.moves.append(self.available_move[self.lvl])
        if self.lvl in self.available_evo.keys():
            if game is not None:
                game.battle_msg.append(f"{self.name} evolved")
            self.evo()

    def evo(self) -> None:
        """Evolve pokemon"""
        for i in range(3):
            self.stats[i] = round(self.stats[i]*1.25)
            self.cur_stats[i] = self.stats[i]
        self.stats[3] = round(self.stats[3]*1.25)
        self.cur_stats[3] = self.stats[3]
        self.num = self.available_evo[self.lvl].num
        self.name = self.available_evo[self.lvl].name
        self.texture = self.available_evo[self.lvl].texture

    def type_modif(self, opp: "Pokemon", move: "Move") -> float:
        """Check for type modifier"""
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

    def check_effect(self) -> None:
        """Check current effect applied on pokemon"""
        if self.effect == "burn":
            self.cur_stats[0] = round(self.cur_stats[0]*0.95)

    def attack(self, opp: "Pokemon", move: "Move", game: "arcade.Window"
               ) -> None:
        """Logic when pokemon attack an enemy"""
        game.battle_msg.append(f"\n{self.name} uses {move.get_name()}")
        modif = self.type_modif(opp, move)
        move.apply_effect(self, opp)
        dmg = round(((((self.lvl / 2+2)*move.get_pwr()*(self.cur_stats[1] /
                    opp.cur_stats[2]))/50)+2)*modif)
        opp.cur_stats[0] -= dmg
        move.set_cur_pp(move.get_cur_pp()-1)
        opp.check_effect()
        game.battle_msg.append(f"{self.name} does {dmg} damage to {opp.name}.")

    def is_dead(self) -> bool:
        """Check whether pokemon is dead or not"""
        if self.cur_stats[0] <= 0:
            self.cur_stats[0] = 0
            return True
        else:
            return False

    def gainkill(self, game: "arcade.Window") -> None:
        """Add kill to killcount and check for level up"""
        self.killcount += 1
        if self.killcount == 1:
            self.killcount = 0
            self.levelup(game)

    def __str__(self) -> str:
        return f"{self.name, self.type, self.lvl, *self.cur_stats}"

    @classmethod
    def random_poke(cls) -> "Pokemon":
        """Give a random non-evolved pokemon (not include magikarp)"""
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
    def Charmander(cls) -> "Pokemon":
        poke = cls(1, "Charmander", "fire", 1, 39, 52, 43, 65)
        poke.texture = arcade.load_texture("images/poke_images/charmander.png")
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        poke.available_move = {12: Move.FlameThrower()}
        poke.available_evo = {25: Pokemon.Charm2()}
        return poke

    @classmethod
    def Charm2(cls) -> "Pokemon":
        poke = cls(2, "Slightly Better Charmander", "fire", None, None, None,
                   None, None)
        poke.texture = arcade.load_texture("images/poke_images/charizard.jpg",
                                           scale=75/221)
        return poke

    @classmethod
    def Squirtle(cls) -> "Pokemon":
        poke = cls(3, "Squirtle", "water", 1, 44, 48, 65, 43)
        poke.texture = arcade.load_texture("images/poke_images/squirtle.jpg",
                                           scale=75/83)
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        poke.available_move = {12: Move.WaterGun()}
        poke.available_evo = {25: Pokemon.Squir2()}
        return poke

    @classmethod
    def Squir2(cls) -> "Pokemon":
        poke = cls(4, "Slightly Better Squirtle", "water", None, None, None,
                   None, None)
        poke.texture = arcade.load_texture(
                       "images/poke_images/squirtle_evo.jpg",
                       scale=50/71)
        return poke

    @classmethod
    def Bulbasaur(cls) -> "Pokemon":
        poke = cls(5, "Bulbasaur", "grass", 1, 45, 49, 49, 45)
        poke.texture = arcade.load_texture("images/poke_images/bulbasaur.jpg",
                                           scale=75/107)
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        poke.available_move = {12: Move.LeafBeam()}
        poke.available_evo = {25: Pokemon.Bulb2()}
        return poke

    @classmethod
    def Bulb2(cls) -> "Pokemon":
        poke = cls(6, "Slightly Better Bulbasaur", "grass", None, None, None,
                   None, None)
        poke.texture = arcade.load_texture("images/poke_images/venesaur.jpg",
                                           scale=150/233)
        return poke

    @classmethod
    def IceCream(cls) -> "Pokemon":
        poke = cls(7, "Ice cream", "water", 1, 36, 50, 50, 44)
        poke.texture = arcade.load_texture("images/poke_images/"
                                           "literal_ice_cream.jpg", scale=3/4)
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        poke.available_move = {12: Move.WaterGun()}
        poke.available_evo = {25: Pokemon.Ice2()}
        return poke

    @classmethod
    def Ice2(cls) -> "Pokemon":
        poke = cls(8, "Still an Ice Cream", "water", None, None, None, None,
                   None)
        poke.texture = arcade.load_texture(
                       "images/poke_images/fallen_ice_cream.jpg", scale=75/149)
        return poke

    @classmethod
    def Garbage(cls) -> "Pokemon":
        poke = cls(9, "Literal Garbage", "grass", 1, 50, 50, 62, 67)
        poke.texture = arcade.load_texture("images/poke_images/garbage.jpg")
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        poke.available_move = {12: Move.LeafBeam()}
        return poke

    @classmethod
    def Torkoal(cls) -> "Pokemon":
        poke = cls(10, "China's air", "fire", 1, 70, 85, 140, 20)
        poke.texture = arcade.load_texture("images/poke_images/torkoal.jpg",
                                           scale=25/24)
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        poke.available_move = {12: Move.FlameThrower()}
        return poke

    @classmethod
    def Klefki(cls) -> "Pokemon":
        poke = cls(11, "Your missing keys", "normal", 1, 57, 80, 91, 75)
        poke.texture = arcade.load_texture("images/poke_images/key.jpg")
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        poke.available_move = {12: Move.Bite()}
        return poke

    @classmethod
    def Magikarp(cls) -> "Pokemon":
        poke = cls(12, "Dead fish", "water", 1, 100, 100, 100, 100)
        poke.texture = arcade.load_texture("images/poke_images/magikarp.jpg",
                                           scale=15/16)
        poke.moves = [Move.Tackle(), Move.Leer(), Move.Growl()]
        poke.available_move = {15: Move.Splash()}
        poke.available_evo = {20: Pokemon.PinkMagikarp()}
        return poke

    @classmethod
    def PinkMagikarp(cls) -> "Pokemon":
        poke = cls(13, "Slightly Less Dead fish", "water", None, None, None,
                   None, None)
        poke.texture = arcade.load_texture("images/poke_images/dead_fish.png",
                                           mirrored=True, scale=50/249)
        return poke


poke_list = [Pokemon.Charmander(), Pokemon.Squirtle(),
             Pokemon.Bulbasaur(), Pokemon.IceCream(),
             Pokemon.Garbage(), Pokemon.Torkoal(),
             Pokemon.Klefki(), Pokemon.Magikarp()]


def main():
    pass


if __name__ == "__main__":
    main()
