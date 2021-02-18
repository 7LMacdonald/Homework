# Heading comments here
import random

# Code telling us the variables are here for later use
str_name = input("What is your name please? ").title()
int_age = int(input("{}, What is your age please? ".format(str_name)))
int_guess = random.randint(-10, 10)

# code description here (What does the code do?)
print("Your name is '{}', your age is'{:.2f}'and your favourate" /
         " number is '{}'".format(str_name, int_age, int_guess))
