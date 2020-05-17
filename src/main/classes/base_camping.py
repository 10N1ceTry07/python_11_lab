from src.main.classes.things_type import ThingsType


class BaseCamping:
    def __init__(self, name=None, producer=None, things_type=ThingsType.HIKING, weight_in_kilo=None, price_in_uah=None):
        self.name = name
        self.producer = producer
        self.things_type = things_type
        self.weight_in_kilo = weight_in_kilo
        self.price_in_uah = price_in_uah

    def __del__(self):
        print("camping deleted")
        return

    def __str__(self):
        name = "Name: {0}\n".format(self.name)
        producer = "Producer: {0}\n".format(self.producer)
        things_type = "Genre type: {0}\n".format(self.things_type)
        weight_in_kilo = "Weight in kilo: {0}\n".format(self.weight_in_kilo)
        price_in_uah = "Price in UAH: {0}\n".format(self.price_in_uah)

        return name + producer + things_type + weight_in_kilo + price_in_uah

    def __repr__(self):
        return 'ThingsForBaseCamping(name=' + self.name + ', producer=' + str(self.producer) + \
               ', things_type=' + str(self.things_type) + ', weight_in_kilo=' + str(self.weight_in_kilo) + \
               ', price_in_uah=' + str(self.price_in_uah) + ')'
