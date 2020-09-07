import random
from places import Place


class Monster(object):
    MONSTER_NAME = None
    MONSTER_DAMAGE = None
    MONSTER_HEALTH = None
    MONSTER_DEFENCE = None
    EXTRA_DAMAGE_CHANCE = None
    BLOCK_CHANCE = None
    MONSTER_LEVEL = None
    LOCATION = None

    def attack(self):
        chance = random.randint(0, 100)
        if chance <= self.EXTRA_DAMAGE_CHANCE:
            extra_damage = random.random()
        else:
            extra_damage = 0
        total_damage = self.MONSTER_DAMAGE + extra_damage
        return total_damage

    def defence(self, taken_damage):
        defenced_damage = (taken_damage / 100) * self.MONSTER_DEFENCE
        return defenced_damage

    def block_next_attack(self):
        block = False
        chance = random.randint(0, 100)
        if chance <= self.BLOCK_CHANCE:
            block = True
        return block

    def summon_monsters(self, location_id):
        location = Place(location_id=location_id).location
        for monster in MONSTERS:
            if monster.LOCATION == location:
                print(f"{monster.MONSTER_NAME} is living in {location}. Monster ID: [{monster.MONSTER_ID}]")


class Worm(Monster):
    def __init__(self):
        self.MONSTER_NAME = "Worm"
        self.MONSTER_DAMAGE = 1.44
        self.MONSTER_HEALTH = 10
        self.MONSTER_DEFENCE = 0.88
        self.EXTRA_DAMAGE_CHANCE = 5
        self.BLOCK_CHANCE = 3
        self.EXPERIENCE = 0.44
        self.MONSTER_LEVEL = 1
        self.LOCATION = Place(location_id=1).location
        self.MONSTER_ID = 1


class Guba(Monster):
    def __init__(self):
        self.MONSTER_NAME = "Guba"
        self.MONSTER_DAMAGE = 3.74
        self.MONSTER_HEALTH = 18.75
        self.MONSTER_DEFENCE = 1.85
        self.EXTRA_DAMAGE_CHANCE = 10
        self.BLOCK_CHANCE = 8
        self.EXPERIENCE = 1.89
        self.MONSTER_LEVEL = 2
        self.LOCATION = Place(location_id=1).location
        self.MONSTER_ID = 2


MONSTERS = [
    Worm(),
    Guba()
]