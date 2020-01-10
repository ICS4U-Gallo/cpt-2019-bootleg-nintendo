import pokemon


class Item:
    def __init__(self, name: str, effect: str, amount: int):
        self.name = name
        self.effect = effect
        self.amount = amount

    def use(pokemon):
        if self.name = "Essential oils":
            pokemon.cur_hp += 20
        if self.name = "Steroids":
            pokemon.atk += 20
        if self.name = "Leg Day":
            pokemon.spd += 20

    @classmethod
    def potion(cls):
        item = cls("Essential oils", "Heal hp by 20", 1)
        item.texture = arcade.load_texture("images/cocaine.jpg")
        return item

    @classmethod
    def steroids(cls):
        item = cls("Steroids", "Increase attack by 20", 1)
        item.texture = arcade.load_texture("images/steroid.jpg")
        return item

    @classmethod
    def leg_day(cls):
        item = cls("Leg Day", "Increase speed by 20", 1)
        item.texture = arcade.load_texture("images/legs.jpg")
        return item


if __name__ == "__main__":
    pass
