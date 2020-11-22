"""
            Python For Loops
                    - Techie Programmer
A for loop is used for iterating over a sequence
(that is either a list, a tuple, a dictionary, a set, or a string).
"""

# Looping Through a String
for x in "banana":
  print(x)

# The break Statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break



# The continue Statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# The range() Function

for x in range(1,6,2):
  print(x)

# Else in For Loop

for x in range(6):
  print(x)
else:
  print("Finally finished!")


# Nested Loops

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# The pass Statement

for x in [0, 1, 2]:
  pass
