
#The code in the using_a_function.py is making use of an external function named tweet.


#The code here is intended to make a console based application that sends tweets. I've written the first part for you.


#For this first task, can you please just call the tweet function and pass in the message that the user enters?

"""
This is importing a function named `tweet` from a file
    that we unfortunately don't have access to change.

You use it like so:
>>> tweet("Hello this is my tweet")

If the function cannot connect to Twitter,
    the function will raise a `CommunicationError`
If the message is too long,
    the function will raise a `MessageTooLongError`
"""
from twitter import (
    tweet,
    MessageTooLongError,
    CommunicationError,
)


message = input("What would you like to tweet?  ")
tweet(message)



