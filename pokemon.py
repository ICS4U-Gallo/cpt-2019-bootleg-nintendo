import poke_move

types = ["fire", "water", "grass", "normal"]


class Move:
    def __init__(self, name, pwr, type, pp, status):
        self.name = name
        self.pwr = pwr
        self.pp = pp
        self.status = status


class Tackle(Move):
    def __init__(self):
        super.__init__("Bump", 40, "normal", 40, None)


class Leer(Move):
    def __init__(self):
        super.__init__("look suggestively", 0, "normal", 40, "reduce def")


class Growl(Move):
    def __init__(self):
        super.__init__("yap", 0, "normal", 40, "reduce atk")


class Pokemon:
    def __init__(self, name, types, lvl, hp, atk, def_, spd):
        self.name = name
        self.type = types
        self.lvl = lvl
        self.stats = [hp, atk, def_, spd]
        self.battle_c = 0

    def levelup(self):
        self.lvl += 1
        for i in range(4):
            self.stats[i] = round(self.stats[i] * 51/50)

    def attack(self, opp, move):
        if (move.type == "fire" and opp.type == "grass") or
        (move.type == "grass" and opp.type == "water") or
        (move.type == "water" and opp.type == "fire"):
            modif = 1.5
        elif (move.type == "fire" and opp.type == "water") or
        (move.type == "water" and opp.type == "grass") or
        (move.type == "grass" and opp.type == "fire"):
            modif = 0.5
        else:
            modif = 1

        dmg = ((self.lvl/2+2)*move.pwr*self.stats[1]/opp.stats[2]/50+2) * modif

    def update(self):
        if self.battle_c % 10 == 0:
            self.levelup()
        

class Charmander(Pokemon):
    def __init__(self):
        super.__init__("Charmander", "fire", 1, 39, 52, 43, 65)


class Squirtle(Pokemon):
    def __init__(self):
        super.__init__("Squirtle", "water", 1, 44, 48, 65, 43)


class Bulbasaur(Pokemon):
    def __init__(self):
        super.__init__("Bulbasaur", "grass", 1, 45, 49, 49, 45)


class IceCream(Pokemon):
    def __init__(self):
        super.__init__("Literally an ice cream", "water", 1, 36, 50, 50, 44)


class Garbage(Pokemon):
    def __init__(self):
        super.__init__("Literal Garbage", "grass", 1, 50, 50, 62, 67)


class torkoal(Pokemone):
    def __init__(self):
        super.__init__("China's air", "fire", 1, 70, 85, 140, 20)


class Klefki(Pokemon):
    def __init__(self):
        super.__init__("Your missing keys", "normal", 1, 57, 80, 91, 75)


class Magikarp(Pokemon):
    def __init__(self):
        super.__init__("Dead fish", "water", 1, 100, 100, 100, 100)


def main():
    pass


if __name__ == "__main__":
    main()
