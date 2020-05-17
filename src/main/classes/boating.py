from src.main.classes.base_camping import BaseCamping


class Boating(BaseCamping):
    def __init__(self, name, producer, things_type, weight_in_kilo, price_in_uah,
                 availability_of_boat=None):
        super().__init__(name, producer, things_type, weight_in_kilo, price_in_uah)
        self.availability_of_boat = availability_of_boat

    def __del__(self):
        print("Boating closed")
        return

    def __str__(self):
        name = "Name: {0}\n".format(self.name)
        producer = "Producer: {0}\n".format(self.producer)
        things_type = "Genre type: {0}\n".format(self.things_type)
        weight_in_kilo = "Weight in kilo: {0}\n".format(self.weight_in_kilo)
        price_in_uah = "Price in UAH: {0}\n".format(self.price_in_uah)
        availability_of_boat = "Availability of boat: {0}\n".format(self.availability_of_boat)

        return name + producer + things_type + weight_in_kilo + price_in_uah + availability_of_boat

    def __repr__(self):
        return 'ThingsForBoating(name=' + self.name + ', producer=' + str(self.producer) + \
               ', things_type=' + str(self.things_type) + ', weight_in_kilo=' + str(self.weight_in_kilo) + \
               ', price_in_uah=' + str(self.price_in_uah) + ', availability_of_tent=' + str(self.availability_of_boat) + ')'