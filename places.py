

class Town(object):
    MINIMUM_LEVEL = 0
    NAME = "Town"


class Ankara(object):
    MINIMUM_LEVEL = 3
    NAME = "Ankara"


class Gultepe(object):
    MINIMUM_LEVEL = 6
    NAME = "Gultepe"


class Mamak(object):
    MINIMUM_LEVEL = 9
    NAME = "Mamak"


class Istanbul(object):
    MINIMUM_LEVEL = 10
    NAME = "Istanbul"


class Place(object):
    PLACES = {
        None: Town(),
        0: Town(),
        1: Town(),
        2: Ankara(),
        3: Gultepe(),
        4: Mamak(),
        5: Istanbul(),
    }

    def __init__(self, location_id=None):
        try:
            self.location = self.PLACES[location_id].NAME
        except KeyError:
            self.location = Town().NAME

    def get_places(self):
        from colorama import Fore, Style, init
        # If you're on Linux, init is unnecessary.
        init()
        for location_id, location in self.PLACES.items():
            if location_id is None or location_id == 0:
                continue
            print(f"Location: {Fore.YELLOW}{location.NAME}{Style.RESET_ALL}, "
                  f"{Fore.GREEN}[Location ID: {location_id}]{Style.RESET_ALL} - "
                  f"Available for level {Fore.RED}{location.MINIMUM_LEVEL}{Style.RESET_ALL} and above.")

