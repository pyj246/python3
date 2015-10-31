# Strings & Console Output

# 3.1--------------------------------------------------------------------------#
brian = "Hello life!"

# 3.2--------------------------------------------------------------------------#
# Assign your variables below, each on its own line!

caesar = "Graham"
praline = "John"
viking = "Teresa"

# Put your variables above this line

print caesar
print praline
print viking

# 3.3--------------------------------------------------------------------------#
# The string below is broken. Fix it using the escape backslash!

'This isn\'t flying, this is falling with style!'

# 3.4--------------------------------------------------------------------------#
"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
fifth_letter = 'MONTY'[4]

print fifth_letter

# 3.5--------------------------------------------------------------------------#
parrot = 'Norwegian Blue'
print len(parrot)

# 3.6--------------------------------------------------------------------------#
parrot = "Norwegian Blue"

print parrot.lower()


# 3.7--------------------------------------------------------------------------#
parrot = "norwegian blue"

print parrot.upper()

# 3.8--------------------------------------------------------------------------#
"""Declare and assign your variable on line 4,
then call your method on line 5!"""

pi = 3.14
print str(pi)

# 3.9--------------------------------------------------------------------------#
ministry = "The Ministry of Silly Walks"


print len(ministry)
print ministry.upper()

# 3.10-------------------------------------------------------------------------#
"""Tell Python to print "Monty Python"
to the console on line 4!"""

print 'Monty Python'

# 3.11-------------------------------------------------------------------------#
"""Assign the string "Ping!" to
the variable the_machine_goes on
line 5, then print it out on line 6!"""

the_machine_goes = 'Ping!'
print the_machine_goes

# 3.12-------------------------------------------------------------------------#
# Print the concatenation of "Spam and eggs" on line 3!

print 'Spam ' + 'and ' + 'eggs'

# 3.13-------------------------------------------------------------------------#
# Turn 3.14 into a string on line 3!

print "The value of pi is around " + str(3.14)

# 3.14-------------------------------------------------------------------------#
string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

# 3.15-------------------------------------------------------------------------#
name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

# 3.16-------------------------------------------------------------------------#
# Write your code below, starting on line 3!

my_string = 'none'
print len(my_string)
print my_string.upper()
