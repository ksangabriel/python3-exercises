# Karl San Gabriel
# www.turreta.com
# Copyright 2019

# Exercise 6
# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
# 
# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)
#

def main():
    user_input = input('Please enter a string: ')

    temp_list = list(user_input)
    temp_list.reverse()

    rev_str = "".join(temp_list)

    if user_input == rev_str:
        print('Palindrome!')
    else:
        print('Not Palindrome!')
 
if __name__ == '__main__': main()
