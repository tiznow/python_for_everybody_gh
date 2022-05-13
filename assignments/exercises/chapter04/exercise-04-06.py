#-------------------------------------------------------------------------------
# Course:    Python for Everybody
#
# Student:   Christopher Martinez
#
# Date:      09/29/2021
#
#
# Specification:
#
# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
# create a function called computepay() which takes two parameters 
# (hours and rate).
#
# Example Output:
#
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0
#-------------------------------------------------------------------------------
def computepay(hours, rate):
    if hours <= 40:
        return hours * rate
    else:
        return 40 * rate + (hours - 40) * 1.5 * rate

try:
    hours = int(input('Enter Hours: '))
    rate  = float(input('Enter Rate: '))

    pay = computepay(hours, rate)

    print('Pay:', pay)

except:
    print('Error, please enter numeric input')
