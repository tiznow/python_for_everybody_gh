#-------------------------------------------------------------------------------
# Course:    Python for Everybody
#
# Student:   Christopher Martinez
#
# Date:      06/01/2021
#
#
# Specification:
#
# Rewrite your pay program using 'try' and 'except' so that your program handles
# non-numeric input gracefully by printing a message and exiting the program.
# The following shows two executions of the program:
#
# [example output]:
#
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
#
#-------------------------------------------------------------------------------

try:
    hours = int(input('Enter Hours: '))
    rate  = float(input('Enter Rate: '))

    pay = 0.0
    if hours <= 40:
        pay = rate * hours
    else:
        pay = 40 * rate + (hours - 40) * 1.5 * rate

    print('Pay:', pay)

except:
    print('Error, please enter numeric input')
