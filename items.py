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
        self.DAMAGE = 8.54
        self.DEFENCE = 0.33
        self.EXTRA_DAMAGE = 1.56
        self.NAME = "Sword of Mountains"
        self.REQUIRED_LEVEL = 1
        self.TYPE = "WEAPON"
        self.ID = 1
        self.EQUIPPED = False


class ArmorOfMountains(Item):
    def __init__(self):
        self.DAMAGE = 0
        self.DEFENCE = 4.22
        self.EXTRA_DAMAGE = 0.33
        self.NAME = "Armor of Mountains"
        self.REQUIRED_LEVEL = 1
        self.TYPE = "ARMOR"
        self.ID = 2
        self.EQUIPPED = False


class DaggerOfMountains(Item):
    def __init__(self):
        self.DAMAGE = 10
        self.DEFENCE = 0.24
        self.EXTRA_DAMAGE = 1.12
        self.NAME = "Dagger of Mountains"
        self.REQUIRED_LEVEL = 1
        self.TYPE = "WEAPON"
        self.ID = 3
        self.EQUIPPED = False

