from character import Character
from places import Place
from monsters import Worm, Monster, MONSTERS
from items import SwordOfMountains, ArmorOfMountains, DaggerOfMountains
import time
from colorama import Fore, Style, init

# If you're on Linux, init is unnecessary.
init()

def fight(character, monster):
    print(f"\n{character.NAME} vs. {monster.MONSTER_NAME} has begun!\n")
    time.sleep(1)
    character_hp = character.HEALTH
    monster_hp = monster.MONSTER_HEALTH
    round_ = 1
    while character_hp > 0 and monster_hp > 0:
        print(f"{Fore.BLUE}------------------------ROUND {round_}------------------------{Style.RESET_ALL}")
        print(f"{Fore.GREEN}###### {character.NAME} IS ATTACKING ######{Style.RESET_ALL}")
        character_total_damage = character.attack() - monster.defence(character.attack())
        monster_hp -= 0 if monster.block_next_attack() else character_total_damage
        if monster.block_next_attack():
            print(f"{Fore.RED}{character.NAME}'s attack "
                  f"has been blocked by {monster.MONSTER_NAME}{Style.RESET_ALL}!")
        else:
            print(f"Dealt {character_total_damage} damage to {monster.MONSTER_NAME}")

        print(f"{monster.MONSTER_NAME} HP: ", monster_hp)

        if monster_hp < 0:
            total_taken_damage = character.HEALTH - character_hp
            character.HEALTH -= total_taken_damage
            return True, round_

        print(f"\n{Fore.YELLOW}Attack will come from monster now...{Style.RESET_ALL}\n")
        time.sleep(2)
        print(f"{Fore.RED}#### {monster.MONSTER_NAME} IS ATTACKING ####{Style.RESET_ALL}")
        monster_total_damage = monster.attack() - character.defence(monster.attack())
        if monster_total_damage < 0:
            print(f"{Fore.GREEN}{monster.MONSTER_NAME} couldn't make any damage to "
                  f"{character.NAME}...{Style.RESET_ALL}")
        else:
            character_hp -= monster_total_damage
            print(f"{monster.MONSTER_NAME} hit {monster_total_damage} damage to {character.NAME}!")

        print(f"{character.NAME} HP: ", character_hp)

        if character_hp < 0:
            character.HEALTH = 0
            return False, round_

        round_ += 1
        print(f"{Fore.YELLOW}\nRound ended, next round will start...{Style.RESET_ALL}")
        time.sleep(3)
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
character.CURRENT_LEVEL = 10
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
    living = character.HEALTH if character.HEALTH > 0 else "You're so fucking dead."
    print(f"\n{Fore.GREEN}{character}{Style.RESET_ALL}, "
          f"your are in {Fore.YELLOW}{character.CURRENT_LOCATION}{Style.RESET_ALL} now.")
    print(f"{Fore.BLUE}LEVEL: {character.CURRENT_LEVEL} | EXPERIENCE: {character.EXPERIENCE}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}HP: {living} | STRENGTH: {character.STRENGTH} | DEFENCE: {character.DEFENCE}{Style.RESET_ALL}")
    print("\n")
    print(f"{Fore.GREEN}1 ->{Style.RESET_ALL} Open the map. Currently, you are in {character.CURRENT_LOCATION}.")
    print(f"{Fore.GREEN}2 ->{Style.RESET_ALL} Open the inventory.")
    print(f"{Fore.GREEN}3 ->{Style.RESET_ALL} Open the skill menu.")
    print("\n")
    action = int(input("Please choose an action: "))

    if action == 1:
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
                        print(f"\n{Fore.GREEN}{character.NAME} has won in {round_} round!!{Style.RESET_ALL}")
                        print("\n")
                        character.gain_experience(chosen_monster.EXPERIENCE)
                    else:
                        print(f"\n{Fore.RED}{character.NAME} has lost against "
                              f"{chosen_monster.MONSTER_NAME} in {round_} round...{Style.RESET_ALL}")
                        print("\n")

    elif action == 2:
        inventory(character)

