

class Town(object):
    LEVEL_RANGE = [0, 10]
    NAME = "Town"


class Place(object):
    PLACES = {
        1: Town(),
    }

    def __init__(self, location_id):
        self.location = self.PLACES[location_id].NAME

    def get_places(self):
        for location_id, location in self.PLACES.items():
            print(f"Location: {location.NAME}, Location ID: {location_id}")

