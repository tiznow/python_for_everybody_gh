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
# Rewrite your pay computation to give the employee 1.5 times the hourly rate
# for hours worked above 40 hours.
#
# [example output]:
#
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0
#
#-------------------------------------------------------------------------------

hours = int(input('Enter Hours: '))
rate  = float(input('Enter Rate: '))
pay = 0.0

if hours <= 40:
    pay = rate * hours
else:
    pay = 40 * rate + (hours - 40) * 1.5 * rate

print('Pay:', pay)
