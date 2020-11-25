"""

                    Python Classes and Objects
                            - Techie Programmer.

        A Class is like an object constructor, or a "blueprint" for creating objects.

"""


#  Create a Class

class myClass:
    x = 10


# Create A Object

o = myClass()
print(o.x)


# The __init__() Function


class person:
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName


p = person("techie", "programmer")
print(p.name)
print(p.lastName)

# Object Methods
class person:
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName

    def printing(self):
        print("name is : ",self.name,' ', self.lastName)

p1 = person("joe",'Dan')

p1.printing()

# The self Parameter

# Modify Object Properties
a = 10
a =20

p1.name = "ryan"


# Delete Object Properties

del p1.name

# Delete Objects

del p1

# The pass Statement

class MystupidClass:
    pass
