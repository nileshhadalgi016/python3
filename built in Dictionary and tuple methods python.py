# Python Tuple Methods

# Python has two built-in methods that you can use on tuples.

my_tuple = (1, 2, 3, 4, 6, 5, 3, 7)

# Method      	Description

# count()	        Returns the number of times a specified value occurs in a tuple
n = my_tuple.count(3)
print(n)

# index() Searches the tuple for a specified value and returns the position of where it was found
i = my_tuple.index(2)
print(i)

# Python Dictionary Methods
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Method	    Description

# copy()	    Returns a copy of the dictionary

x = car.copy()

print(x)

# fromkeys()    Returns a dictionary with the specified keys and value
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)

# get()	        Returns the value of the specified key
x = car.get("model")
print(x)

# items()   	Returns a list containing a tuple for each key value pair
x = car.items()

print(x)

# keys()	    Returns a list containing the dictionary's keys
x = car.keys()

print(x)

# pop()	        Removes the element with the specified key
car.pop("model")

print(car)

# popitem() 	Removes the last inserted key-value pair
car.popitem()

print(car)

# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
x = car.setdefault("model", "Bronco")

print(x)

# update()	    Updates the dictionary with the specified key-value pairs
car.update({"color": "White"})

print(car)

# values()	    Returns a list of all the values in the dictionary
x = car.values()

print(x)

# clear()	    Removes all the elements from the dictionary

car.clear()

print(car)
