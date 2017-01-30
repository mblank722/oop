# Now, create another class called Dog that inherits everything that the Animal
# does and has, but
#     1) have the default health be 150 and
#     2) add a new method called pet, which when invoked, increase the health by 5.
# Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth().

Now, create another class called Dragon that also inherits everything from Animal,
but
    1) have the default health be 170 and
    2) add a new method called fly, which when invoked, decreased the health by 10.
Have the Dragon walk() three times, run() twice, fly() twice, and have it displayHealth().
When the Dragon's displayHealth function is called, have it say 'this is a dragon!'
    before it displays the default information (by calling the parent's displayHealth function).

Now for the first instance of the animal (instance called 'animal'), try calling fly() or pet() and make sure this doesn't work.  (-:
class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0


    def displayInfo(self):  # - method display the bike's prices, maximum speed, and the total miles.
        print "price: $", self.price, "max_speed:",  self.max_speed, "miles ridden:",  self.miles
        return self

    def ride(self):          # - displays "Riding" on the screen and increase the total miles ridden by 10
        self.miles += 10
        print "Riding... miles ridden:", self.miles
        return self

    def reverse(self):  # - displays "Reversing" on the screen and decrease the total miles ridden by 5...
        self.miles -= 5
        print "Riding in Reverse... miles ridden:" , self.miles
        return self



# create instances and run methods
bike1 = Bike(99.99, 12)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike1.ride().ride().ride().reverse().displayInfo()

bike2 = Bike(139.99, 20)
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()
