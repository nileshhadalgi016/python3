'''
            Python  If..elif..else
                    - techie Programmer !

Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

'''
a = 10
b = 20
c = 10


# If statement:

if a != b :
    print("hello")
    print("world")

# Indentation
if a == b :
    print("hello")

# Elif

if a == b:
    print("a = b")
elif a == c:
    print('a = c')

# Else
if a == b:
    print("a = b")
elif a != c:
    print('a = c')
else :
    print(' conditions Failed')



# Short Hand
if a==c : print('yes')

# Short Hand If ... Else

print('yes') if a!=c else print('no')

# And

if a == c and a != b:
    print('condition satisfied ')

# or

if a != c or a != b:
    print('condition satisfied ')

# Nested

if a == c :

    if a != b :
        print("both Condition satisfied")


# The pass Statement

if a==c:
    pass
