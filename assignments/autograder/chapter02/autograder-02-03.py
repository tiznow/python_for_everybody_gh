#-------------------------------------------------------------------------------
# Course:    Python for Everybody
#
# Student:   Christopher Martinez
#
# Date:      05/31/2021
#
#
# Specification:
#
# Write a program to prompt the user for hours and rate per hour using input to
# compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the
# program (the pay should be 96.25). You should use "input" to read a string and
# float() to convert the string to a number. Do not worry about error checking
# data.
#
#-------------------------------------------------------------------------------

hours = float(input('Enter Hours: '))
rate  = float(input('Enter Rate: '))
pay   = hours * rate
print('Pay:', pay)
