class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch(instance):
        instance.on = not instance.on

kenwood = Kettle("Kenwood", 8.99)
kettle1 = Kettle("whatever_type", 9)
print(kenwood.make)
print(kenwood.price)
print(kenwood.on)
kenwood.power_source = "gas"
print(Kettle.power_source)
print(kenwood.power_source)
