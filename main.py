from character import Character
from places import Place
from monsters import Worm, Monster, MONSTERS
from items import SwordOfMountains, ArmorOfMountains, DaggerOfMountains
import time
from colorama import Fore, Style, init
from messages import Message

# If you're on Linux, init is unnecessary.
init()


def fight(character, monster):
    message = Message(character, monster)
    message.fight_begin_message()
    time.sleep(1)
    character_hp = character.HEALTH
    monster_hp = monster.MONSTER_HEALTH
    round_ = 1
    while character_hp > 0 and monster_hp > 0:
        message.round_title(round_)
        message.character_attacking_message()
        character_total_damage = character.attack() - monster.defence(character.attack())
        monster_hp -= 0 if monster.block_next_attack() else character_total_damage
        if monster.block_next_attack():
            message.monsters_block_message()
        else:
            message.character_damage_message(character_total_damage)

        message.current_monster_hp(monster_hp)

        if monster_hp < 0:
            total_taken_damage = character.HEALTH - character_hp
            character.HEALTH -= total_taken_damage
            return True, round_

        print(f"\n{Fore.YELLOW}Attack will come from monster now...{Style.RESET_ALL}\n")

        time.sleep(2)
        message.monster_attacking_message()
        monster_total_damage = monster.attack() - character.defence(monster.attack())
        if monster_total_damage < 0:
            message.characters_block_message()
        else:
            character_hp -= monster_total_damage
            message.monster_damage_message(monster_total_damage)

        message.current_character_hp(character_hp)

        if character_hp < 0:
            character.HEALTH = 0
            return False, round_

        round_ += 1
        print(f"{Fore.YELLOW}\nRound ended, next round will start...{Style.RESET_ALL}")
        time.sleep(3)
        print("\n")
    return won, round_


def inventory(character):
    message = Message(character=character)
    item_detail = True
    print("\n")
    while item_detail:
        for i, item in enumerate(character.INVENTORY):
            equipped = item.EQUIPPED
            message.items_in_inventory(i, item.NAME, equipped)

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
# character.CURRENT_LEVEL = 10
print("\n")

# these should not be here, but I added them to tests. When I
# write the looting system, they'll be removed.
# sword = SwordOfMountains()
# armor = ArmorOfMountains()
# dagger = DaggerOfMountains()
# character.equipped_item(sword)
# character.equipped_item(armor)
# character.equipped_item(dagger)

while True:
    message = Message(character)
    message.menu_and_character_summary()
    action = int(input("Please choose an action: "))

    if action == 1:
        # To fight, you have to travel ( ^_^ )
        # Where will you travel? To bad lands ( ~_~ )
        # What will you see? Monsters |_ O_O _|
        travel = True
        while travel:
            place = Place()
            place.get_places()
            place_id = input("Write the place id you want to travel "
                             "(to stop traveling, write q): ")
            if place_id == "q":
                break

            try:
                selected_place = Place.PLACES[int(place_id)]
            except KeyError:
                selected_place = Place.PLACES[1]
                location_changed = False

            location_changed = character.chance_location(selected_place)
            if location_changed:
                keep_fight = True
                while keep_fight:
                    monster = Monster()
                    monster.summon_monsters(location_id=int(place_id))
                    try:
                        monster_id = int(input("Write the monster id you want to "
                                               "fight against to (to exit, write 0): "))
                    except ValueError:
                        break
                    if monster_id == 0:
                        break
                    chosen_monster = None
                    for m in MONSTERS:
                        if monster_id == m.MONSTER_ID:
                            chosen_monster = m
                    won, round_ = fight(character=character, monster=chosen_monster)
                    if won:
                        message.character_win_message(round_)
                        character.gain_experience_and_pcash(chosen_monster.EXPERIENCE,
                                                            chosen_monster.PCash.amount)
                    else:
                        message.character_lost_message(round_)

    elif action == 2:
        inventory(character)

