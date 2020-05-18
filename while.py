#loops - only two - for and while
#loops iterate over a given sequence (work their way through items in an interval)
    #ex: for some_variable in [1,2,3]
        #for will take each item in the brackets and will put it in the variable name assigned - some_variable
        #then it will execute the code that's inside the loop meaning the code following the for statement

# Problem 1: Warm the oven
# Write a while loop that checks to see if the oven
# is 350 degrees. If it is, print "The oven is ready!"
# If it's not, increase current_oven_temp by 25 and print
# out the current temperature.

current_oven_temp = 75

while current_oven_temp < 350:
    current_oven_temp += 25
    print(current_oven_temp)
else:
    print("The oven is ready")

# Solution 1 here

# Problem 2: Total and average
# Complete the following function so that it asks for
# numbers from the user until they enter 'q' to quit.
# When they quit, print out the list of numbers,
# the sum and the average of all of the numbers.
#THIS CREATES AN INFINITE LOOP!
def total_and_average():
    numbers = []
    while True:
        num = input("Give me a number, or 'q' to quit:  ").lower()
        if num == 'q':
            break
        try:
            numbers.append(float(num))
        except ValueError:
            continue
    print("You entered:  ", numbers)
    print("The total is: ", sum(numbers))
    print("The average is: ", sum(numbers)/len(numbers))

total_and_average()

# Problem 3: Missbuzz
# Write a while loop that increments current by 1
# If the new number is divisible by 3, 5, or both,
# print out the number. Otherwise, skip it.
# Break out of the loop when current is equal to 101.

current = 1

while current <101:
    if not current % 3 or current % 5 == 0:
        print(current)
    current += 1