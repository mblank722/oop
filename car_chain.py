# Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed,
# fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%.
#
# Create six different instances of the class Car. In the class have a method called display_all() that returns
# all the information about the car as a string. In your __init__(), call this display_all() method
# to display information about the car once the attributes have been defined.
#
# A sample output would be like this:
#
# Price: 2000
# Speed: 35mph
# Fuel: Full
# Mileage: 15mpg
# Tax: 0.12




class Car(object):

    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.displayAll()

    def displayAll(self):  # - method display the bike's prices, maximum speed, and the total miles.
        print "price: $", self.price
        print "speed:",  self.speed
        print "fuel:",  self.fuel
        print "mileage", self.mileage
        print "tax:",  self.tax
        print " "


car1=Car(1000, 10, "full", 11)
car1=Car(2000, 20, "hi-test", 22)
car1=Car(30000, 30, "hi-test3", 3)
