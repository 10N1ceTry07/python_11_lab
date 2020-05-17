import doctest

from src.main.classes.things_type import ThingsType
from src.main.classes.trekking import Trekking
from src.main.classes.boating import Boating
from src.main.classes.camping import Camping


class CampingManager:
    def __init__(self, list_of_things=[]):
        self.list_of_things = list_of_things

    def find_things_for_hiking(self, things_type: ThingsType):
        """
        >>> thing_one = Boating("boat", "Dynamo", ThingsType.BOATING, 200, 7000, True)
        >>> thing_two = Trekking("backpack", "CityStyle", ThingsType.HIKING, 2.5, 550, True)
        >>> thing_three = Camping("tent", "Caravan", ThingsType.CAMPING, 5.4, 1500, True)
        >>> print(str(CampingManager([thing_one, thing_two, thing_three]).find_things_for_hiking(ThingsType.HIKING))) #doctest: +ELLIPSIS
        [ThingsForTrekking(...things_type=ThingsType.HIKING...)]


        """
        return list(filter(lambda things: things.things_type == things_type, self.list_of_things))


if __name__ == '__main__':
    doctest.testmod(verbose=True)
