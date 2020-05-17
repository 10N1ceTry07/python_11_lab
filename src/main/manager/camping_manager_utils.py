import doctest

from src.main.classes.things_type import ThingsType
from src.main.classes.trekking import Trekking
from src.main.classes.boating import Boating
from src.main.classes.camping import Camping


class CampingManagerUtils:
    def __init__(self):
        pass

    @staticmethod
    def sort_by_price_descending(list_of_things):
        """
        >>> thing_one = Boating("boat", "Dynamo", ThingsType.BOATING, 200, 7000, True)
        >>> thing_two = Trekking("backpack", "CityStyle", ThingsType.HIKING, 2.5, 550, True)
        >>> thing_three = Camping("tent", "Caravan", ThingsType.CAMPING, 5.4, 1500, True)
        >>> print(str(CampingManagerUtils.sort_by_price_descending(([thing_one,thing_two, thing_three])))) #doctest: +ELLIPSIS
        [ThingsForBoating(...price_in_uah=7000...), ThingsForCamping(...price_in_uah=1500...), ThingsForTrekking(...price_in_uah=550...)]
        """
        return sorted(list_of_things, key=lambda things: things.price_in_uah, reverse=True)

    @staticmethod
    def sort_by_price_ascending(list_of_things):
        """
        >>> thing_one = Boating("boat", "Dynamo", ThingsType.BOATING, 200, 7000, True)
        >>> thing_two = Trekking("backpack", "CityStyle", ThingsType.HIKING, 2.5, 550, True)
        >>> thing_three = Camping("tent", "Caravan", ThingsType.CAMPING, 5.4, 1500, True)
        >>> print(str(CampingManagerUtils.sort_by_price_ascending(([thing_one,thing_two, thing_three])))) #doctest: +ELLIPSIS
        [ThingsForTrekking(...price_in_uah=550...), ThingsForCamping(...price_in_uah=1500...), ThingsForBoating(...price_in_uah=7000...)]
        """
        return sorted(list_of_things, key=lambda things: things.price_in_uah)

    @staticmethod
    def sort_by_weight_in_kilo(list_of_things):
        """
        >>> thing_one = Boating("boat", "Dynamo", ThingsType.BOATING, 200, 7000, True)
        >>> thing_two = Trekking("backpack", "CityStyle", ThingsType.HIKING, 2.5, 550, True)
        >>> thing_three = Camping("tent", "Caravan", ThingsType.CAMPING, 5.4, 1500, True)
        >>> list_things = [thing_one, thing_two, thing_three]
        >>> result = CampingManagerUtils.sort_by_weight_in_kilo(list_things)
        >>> for obj1 in result: print(obj1.weight_in_kilo)
        2.5
        5.4
        200
        """
        return sorted(list_of_things, key=lambda things: things.weight_in_kilo)


if __name__ == '__main__':
    doctest.testmod(verbose=True)