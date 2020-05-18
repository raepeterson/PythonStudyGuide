# When will the user see the text "Here you go!" outputted? Answer: as soon as the input contains the string "please"

request = input("What would you like?  ")
while "please" not in request:
    request = input("You seem to be missing a magic word.  What would you like?  ")
print("Here you go!")