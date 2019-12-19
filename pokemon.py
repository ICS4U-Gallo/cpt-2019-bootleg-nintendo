import poke_move

types = ["fire", "water", "not wood"]


class Pokemon:
    def __init__(self, name, types, lvl, hp, atk, def_, spd):
        self.name = name
        self.type = types
        self.lvl = lvl
        self.hp = hp
        self.stats = [atk, def_, spd]

    def levelup(self):
        self.lvl += 1
        self.hp += 1
        for stat in self.stats:
            stat += 2


def main():
    pass


if __name__ == "__main__":
    main()
