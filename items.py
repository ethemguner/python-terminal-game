class Item(object):
    DAMAGE = None
    DEFENCE = None
    EXTRA_DAMAGE = None
    NAME = None
    REQUIRED_LEVEL = None
    TYPE = None
    ID = None
    EQUIPPED = False

    def get_item_info(self):
        print(f"DAMAGE: {self.DAMAGE}")
        print(f"DEFENCE: {self.DEFENCE}")
        print(f"EXTRA DAMAGE: {self.EXTRA_DAMAGE}")
        print(f"REQUIRED LEVEL: {self.REQUIRED_LEVEL}")
        print(f"EQUIPPED:", "Equipped" if self.EQUIPPED else "Not Equipped.")


class SwordOfMountains(Item):
    def __init__(self):
        self.DAMAGE = 2.78
        self.DEFENCE = 0.33
        self.EXTRA_DAMAGE = 0.78
        self.NAME = "Sword of Mountains"
        self.REQUIRED_LEVEL = 1
        self.TYPE = "WEAPON"
        self.ID = 1
        self.EQUIPPED = False


class ArmorOfMountains(Item):
    def __init__(self):
        self.DAMAGE = 0
        self.DEFENCE = 3.14
        self.EXTRA_DAMAGE = 0.12
        self.NAME = "Armor of Mountains"
        self.REQUIRED_LEVEL = 1
        self.TYPE = "ARMOR"
        self.ID = 2
        self.EQUIPPED = False


class DaggerOfMountains(Item):
    def __init__(self):
        self.DAMAGE = 4
        self.DEFENCE = 0
        self.EXTRA_DAMAGE = 0.89
        self.NAME = "Dagger of Mountains"
        self.REQUIRED_LEVEL = 1
        self.TYPE = "WEAPON"
        self.ID = 3
        self.EQUIPPED = False

