'''

        Python While Loops
                - Techie Programmer

Python Loops

Python has two primitive loop commands:

while loops
for loops

'''


# The while Loop

i = 2
while i < 5:
  print(i)
  i += 1


# The break Statement

i = 2
while i < 5:
  print(i)
  if i == 3:
    break
  i += 1


# The continue Statement

i = 2
while i < 5:
  i += 1
  if i == 3:
    continue
  print(i)


# The else Statement

i = 2
while i < 5:
  print(i)
  i += 1
else:
  print("i is no longer less than 5")
