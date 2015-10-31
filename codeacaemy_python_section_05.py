# Conitionals & Control Flow

# 5.1--------------------------------------------------------------------------#
def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()

# 5.2--------------------------------------------------------------------------#
# Assign True or False as appropriate on the lines below!

# Set this to True if 17 < 328 or to False if it is not.
bool_one = True   # We did this one for you!

# Set this to True if 100 == (2 * 50) or to False otherwise.
bool_two = 100 == (2 * 50)

# Set this to True if 19 <= 19 or to False if it is not.
bool_three = 19 <= 19

# Set this to True if -22 >= -18 or to False if it is not.
bool_four = -22 >= -18

# Set this to True if 99 != (98 + 1) or to False otherwise.
bool_five = 99 != (98 + 1)

# 5.3--------------------------------------------------------------------------#
# Assign True or False as appropriate on the lines below!

# (20 - 10) > 15
bool_one = False    # We did this one for you!

# (10 + 17) == 3**16
# Remember that ** can be read as 'to the power of'. 3**16 is about 43 million.
bool_two = (10 + 17) == 3**16

# 1**2 <= -1
bool_three = 1**2 <= -1

# 40 * 4 >= -4
bool_four = 40 * 4 >= -4

# 100 != 10**2
bool_five = 100 != 10**2

# 5.4--------------------------------------------------------------------------#
# Create comparative statements as appropriate on the lines below!

# Make me true!
bool_one = 3 < 5  # We already did this one for you!

# Make me false!
bool_two = 2 == 3

# Make me true!
bool_three = 2 == 2

# Make me false!
bool_four = 3 == 1

# Make me true!
bool_five = 3 != 1

# 5.5--------------------------------------------------------------------------#
"""
     Boolean Operators
------------------------      True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True

"""

# 5.6--------------------------------------------------------------------------#
bool_one = False and False

bool_two = -(-(-(-2))) == -2 and 4 >= 16**0.5

bool_three = 19 % 4 != 300 / 10 / 10 and False

bool_four = -(1**2) < 2**0 and 10 % 10 <= 20 - 10 * 2

bool_five = True and True

# 5.7--------------------------------------------------------------------------#
bool_one = 2**3 == 108 % 100 or 'Cleese' == 'King Arthur'

bool_two = True or False

bool_three = 100**0.5 >= 50 or False

bool_four = True or True

bool_five = 1**100 == 100**1 or 3 * 2 * 1 != 3 + 2 + 1

# 5.8--------------------------------------------------------------------------#
bool_one = not True

bool_two = not 3**4 < 4**3

bool_three = not 10 % 3 <= 10 % 2

bool_four = not 3**2 + 4**2 != 5**2

bool_five = not not False

# 5.9--------------------------------------------------------------------------#
bool_one = False or not True and True

bool_two = False and not True or True

bool_three = True and not (False or False)

bool_four = not not True or False and not True

bool_five = False or not (True and True)

# 5.10-------------------------------------------------------------------------#
# Use boolean expressions as appropriate on the lines below!

# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!

# Make me true!
bool_two = 1 == 1 and 2 == 2

# Make me false!
bool_three = 2 > 3 and True

# Make me true!
bool_four = True and True and True

# Make me true!
bool_five = True and True and True

# 5.11-------------------------------------------------------------------------#
response = 'Y'

answer = "Left"
if answer == "Left":
    print "This is the Verbal Abuse Room, you heap of parrot droppings!"

# Will the above print statement print to the console?
# Set response to 'Y' if you think so, and 'N' if you think not.

# 5.12-------------------------------------------------------------------------#
def using_control_once():
    if 1 == 1:
        return "Success #1"

def using_control_again():
    if 2 == 2:
        return "Success #2"

print using_control_once()
print using_control_again()

# 5.13-------------------------------------------------------------------------#
answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:
        return False       # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:
        return False       # Make sure this returns False

# 5.14-------------------------------------------------------------------------#
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:
        return -1
    else:
        return 0

print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)

# 5.15-------------------------------------------------------------------------#
# Make sure that the_flying_circus() returns True
def the_flying_circus():
    if True and 1 == 1:    # Start coding here!
        # Don't forget to indent
        # the code inside this block!
        return True
    elif True and 1 != 1:
        # Keep going here.
        # You'll want to add the else statement, too!
        return True
    else:
        return True        
