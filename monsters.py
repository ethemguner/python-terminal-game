import random
from places import Place
from money import PCash

class Monster(object):
    MONSTER_NAME = None
    MONSTER_DAMAGE = 1.44
    MONSTER_HEALTH = 1.7
    MONSTER_DEFENCE = 1.6
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
        from colorama import Fore, Style, init
        # If you're on Linux, init is unnecessary.
        init()
        location = Place(location_id=location_id).location
        for monster in MONSTERS:
            if monster.LOCATION == location:
                print(f"{Fore.RED}{monster.MONSTER_NAME}{Style.RESET_ALL} is living "
                      f"in {Fore.YELLOW}{location}.{Style.RESET_ALL} "
                      f"Monster ID: {Fore.GREEN}[{monster.MONSTER_ID}]{Style.RESET_ALL}")


class Worm(Monster):
    def __init__(self):
        self.MONSTER_NAME = "Worm"
        self.MONSTER_DAMAGE += 1.44
        self.MONSTER_HEALTH += 10
        self.MONSTER_DEFENCE += 0.88
        self.EXTRA_DAMAGE_CHANCE = 5
        self.BLOCK_CHANCE = 3
        self.EXPERIENCE = 0.44
        self.MONSTER_LEVEL = 1
        self.LOCATION = Place(location_id=1).location
        self.MONSTER_ID = 1
        self.PCash = PCash(2)


class Guba(Monster):
    def __init__(self):
        self.MONSTER_NAME = "Guba"
        self.MONSTER_DAMAGE += 3.74
        self.MONSTER_HEALTH += 18.75
        self.MONSTER_DEFENCE += 1.85
        self.EXTRA_DAMAGE_CHANCE = 10
        self.BLOCK_CHANCE = 8
        self.EXPERIENCE = 1.89
        self.MONSTER_LEVEL = 2
        self.LOCATION = Place(location_id=1).location
        self.MONSTER_ID = 2
        self.PCash = PCash(7)


class Toly(Monster):
    def __init__(self):
        self.MONSTER_NAME = "Toly"
        self.MONSTER_DAMAGE += 4.86
        self.MONSTER_HEALTH += 23.87
        self.MONSTER_DEFENCE += 2.67
        self.EXTRA_DAMAGE_CHANCE = 13
        self.BLOCK_CHANCE = 10
        self.EXPERIENCE = 2.74
        self.MONSTER_LEVEL = 3
        self.LOCATION = Place(location_id=2).location # change location
        self.MONSTER_ID = 3
        self.PCash = PCash(14)


class Mox(Monster):
    def __init__(self):
        self.MONSTER_NAME = "Mox"
        self.MONSTER_DAMAGE += 1.79
        self.MONSTER_HEALTH += 30.47
        self.MONSTER_DEFENCE += 4
        self.EXTRA_DAMAGE_CHANCE = 4
        self.BLOCK_CHANCE = 7
        self.EXPERIENCE = 3.5
        self.MONSTER_LEVEL = 4
        self.LOCATION = Place(location_id=2).location # change location
        self.MONSTER_ID = 4
        self.PCash = PCash(28)


class Phyle(Monster):
    def __init__(self):
        self.MONSTER_NAME = "Phyle"
        self.MONSTER_DAMAGE += 5.33
        self.MONSTER_HEALTH += 25
        self.MONSTER_DEFENCE += 3.41
        self.EXTRA_DAMAGE_CHANCE = 14
        self.BLOCK_CHANCE = 14
        self.EXPERIENCE = 4.22
        self.MONSTER_LEVEL = 5
        self.LOCATION = Place(location_id=2).location # change location
        self.MONSTER_ID = 5
        self.PCash = PCash(42)


class Otxer(Monster):
    def __init__(self):
        self.MONSTER_NAME = "Otxer"
        self.MONSTER_DAMAGE += 7
        self.MONSTER_HEALTH += 35
        self.MONSTER_DEFENCE += 5
        self.EXTRA_DAMAGE_CHANCE = 20
        self.BLOCK_CHANCE = 20
        self.EXPERIENCE = 7.5
        self.MONSTER_LEVEL = 6
        self.LOCATION = Place(location_id=3).location # change location
        self.MONSTER_ID = 6
        self.PCash = PCash(85)


class Jav(Monster):
    def __init__(self):
        self.MONSTER_NAME = "Jav"
        self.MONSTER_DAMAGE += 7.88
        self.MONSTER_HEALTH += 38.97
        self.MONSTER_DEFENCE += 5
        self.EXTRA_DAMAGE_CHANCE = 15
        self.BLOCK_CHANCE = 15
        self.EXPERIENCE = 8.24
        self.MONSTER_LEVEL = 7
        self.LOCATION = Place(location_id=3).location # change location
        self.MONSTER_ID = 7
        self.PCash = PCash(135)


class Rayl(Monster):
    def __init__(self):
        self.MONSTER_NAME = "Rayl"
        self.MONSTER_DAMAGE += 8.78
        self.MONSTER_HEALTH += 42
        self.MONSTER_DEFENCE += 5.80
        self.EXTRA_DAMAGE_CHANCE = 20
        self.BLOCK_CHANCE = 20
        self.EXPERIENCE = 10
        self.MONSTER_LEVEL = 8
        self.LOCATION = Place(location_id=3).location # change location
        self.MONSTER_ID = 8
        self.PCash = PCash(189)


class Haxy(Monster):
    def __init__(self):
        self.MONSTER_NAME = "Haxy"
        self.MONSTER_DAMAGE += 9.75
        self.MONSTER_HEALTH += 45
        self.MONSTER_DEFENCE += 6.33
        self.EXTRA_DAMAGE_CHANCE = 25
        self.BLOCK_CHANCE = 25
        self.EXPERIENCE = 13
        self.MONSTER_LEVEL = 9
        self.LOCATION = Place(location_id=4).location # change location
        self.MONSTER_ID = 9
        self.PCash = PCash(300)


class Felankor(Monster):
    def __init__(self):
        self.MONSTER_NAME = "Felankor"
        self.MONSTER_DAMAGE += 13.74
        self.MONSTER_HEALTH += 55
        self.MONSTER_DEFENCE += 8
        self.EXTRA_DAMAGE_CHANCE = 50
        self.BLOCK_CHANCE = 50
        self.EXPERIENCE = 21
        self.MONSTER_LEVEL = 10
        self.LOCATION = Place(location_id=5).location  # change location
        self.MONSTER_ID = 10
        self.PCash = PCash(500)


MONSTERS = [
    Worm(),
    Guba(),
    Toly(),
    Mox(),
    Phyle(),
    Otxer(),
    Jav(),
    Rayl(),
    Haxy(),
    Felankor()
]

