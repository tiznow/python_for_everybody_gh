#-------------------------------------------------------------------------------
# Course:    Python for Everybody
#
# Student:   Christopher Martinez
#
# Date:      09/27/2021
#
#
# Specification:
#
# Write a program to prompt the user for hours and rate per hour using input to
# compute gross pay. Pay the hourly rate for hours up to 40 and 1.5 times the
# hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of
# 10.50 per hour to test the program (the pay should be 498.75). You should use
# __input__ to read a string and __float()__ to convert the string to a number.
# Do not worry about error checking the user input - assume the user types
# numbers properly.
#-------------------------------------------------------------------------------
hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

if hours <= 40:
    pay = rate * hours

else:
    pay = (rate * 40) + (hours - 40) * (rate * 1.5)

print(pay)
