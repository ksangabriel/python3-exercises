# Karl San Gabriel
# www.turreta.com
# Copyright 2019

# Exercise 4
# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
# 
# Create a program that asks the user for a number and then prints out a list 
# of all the divisors of that number. (If you don’t know what a divisor is, 
# it is a number that divides evenly into another number. For example, 13 
# is a divisor of 26 because 26 / 13 has no remainder.)
#

def main():

    val = int(input('Enter an integer: '))
    max_range = val + 1
    divisors = list(filter(lambda x: val % x == 0, range(1, max_range)))
    print(divisors)
    
if __name__ == '__main__': main()
