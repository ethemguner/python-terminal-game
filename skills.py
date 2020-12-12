class Skill:
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

    ADDITIONAL_DAMAGE_PER_LEVEL = 1.78

    POINT = 0
    POINT_PER_LEVEL = 2

    def __init__(self, name=None, skill_type=None,
                 damage=None, effect=None, effect_chance=None,
                 skill_level=None, *args, **kwargs):
        self.name = name
        self.skill_type = self.SKILL_TYPES.get(skill_type)
        self.effect_chance = effect_chance
        self.skill_level = skill_level
        self.effect = self.EFFECTS.get(effect)
        self.damage = damage

    def attack(self):
        print(f"{self.name} is in use.")
        pass


class BasicAttack(Skill):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.character_level = kwargs.pop('character_level')
        self.name = "Basic Attack"
        self.skill_type = 2
        self.damage = 3.4 + self.character_level * self.ADDITIONAL_DAMAGE_PER_LEVEL
        self.skill_level = 1


class HeavyAttack(Skill):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.character_level = kwargs.pop('character_level')
        self.name = "Heavy Attack"
        self.skill_type = 2
        self.damage = 7.8 + self.character_level * self.ADDITIONAL_DAMAGE_PER_LEVEL
        self.skill_level = 1
