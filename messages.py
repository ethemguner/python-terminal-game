# The print garbage. It was really painful to read the code.
# Also the coloring shit is making all prints worse.
# So, yeah...
from colorama import Fore, Style, init

# If you're on Linux, init is unnecessary.
init()


class Message:
    def __init__(self, character, monster=None, item=None):
        self.character = character
        self.monster = monster
        self.item = item

    def menu_and_character_summary(self):
        living = self.character.HEALTH if self.character.HEALTH > 0 else "You're so fucking dead."
        print(f"\n{Fore.GREEN}{self.character}{Style.RESET_ALL}, "
              f"your are in {Fore.YELLOW}{self.character.CURRENT_LOCATION}{Style.RESET_ALL} now.")
        print(f"{Fore.BLUE}LEVEL: {self.character.CURRENT_LEVEL}"
              f" | EXPERIENCE: {self.character.EXPERIENCE}{Style.RESET_ALL}")
        print(
            f"{Fore.BLUE}HP: {living} | STRENGTH: {self.character.STRENGTH}"
            f" | DEFENCE: {self.character.DEFENCE}{Style.RESET_ALL}")
        print("\n")
        print(f"{Fore.GREEN}1 ->{Style.RESET_ALL} Open the map. Currently,"
              f" you are in {self.character.CURRENT_LOCATION}.")
        print(f"{Fore.GREEN}2 ->{Style.RESET_ALL} Open the inventory.")
        print(f"{Fore.GREEN}3 ->{Style.RESET_ALL} Open the skill menu.")
        print("\n")

    def round_title(self, round_):
        print(f"{Fore.BLUE}------------------------ROUND {round_}------------------------{Style.RESET_ALL}")

    def character_attacking_message(self):
        print(f"{Fore.GREEN}###### {self.character.NAME} IS ATTACKING ######{Style.RESET_ALL}")

    def fight_begin_message(self):
        print(f"\n{self.character.NAME} vs. {self.monster.MONSTER_NAME} has begun!\n")

    def monsters_block_message(self):
        print(f"{Fore.RED}{self.character.NAME}'s attack "
              f"has been blocked by {self.monster.MONSTER_NAME}{Style.RESET_ALL}!")

    def character_damage_message(self, character_total_damage):
        print(f"Dealt {character_total_damage} damage to {self.monster.MONSTER_NAME}")

    def current_monster_hp(self, monster_hp):
        print(f"{self.monster.MONSTER_NAME} HP: ", monster_hp)

    def monster_attacking_message(self):
        print(f"{Fore.RED}#### {self.monster.MONSTER_NAME} IS ATTACKING ####{Style.RESET_ALL}")

    def characters_block_message(self):
        print(f"{Fore.GREEN}{self.monster.MONSTER_NAME} couldn't make any damage to "
              f"{self.character.NAME}...{Style.RESET_ALL}")

    def monster_damage_message(self, monster_total_damage):
        print(f"{self.monster.MONSTER_NAME} hit {monster_total_damage} damage to {self.character.NAME}!")

    def current_character_hp(self, character_hp):
        print(f"{self.character.NAME} HP: ", character_hp)

    def traveling_warning(self, min_level):
        print(f"\n{Fore.RED}You cannot travel to this place. "
              f"It requires minimum {min_level} level.\n{Style.RESET_ALL}")

    def traveling_message(self):
        print(f"\n{Fore.GREEN}You traveled to {self.character.CURRENT_LOCATION}.{Style.RESET_ALL}\n")

    def items_in_inventory(self, i, item_name, equipped):
        print(f"{i} -> {item_name} |",
              f"{Fore.GREEN}Equipped.{Style.RESET_ALL}" if equipped else f"{Fore.RED}Not Equipped.{Style.RESET_ALL}")

    def character_win_message(self, round_):
        print(f"\n{Fore.GREEN}{self.character.NAME} has won in {round_} round!!{Style.RESET_ALL}")
        print("\n")

    def character_lost_message(self, round_):
        print(f"\n{Fore.RED}{self.character.NAME} has lost against "
              f"{self.monster.MONSTER_NAME} in {round_} round...{Style.RESET_ALL}")
        print("\n")

    def level_up(self, next_level_experience):
        print(f"{self.character.NAME}, YOU LEVELED UP TO {self.character.CURRENT_LEVEL}! "
              f"Next level ({self.character.CURRENT_LEVEL + 1}) requires {next_level_experience} experience. "
              f"You have {self.character.EXPERIENCE} experience.")

    def strength_increased(self, strength_diff):
        print(f"{Fore.GREEN}Your strength increased +{strength_diff}! {Style.RESET_ALL}"
              f"Your current strength is {self.character.STRENGTH}.")

    def defence_increased(self, defence_diff):
        print(f"{Fore.GREEN}Your defence increased +{defence_diff}! {Style.RESET_ALL}"
              f"Your current defence is {self.character.DEFENCE}.")

    def cannot_equip_item(self, item_name, item_level):
        print(f"{Fore.RED}You cannot equip {item_name}. It requires {item_level} level.{Style.RESET_ALL}")

    def item_added(self, item_name):
        print(f"{Fore.GREEN}{item_name} added to your inventory.{Style.RESET_ALL}")

    def unequipped_item(self, item_name):
        print(f"{Fore.YELLOW}{item_name} unequipped!{Style.RESET_ALL}")

    def strength_decreased(self, strength_diff):
        print(f"{Fore.RED}Your strength decreased {strength_diff}. {Style.RESET_ALL}"
              f"Now, your strength is {self.character.STRENGTH}")

    def defence_decreased(self, defence_diff):
        print(f"{Fore.RED}Your defence decreased {defence_diff}. {Style.RESET_ALL}"
              f"Now, your defence is {self.character.DEFENCE}")

    def equipped_item(self, item_name):
        print(f"\n{Fore.GREEN}You equipped {item_name}.{Style.RESET_ALL}")

    def gained_experience(self, experience):
        print(f"You gained {Fore.GREEN}{experience}{Style.RESET_ALL} experience.")

    def gained_pcash(self, pcash_amount):
        print(f"You gained {Fore.CYAN}{pcash_amount}{Style.RESET_ALL} PCash.")

