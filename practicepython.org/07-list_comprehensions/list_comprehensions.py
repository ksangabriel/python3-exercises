# Karl San Gabriel
# www.turreta.com
# Copyright 2019

# Exercise 7
# https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
# 
# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
# Write one line of Python that takes this list a and makes a new list that has only the even 
# elements of this list in it.
#

def main():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    even_list = list(filter(lambda x: x % 2 == 0, a))
    print(even_list)
 
if __name__ == '__main__': main()
