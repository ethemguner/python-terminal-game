from character import Character
from places import Place
from monsters import Worm, Monster, MONSTERS
from items import SwordOfMountains, ArmorOfMountains, DaggerOfMountains
import time


def fight(character, monster):
    print(f"{character.NAME} vs. {monster.MONSTER_NAME} has begun!")
    time.sleep(2)
    character_hp = character.HEALTH
    monster_hp = monster.MONSTER_HEALTH
    round_ = 1
    while character_hp > 0 and monster_hp > 0:
        print(f"---------------------------ROUND {round_}---------------------------")
        print(f"#### ATTACK FROM {character.NAME} ####")
        character_total_damage = character.attack() - monster.defence(character.attack())
        monster_hp -= 0 if monster.block_next_attack() else character_total_damage
        if monster.block_next_attack():
            print(f"{character.NAME}'s attack has been blocked by {monster.MONSTER_NAME}!")
        else:
            print(f"{character.NAME} dealt {character_total_damage} damage to {monster.MONSTER_NAME}!")

        print(f"{monster.MONSTER_NAME} HP: ", monster_hp)

        if monster_hp < 0:
            total_taken_damage = character.HEALTH - character_hp
            character.HEALTH -= total_taken_damage
            return True, round_

        print("Attack will come from monster now...")
        time.sleep(3)
        print(f"#### ATTACK FROM {monster.MONSTER_NAME} ####\n")
        monster_total_damage = monster.attack() - character.defence(monster.attack())
        if monster_total_damage < 0:
            print(f"{monster.MONSTER_NAME} couldn't make any damage to {character.NAME}...")
        else:
            character_hp -= monster_total_damage
            print(f"{monster.MONSTER_NAME} hit {monster_total_damage} damage to {character.NAME}!")

        print(f"{character.NAME} HP: ", character_hp)

        if character_hp < 0:
            character.HEALTH = 0
            return False, round_

        round_ += 1
        print("Round ended, next round will start...")
        time.sleep(4)
        print("\n")
    return won, round_


def inventory(character):
    item_detail = True
    print("\n")
    while item_detail:
        for i, item in enumerate(character.INVENTORY):
            equipped = item.EQUIPPED
            print(f"{i} -> {item.NAME} |", "Equipped." if equipped else "Not Equipped.")

        print("If you want to equip an item, write: equip <number of item>")
        item_detail = input("To see details, write number of that item (to go menu enter q): ")
        print("\n")
        for i, item in enumerate(character.INVENTORY):
            if item_detail == str(i):
                print(f"### {item.NAME} ###")
                item.get_item_info()
        print("\n")

        try:
            equip_command = item_detail.split(" ")[0]
            if equip_command == "equip":
                item_number = item_detail.split(" ")[1]
                for i, item in enumerate(character.INVENTORY):
                    if item_number == str(i):
                        character.equipped_item(item)
                        print("\n")
        except AttributeError:
            pass

        if item_detail == "q":
            item_detail = False


character_name = input("Choose a name to your mighty adventure: ")
place = Place(location_id=1)
character = Character(name=character_name, location=place.location)
print("\n")

# these should not be here, but I added them to tests. When I
# write the looting system, they'll be removed.
sword = SwordOfMountains()
armor = ArmorOfMountains()
dagger = DaggerOfMountains()
character.equipped_item(sword)
character.equipped_item(armor)
character.equipped_item(dagger)

while True:
    print(f"{character}, your are in {character.CURRENT_LOCATION} now.")
    print(f"LEVEL: {character.CURRENT_LEVEL} | EXPERIENCE: {character.EXPERIENCE}")
    print(f"HP: {character.HEALTH} | STRENGTH: {character.STRENGTH} | DEFENCE: {character.DEFENCE}")
    print("\n")
    print(f"1 -> Go to fight against monsters in {character.CURRENT_LOCATION}")
    print("2 -> Open the inventory.")
    print("3 -> Open the skill menu.")
    print("\n")
    action = int(input("Please choose an action: "))

    if action == 1:
        monster = Monster()
        monster.summon_monsters(location_id=1)
        monster_id = int(input("Write the monster id you want to fight against to: "))
        chosen_monster = None
        for m in MONSTERS:
            print(m.MONSTER_ID, monster_id)
            if monster_id == m.MONSTER_ID:
                chosen_monster = m
        won, round_ = fight(character=character, monster=chosen_monster)
        if won:
            print(f"{character.NAME} has won in {round_} round!!")
            print("\n")
            character.gain_experience(chosen_monster.EXPERIENCE)
        else:
            print(f"{character.NAME} has lost against {chosen_monster.MONSTER_NAME} in {round_} round...")
            print("\n")
    elif action == 2:
        inventory(character)