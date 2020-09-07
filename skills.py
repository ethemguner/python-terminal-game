class Skill(object):
    SKILL_TYPES = {
        1: 'RANGE',
        2: 'MELEE',
        3: 'MAGIC',
    }
    EFFECTS = {
        1: 'FROSTY',
        2: 'BURNING',
        3: 'ELECTRIC'
    }

    MIN_LEVEL = 0
    MAX_LEVEL = 10
    EFFECT_PER_LEVEL = 0.68

    POINT = 0
    POINT_PER_LEVEL = 2

    def __init__(self, name, skill_type,
                 damage, effect, effect_chance,
                 skill_level):
        self.name = name
        self.skill_type = self.SKILL_TYPES[skill_type]
        self.effect = self.EFFECTS[effect]
        self.damage = damage

    def attack(self):
        message = f"Attack with {self.name}"
        return message

