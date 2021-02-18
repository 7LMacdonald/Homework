# Heading comments here
# LIBRARIES AND OTHER IMPORTS """
import random


# THE DEFINITIONS GO ABOVE THE CODE SINCE THEY ARE CALLABLE CODE """
# A definition to collect and return the user name and age
def user():
    str_name = input("What is your name please? ").title()
    int_age = int(input("{},  what is your age please? ".format(str_name)))
    return str_name, int_age


# A definition to generate a random number between -10 and 10
def guess():
    int_guess = random.randint(-10, 10)
    return int_guess


# Outputs the collected information for the user to see
def publish():
    str_name, int_age = user()
    int_guess = guess()
    print("your name is '{}', your age is '{:.2f}' and your" /
          " favourate numbe is '{}'".format(str_name, int_age, int_guess))
    return str_name, int_age, int_guess
    # Only needed if variables are to be used elsewere

publish()
