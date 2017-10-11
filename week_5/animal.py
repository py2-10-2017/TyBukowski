class Animal(object):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
    
    def displayHealth(self):
        print 'Name: {0}'.format(self.name)
        print 'health: {0}'.format(self.health)

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name, 150)

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name, 170)

    def fly(self):
        self.health -= 10
        return self
    
    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print 'I am a Dragon'
        return self


# a = Animal('Rover')
# a.walk().walk().walk().run().run().displayHealth()

# b = Dog('Spot')
# b.walk().walk().walk().run().run().pet().fly().displayHealth()

#     b.walk().walk().walk().run().run().pet().fly().displayHealth()
# AttributeError: 'Dog' object has no attribute 'fly'

# c = Dragon('Draco')
# c.walk().run().fly().displayHealth()

# d = Animal('Chewy')
# d.walk().run().displayHealth()

# d.walk().run().fly().displayHealth()
# AttributeError: 'Animal' object has no attribute 'fly'
#   d.walk().run().pet().displayHealth()
# AttributeError: 'Animal' object has no attribute 'pet'