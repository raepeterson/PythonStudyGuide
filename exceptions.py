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

import math

def split_check(total, number_of_people):
    if number_of_people <=1:
        raise ValueError ("More than 1 person is required to split the check")
    #math.ceil returns an integer value
    #no need to assign variable - return is returning the value to the caller of split_check
    return math.ceil(total / number_of_people)

try:
    total_due = float(input("What is the total?  "))
    number_of_people = int(input("How many people?  "))
    amount_due = split_check(total_due, number_of_people)
# as gives a reference to the exception that was raised
# err means error which is a new variable created to be assigned to the exception that was thrown
# when someone enters an invalid number
except ValueError as err:
    print("Oh no, that's not a valid value, try again!")
    print("({})".format(err))
else:
    print("Each person owes ${}".format (amount_due))
