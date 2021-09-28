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
# Write a program to prompt the user for hours and rate per hour to compute
# gross pay.
#
# [example output]:
#
# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25
#
#-------------------------------------------------------------------------------

hours = input('Enter Hours: ')
rate  = input('Enter Rate: ')
pay   = float(hours) * float(rate)
print('Pay:', pay)
