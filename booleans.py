#Booleans are True and False Logic

#any object that isn't empty is true
#Chain together booleans using and  -  or  -
#and works with all objects
#or works with either value. If either value is true, its true
#and or works with both objects
#Chaining works the same as order of operations in math

#Empty strings are false
bool ("")

#and is true because both objects are true
True and True

#and is false because third object is false
True and True and False

#or is true because one object is true
False or False or True

#and is false because the 2nd string is false
(False or False or True) and (True and False)

#and not is false because the 2nd variable is false
is_smoker = True
has_kids = True
has_kids and not is_smoker

