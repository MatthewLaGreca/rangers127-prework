#Author: Matthew LaGreca

# Question 1: Write a function to print “hello_USERNAME!” 
# USERNAME is the input of the function.

def hello_name(user_name):
    """prints "hello_user_name!" """

    # Checking for valid input
    if type(user_name) != str:
        print('invalid input; "user_name" needs to be a string')
    
    # Printing 'hello_user_name!'
    else:
        print(f'hello_{user_name}!')

#----------------------------------------------------------------------
# Question 2: Write a python function, first_odds 
# that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    """Prints the first odd numbers from 1 to 100"""
    print('The odd numbers from 1-100 are: ', end = '')

    # Looping through 1-100, using a step size of 2
    for i in range(1,100,2):
        print(f'{i}', end = ' ')

#----------------------------------------------------------------------
# Question 3: Please write a Python function, max_num_in_list 
# to return the max number of a given list. 
# The first line of the code has been defined as below.

def max_num_in_list(a_list):
    """Given a list, this function will return the max number
    *Notes:
    - Will not work with complex numbers
    - will not check numbers in lists, tuples and 
    dictionaries in submitted list"""

    # checks to see if list is empty:
    if a_list == []:
        print('The submitted list is empty')
        return None 
    
    # declaring variables
    cur_max = 0.0

    # determines the max and sets it in cur_max:
    for i in range(len(a_list)):

        # checking to see if the current list item is of a numeric type
        if not isinstance(a_list[i], (int,float)):
            continue
        
        # if it's not, is it greater than the current max?
        else:
            if cur_max == 0:
                cur_max = float(a_list[i])
            elif cur_max < float(a_list[i]):
                cur_max = float(a_list[i])
    return cur_max

# my_list = [1, 2, 5, 69, -200, '2 million', 'Welven', '999999999', .2, {}, [], 420690.124350125]
# print(max_num_in_list(my_list))
# print(my_list)
# print(max_num_in_list([]))

#-----------------------------------------------------------------------
# Question 4: Write a function to return if the given year is a 
# leap year. A leap year is divisible by 4, but not divisible by 
# 100, unless it is also divisible by 400. The return should be 
# boolean Type (true/false).

def is_leap_year(a_year):
    # Error Checking
    if not isinstance(a_year, int):
        return "Not a valid input, please input a whole number integer"
    
    # Divisible by 4?
    if a_year % 4 == 0:

        # Divisible by 100?
        if a_year % 100 == 0:

            # Divisible by 400?
            if a_year % 400 == 0:
                return True
            else:
                return False
        else: 
            return True
    else:
        return False

# print(is_leap_year('2404'))

#----------------------------------------------------------------------
# Question 5:
# Write a function to check to see if all numbers in list are 
# consecutive numbers. For example, [2,3,4,5,6,7] are consecutive 
# numbers, but [1,2,4,5] are not consecutive numbers. The return 
# should be boolean Type.

def is_consecutive(a_list):
    for i in range(len(a_list)):
        if not isinstance(a_list[i], int):
            return 'Not a valid input.  Please submit a list of integers'
        if i == 0:
            continue
        elif a_list[i] != a_list[i-1] + 1:
            return False
    return True

# print(is_consecutive([1,2,3]))
# print(is_consecutive([1,2,4]))
# print(is_consecutive([1,2,'3']))
# print(is_consecutive([-1,0,1]))
# print(is_consecutive([3,2,1]))