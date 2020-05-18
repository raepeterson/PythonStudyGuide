# some functions return a value
    # ex 1 you call the function len and pass it an object it gives you a value back
    # ex 2 is when I call the upper method on a strings it created us a new string and returned it
# methods are just owned functions
# functions can take arguments, process them, and then return a value to the caller of your function
# rounding function rounds down
# import module (tools) for more functions - include at top of file
# use import math then math.ceil to return an integer value
# try
# except
# as gives a reference to the exception that was raised

#Can you please raise a ValueError if the product_idea is less than 3 characters long? product_idea is a string.
def suggest(product_idea):
    if len(product_idea) < 3:
        raise ValueError
    return product_idea + "inator"