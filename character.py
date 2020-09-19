import random
from messages import Message


class Character(object):
    NAME = None
    CURRENT_LEVEL = 1
    CURRENT_LOCATION = None
    WEAPON = None
    ARMOR = None
    STRENGTH = 12
    HEALTH = 35
    DEFENCE = 2.4
    EXPERIENCE = 0
    INVENTORY = []
    WEAPON_EQUIPPED = False
    ARMOR_EQUIPPED = False
    TOTAL_PCASH = 0
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
        self.message = Message(character=self)

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

        return self.message.level_up(next_level_experience)

    def gain_experience_and_pcash(self, experience, pcash_amount):
        if self.CURRENT_LEVEL == 10:
            return

        self.EXPERIENCE += experience
        self.message.gained_experience(experience)

        self.TOTAL_PCASH += pcash_amount
        self.message.gained_pcash(pcash_amount)

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
            self.message.traveling_message()
            return True
        else:
            self.message.traveling_warning(location.MINIMUM_LEVEL)
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
            self.message.equipped_item(self.WEAPON.NAME)
        elif item.TYPE == "ARMOR":
            self.ARMOR = item
            self.ARMOR.EQUIPPED = True
            self.message.equipped_item(self.ARMOR.NAME)

        self.add_item_to_inventory(item)

        old_strength = self.STRENGTH
        old_defence = self.DEFENCE
        self.STRENGTH += item.DAMAGE
        self.DEFENCE += item.DEFENCE
        strength_diff = self.STRENGTH - old_strength
        defence_diff = self.DEFENCE - old_defence

        if self.STRENGTH > old_strength:
            self.message.strength_increased(strength_diff)

        if self.DEFENCE > old_defence:
            self.message.defence_increased(defence_diff)

    def equipped_item(self, item):
        if self.CURRENT_LEVEL < item.REQUIRED_LEVEL:
            self.message.cannot_equip_item(item.NAME, item.REQUIRED_LEVEL)
        else:
            self.set_item(item)

    def add_item_to_inventory(self, item):
        if item not in self.INVENTORY:
            self.INVENTORY.append(item)
            self.message.item_added(item.NAME)

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

        self.message.unequipped_item(item.NAME)
        if item_type == "WEAPON":
            self.WEAPON = None
        elif item_type == "ARMOR":
            self.ARMOR = None

        if old_strength > self.STRENGTH:
            strength_diff = old_strength - self.STRENGTH
            self.message.strength_decreased(strength_diff)

        if old_defence > self.DEFENCE:
            defence_diff = old_defence - self.DEFENCE
            self.message.defence_decreased(defence_diff)

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
