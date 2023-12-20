class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch(instance):
        instance.on = not instance.on

    def make_hot_water(self):
        self.water = True

kenwood = Kettle("Kenwood", 8.99)
kenwood.make_hot_water()
print(kenwood.water)
print(kenwood.__dict__)
