# some functions return a value
    # ex 1 you call the function len and pass it an object it gives you a value back
    # ex 2 is when I call the upper method on a strings it created us a new string and returned it
# methods are just owned functions
# functions can take arguments, process them, and then return a value to the caller of your function
# rounding function rounds down
# import module (tools) for more functions - include at top of file
# use import math then math.ceil to return an integer value

import math

def split_check(total, number_of_people):
    #math.ceil returns an integer value
    #no need to assign variable - return is returning the value to the caller of split_check
    return math.ceil(total / number_of_people)

total_due = float(input("What is the total?  "))
number_of_people = int(input("How many people?  "))

amount_due = split_check(total_due, number_of_people)

print("Each person owes ${}".format (amount_due))