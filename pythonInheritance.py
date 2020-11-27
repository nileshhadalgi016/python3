"""

                        Python Inheritance
                                - Techie Programmer

Inheritance allows us to define a class that inherits all the methods and properties from another class.

"""


# Create a Parent Class

class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printit(self):
        print(self.fname, self.lname)


p1 = person("techie", "programmer")
print(p1.fname)
p1.printit()


# Create a Child Class

class student(person):
    def __init__(self,fname, lname,grad):
        person.__init__(self,fname, lname)
        self.grad = grad

    def gradYear(self):
        print(self.grad)


s1 = student("techie", "programmer",2020)
s1.printit()
s1.gradYear()

