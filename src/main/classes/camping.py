from src.main.classes.base_camping import BaseCamping


class Camping(BaseCamping):
    def __init__(self, name, producer, things_type, weight_in_kilo, price_in_uah,
                 availability_of_tent=None):
        super().__init__(name, producer, things_type, weight_in_kilo, price_in_uah)
        self.availability_of_tent = availability_of_tent

    def __del__(self):
        print("Camping closed")
        return

    def __str__(self):
        name = "Name: {0}\n".format(self.name)
        producer = "Producer: {0}\n".format(self.producer)
        things_type = "Genre type: {0}\n".format(self.things_type)
        weight_in_kilo = "Weight in kilo: {0}\n".format(self.weight_in_kilo)
        price_in_uah = "Price in UAH: {0}\n".format(self.price_in_uah)
        availability_of_tent = "Availability of tent: {0}\n".format(self.availability_of_tent)

        return name + producer + things_type + weight_in_kilo + price_in_uah + availability_of_tent

    def __repr__(self):
        return 'ThingsForCamping(name=' + self.name + ', producer=' + str(self.producer) + \
               ', things_type=' + str(self.things_type) + ', weight_in_kilo=' + str(self.weight_in_kilo) + \
               ', price_in_uah=' + str(self.price_in_uah) + ', availability_of_tent=' + str(self.availability_of_tent) + ')'
