import pokemon


class Item:
    def __init__(self, name: str, effect: str, amount: int):
        self.name = name
        self.effect = effect
        self.amount = amount

    def use(pokemon):
        if self.name = "Potion":
            pokemon.cur_hp += 20
        if self.name = "Steroids":
            pokemon.atk += 20
        if self.name = "Leg Day":
            pokemon.spd += 20

    @classmethod
    def potion(cls):
        return cls("Potion", "Heal hp by 20", 1)

    @classmethod
    def steroids(cls):
        return cls("Steroids", "Increase attack by 20", 1)

    @classmethod
    def leg_day(cls):
        return cls("Leg Day", "Increase speed by 20", 1)


if __name__ == "__main__":
    pass
