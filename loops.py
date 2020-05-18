# loops
# all caps is a naming convention for constants - it will never be changed while program runs
import sys

MASTER_PASSWORD = 'opensesame'
password = input("Please enter the secret password:  ")
attempt_count = 1
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("Too many invalid password attempts")
    password = input("Invalid password, try again:  ")
    attempt_count += 1
print("Welcome to secret town.")