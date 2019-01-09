# Karl San Gabriel
# www.turreta.com
# Copyright 2019

# Exercise 1 
# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
# 
# Create a program that asks the user to enter their name and their age. Print 
# out a message addressed to them that tells them the year that they will turn 
# 100 years old.
#
# Extras:
# 
# 1. Add on to the previous program by asking the user for another number and 
#    printing out that many copies of the previous message. (Hint: order of 
#    operations exists in Python)
#
# 2. Print out that many copies of the previous message on separate lines. 
#    (Hint: the string "\n is the same as pressing the ENTER button)
#
import datetime

def main():
    name = input("What is your name?")
    age = int(input("How old are you?"))
    message_count = int(input("How many times you want to be greeted?"))

    current_year = datetime.date.today().year

    i = 0
    while i < message_count:
        print(f'Good day, {name}. You will turn 100 years old in {current_year + (100 - age)}')
        i+=1

if __name__ == '__main__': main()

