Class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo():  # - method display the bike's prices, maximum speed, and the total miles.
        print("price: ",self.price,"max_speed:", self.max_speed, "miles ridded:", miles)

    def ride():          # - displays "Riding" on the screen and increase the total miles ridden by 10
        self.miles += 10
        print("Riding... miles ridden:", str(self.miles))

    def reverse():  # - displays "Reversing" on the screen and decrease the total miles ridden by 5...
        self.miles -= 5            print("Riding in Reverse... miles ridden:", self.miles)

    

# create instances and run methods
bike1 = Bike(99.99, 12)
bike1.drive()
bike1.drive()
bike1.drive()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike(139.99, 20)
bike2.drive()
bike2.drive()
bike2.reverse()
bike2.reverse()
bik2.displayInfo()
Copy
