"""
                Python Lambda
                        -Techie Programmer


            A lambda function is a small anonymous function.


        Syntax :
                lambda arguments : expression


"""

# Example

x = lambda a: a + 20

print(x(5))

# Example 2

x = lambda a, b: a * b
print(x(5, 6))


# Another Used Case Of Lambda

def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(10))
