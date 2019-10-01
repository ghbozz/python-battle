# Fighter
import random


class Fighter:

    def __init__(self, attack, defense, hp):
        self.attack = attack
        self.defense = defense
        self.hp = hp

    def strike(self):
        return self.attack * random.randrange(1, 3)

    def get_damage(self, damage):
        computed_damage = damage - ((self.defense / 100) * 10)
        self.hp -= computed_damage
        return computed_damage
