'''
Create a new class called Bike with the following properties/attributes:
price
max_speed
miles
...
Create 3 instances of the Bike class. 

Use the __init__() function to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); In the __init__() also write the code so that the initial miles is set to be 0 whenever a new instance is created.
Add the following functions to this class:
displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().
What would you do to prevent the instance from having negative miles?
Which methods can return self in order to allow chaining methods?
'''

#TRY TO ADD COMMENTS!!!

class bike(object): #bike class created
#set attirbutes in the init function
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0 
    #set the attributes to the object, set default miles to 0

    def displayInfo(self):
        print "Price: ${}".format(str(self.price))
        print "Top speed: {}".format(str(self.max_speed))
        print "Mileage: {}".format(str(self.miles))

    def ride(self):
        print "Riding"
        self.miles += self.miles + 10

    def reverse(self):
        print "Reversing"
       # self.miles = self.miles -=5 --Wont work, will yeild negative
        if self.miles >= 5:
            self.miles -= 5
# instance 1
bike1 = bike(50, 12)
bike1.ride()
bike1.reverse()
bike1.displayInfo()

#instance 2
bike2 = bike(75, 15)
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.displayInfo()

#instance 3
bike3 = bike(500, 30)
bike3.ride()
bike3.ride()
bike3.ride()
bike3.ride()
bike3.ride()
bike3.displayInfo()