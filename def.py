# def defines a function
# give your def a name the define what parameters are expected when its called tab in body
# the values you put into a function are called arguments - in this ex text is the first argument
# def is used to call the same functions to apply parameters to strings


def yell(text):
    text = text.upper()
    number_of_characters = len(text)
    result = text + "!" * (number_of_characters // 2)
    print(result)

yell("You are doing great")
yell("Don't forget to ask for help")
yell("Don't repeat yourself")