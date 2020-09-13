import random


class Character(object):
    NAME = None
    CURRENT_LEVEL = 1
    CURRENT_LOCATION = None
    WEAPON = None
    ARMOR = None
    STRENGTH = 3
    HEALTH = 35
    DEFENCE = 2
    EXPERIENCE = 0
    INVENTORY = []
    WEAPON_EQUIPPED = False
    ARMOR_EQUIPPED = False
    LEVELS_AND_EXPERIENCES = {
        1: 10,
        2: 16,
        3: 25,
        4: 36,
        5: 56,
        6: 98,
        7: 133,
        8: 188,
        9: 266,
        10: 365,
    }

    def __init__(self, name, location=None,
                 weapon=None, armor=None):
        self.NAME = name
        self.CURRENT_LOCATION = location
        self.WEAPON = weapon
        self.ARMOR = armor

    def __str__(self):
        return self.NAME

    def level_up(self):
        for level, experience in self.LEVELS_AND_EXPERIENCES.items():
            if self.EXPERIENCE >= experience and level > self.CURRENT_LEVEL:
                self.CURRENT_LEVEL += 1
                self.STRENGTH += 2.55

        try:
            next_level_experience = self.LEVELS_AND_EXPERIENCES[self.CURRENT_LEVEL + 1]
        except KeyError:
            return print("You have reached the maximum level!")

        return print(f"{self.NAME}, YOU LEVELED UP TO {self.CURRENT_LEVEL}! "
                     f"Next level ({self.CURRENT_LEVEL + 1}) requires {next_level_experience} experience. "
                     f"You have {self.EXPERIENCE} experience.")

    def gain_experience(self, experience):
        if self.CURRENT_LEVEL == 10:
            return

        self.EXPERIENCE += experience
        print(f"You gained {experience} experience.")

        if self.EXPERIENCE >= self.get_next_level_experience():
            self.level_up()

    def get_next_level_experience(self):
        next_level_experience = self.LEVELS_AND_EXPERIENCES[self.CURRENT_LEVEL + 1]
        return next_level_experience

    def get_items_extra_damage(self):
        weapon_extra_damage = self.WEAPON.EXTRA_DAMAGE if self.WEAPON else 0
        armor_extra_damage = self.ARMOR.EXTRA_DAMAGE if self.ARMOR else 0
        return weapon_extra_damage + armor_extra_damage

    def get_skill_damage(self, skill):
        return 0

    def chance_location(self, location):
        if self.CURRENT_LEVEL >= location.MINIMUM_LEVEL:
            self.CURRENT_LOCATION = location.NAME
            print(f"\nYou traveled to {self.CURRENT_LOCATION}.\n")
            return True
        else:
            print(f"\n########## You cannot travel to this place. "
                  f"It requires minimum {location.MINIMUM_LEVEL} level. ##########\n")
            return False

    def attack(self, skill=None):
        items_extra_damage = self.get_items_extra_damage()
        skill_total_damage = self.get_skill_damage(skill)
        extra_damage = (self.STRENGTH / 100) * random.randint(1, 5)
        total_damage = (self.STRENGTH + skill_total_damage +
                        extra_damage + items_extra_damage) * (self.CURRENT_LEVEL / 10)
        return total_damage

    def defence(self, taken_damage):
        defenced_damage = (taken_damage / 100) * self.DEFENCE
        return defenced_damage

    def set_item(self, item):
        if self.WEAPON and item.TYPE == "WEAPON" and item.ID == self.WEAPON.ID or \
                self.ARMOR and item.TYPE == "ARMOR" and item.ID == self.ARMOR.ID:
            print("Already equipped.")
            return
        elif self.WEAPON and item.TYPE == "WEAPON" and item.ID != self.WEAPON.ID or \
                self.ARMOR and item.TYPE == "ARMOR" and item.ID != self.ARMOR.ID:
            self.unequipped_item(item_type=item.TYPE)

        if item.TYPE == "WEAPON":
            self.WEAPON = item
            self.WEAPON.EQUIPPED = True
            print(f"You equipped {self.WEAPON.NAME}.")
        elif item.TYPE == "ARMOR":
            self.ARMOR = item
            self.ARMOR.EQUIPPED = True
            print(f"You equipped {self.ARMOR.NAME}.")

        self.add_item_to_inventory(item)

        old_strength = self.STRENGTH
        old_defence = self.DEFENCE
        self.STRENGTH += item.DAMAGE
        self.DEFENCE += item.DEFENCE
        strength_diff = self.STRENGTH - old_strength
        defence_diff = self.DEFENCE - old_defence

        if self.STRENGTH > old_strength:
            print(f"Your strength increased +{strength_diff}! "
                  f"Your current strength is {self.STRENGTH}.")

        if self.DEFENCE > old_defence:
            print(f"Your defence increased +{defence_diff}! "
                  f"Your current defence is {self.DEFENCE}.")

    def equipped_item(self, item):
        if self.CURRENT_LEVEL < item.REQUIRED_LEVEL:
            print(f"You cannot equip {item.NAME}. It requires {item.REQUIRED_LEVEL} level.")
        else:
            self.set_item(item)

    def add_item_to_inventory(self, item):
        if item not in self.INVENTORY:
            self.INVENTORY.append(item)
            print(f"{item.NAME} added to your inventory.")

    def unequipped_item(self, item_type):
        if item_type == "WEAPON" and self.WEAPON:
            item = self.WEAPON
        elif item_type == "ARMOR" and self.ARMOR:
            item = self.ARMOR
        else:
            item = None

        for item_in_inventory in self.INVENTORY:
            if item_in_inventory == item:
                item_in_inventory.EQUIPPED = False

        old_strength = self.STRENGTH
        old_defence = self.DEFENCE
        self.STRENGTH -= item.DAMAGE
        self.DEFENCE -= item.DEFENCE

        print(f"{item.NAME} unequipped!")
        if item_type == "WEAPON":
            self.WEAPON = None
        elif item_type == "ARMOR":
            self.ARMOR = None

        if old_strength > self.STRENGTH:
            strength_diff = old_strength - self.STRENGTH
            print(f"Your strength decreased {strength_diff}. "
                  f"Now your strength is {self.STRENGTH}")

        if old_defence > self.DEFENCE:
            defence_diff = old_defence - self.DEFENCE
            print(f"Your defence decreased {defence_diff}. "
                  f"Now your defence is {self.DEFENCE}")

# from places import Place
# from items import SwordOfMountains, ArmorOfMountains, DaggerOfMountains
# import time
#
# character = Character(name="Ethem", location=Place(location_id=1))
# sword = SwordOfMountains()
# armor = ArmorOfMountains()
#
# character.equipped_item(sword)
# print("-----------------------------------------------------")
# time.sleep(4)
# character.equipped_item(armor)
# time.sleep(4)
# print("-----------------------------------------------------")
# character.unequipped_item(item_type="ARMOR")
# character.equipped_item(armor)
# print("-----------------------------------------------------")
# time.sleep(5)
#
# character.unequipped_item(item_type="WEAPON")
# time.sleep(3)
# character.unequipped_item(item_type="ARMOR")

# dagger = DaggerOfMatatutu()
# character.equipped_item(dagger)
