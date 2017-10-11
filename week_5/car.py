class Car(object):
    def __init__(self, price, speed, fuel, mpg):
        self.price = price
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.speed = speed
        self.fuel = fuel
        self.mpg = mpg

    def display_all(self):
        print "Price: {}".format(str(self.price))
        print "Speed: {}mph".format(str(self.speed))
        print "Fuel: {}".format(str(self.fuel))
        print "MPG: {}mpg".format(str(self.mpg))
        print "Tax: {}".format(str(self.tax))


car1 = Car(2000,35,"Full",15)
car1.display_all()

car2 = Car(2000,5,"Not Full",105)
car2.display_all()

car3 = Car(2000,15,"Kind of Full",95)
car3.display_all()

car4 = Car(2000,25,"Full",25)
car4.display_all()

car5 = Car(2000,45,"Empty",25)
car5.display_all()

car6 = Car(2000000,35,"Empty",15)
car6.display_all()