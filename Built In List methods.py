"""
BY : techie Programmer 

Python has a set of built-in methods that you can use on lists/arrays.

Method	        Description

append()	    Adds an element at the end of the list
clear()	        Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the specified value
extend()	    Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()    	Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()      	Removes the first item with the specified value
reverse()	    Reverses the order of the list
sort()	        Sorts the list

"""

my_list = [1, 3, 2, 5, 3, 6, 8]

my_list.append(10)
print(my_list)

new_list = my_list.copy()
print(new_list)

n = my_list.count(3)
print(n)

n_list = [12, 23, 45, 567]
n_list.extend(my_list)
print(n_list)

x = my_list.index(3)
print(x)

my_list.insert(1, 123)
print(my_list)

data = my_list.pop(0)
print(data)

my_list.remove(123)
print(my_list)

my_list.reverse()
print(my_list)

my_list.sort()
print(my_list)

my_list.clear()
print(my_list)
