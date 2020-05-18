# = assigns value
# == compares two objects
# != says the strings are not the same
# >= compares whether numbers or strings are greater than or equal to
    #strings are compared in alaphabetical order
        #ex:sushine is great than rain
# expressions follow if
# elif allows you to chain different conditions


first_name = input("What is your first name?  ")
print("Hello,", first_name)
if first_name == "Craig":
    print(first_name, "is learning Python")
elif first_name == "Maximillian":
    print(first_name, "is learning with fellow students in the community!")
else:
    age = int(input("How old are you?  "))
    if age <= 6:
        print("Wow you're {}! If you can read you should learn too!".format(age))
    print("You should totally learn Python, {}!".format(first_name))
print("Have a great day {}!".format(first_name))
