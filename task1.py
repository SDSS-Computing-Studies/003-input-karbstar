#! python3
"""
Ask the user for their name and their email address.
You will need to use the .strip() method for this assignment. Be aware of your 
(2 points)

Inputs:
 name = .strip()
 email= .strip()

Sample output:
 Your name is Joe Lunchbox, and your email is joe@koolsandwiches.org.
"""
x = input("what is your Name").strip()
y = input("email").strip()
print(f"Your name is {x}, and your email is {y}")