"""
            Python Functions
                        -Techie Programmer

        A function is a block of code which only runs when it is called.


"""

# Creating a Function

def hello():
    print("hello")


# Calling a Function
hello()

# Arguments

def name(First_name):
    print("name is ",First_name)

name('techie')
name("nilesh")

# Parameters or Arguments?

    # A parameter is the variable listed inside the parentheses in the
    #  function definition.

    # An argument is the value that is sent to the function when it is called.


# Number of Arguments

def fullName(firstName,LastName):
    print(firstName,LastName)

fullName("Nilesh ",'Hadalgi')

# Arbitrary Arguments, *args

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Keyword Arguments

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments, **kwargs

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")



# Default Parameter Value

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# Passing a List as an Argument

l = [1,2,3]

def numb(l):
    print(l[2])
numb(l)

# Return Values

def add(a,b):
    return a+b

print(add(2,4))


# The pass Statement
def add():
    pass
