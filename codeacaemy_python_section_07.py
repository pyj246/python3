# Functions

# 7.1--------------------------------------------------------------------------#
def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print "With tax: %f" % bill
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print "With tip: %f" % bill
    return bill

meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

# 7.2--------------------------------------------------------------------------#
# Define your spam function starting on line 5. You
# can leave the code on line 11 alone for now--we'll
# explain it soon!
def spam():
    """
    Comments
    """
    print "Eggs!"





# Define the spam function above this line.
spam()

# 7.3--------------------------------------------------------------------------#
def square(n):
    """Returns the square of a number."""
    squared = n**2
    print "%d squared is %d." % (n, squared)
    return squared

# Call the square function on line 9! Make sure to
# include the number 10 between the parentheses.

square(10)

# 7.4--------------------------------------------------------------------------#
def power(base, exponent):  # Add your parameters here!
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

power(37,4)  # Add your arguments here!

# 7.5--------------------------------------------------------------------------#
def one_good_turn(n):
    return n + 1

def deserves_another(n):
    return one_good_turn(n) + 2

# 7.6--------------------------------------------------------------------------#
def cube(number):
    return number ** 3

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

# 7.7--------------------------------------------------------------------------#
# Ask Python to print sqrt(25) on line 3.

sqrt(25)

# 7.8--------------------------------------------------------------------------#
# Ask Python to print sqrt(25) on line 3.

import math

print math.sqrt(25)

# 7.9--------------------------------------------------------------------------#
# Import *just* the sqrt function from math on line 3!

from math import sqrt

# 7.10-------------------------------------------------------------------------#
# Import *everything* from the math module on line 3!

from math import *

# 7.11-------------------------------------------------------------------------#
import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!

# 7.12-------------------------------------------------------------------------#
def biggest_number(*args):
    print max(args)
    return max(args)

def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

# 7.13-------------------------------------------------------------------------#
# Set maximum to the max value of any set of numbers on line 3!

maximum = max(1, 2, 3)

print maximum

# 7.14-------------------------------------------------------------------------#
# Set minimum to the min value of any set of numbers on line 3!

minimum = min(1,2,3)

print minimum

# 7.15-------------------------------------------------------------------------#
absolute = abs(-42)

print absolute

# 7.16-------------------------------------------------------------------------#
# Print out the types of an integer, a float,
# and a string on separate lines below.

print type(42)
print type(4.2)
print type('42')

# 7.17-------------------------------------------------------------------------#
def shut_down(s):
    if s == 'yes':
        return 'Shutting down'
    elif s == 'no':
        return 'Shutdown aborted'
    else:
        return 'Sorry'

# 7.18-------------------------------------------------------------------------#
from math import *

print math.sqrt(13689)

# 7.19-------------------------------------------------------------------------#
def distance_from_zero(value):
    valueType = type(value)
    if valueType == int or valueType == float:
        return abs(value)
    else:
        return 'Nope'
