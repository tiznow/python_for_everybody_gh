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
# Write a program which prompts the user for a Celsius temperature, convert the
# temperature to Fahrenheit, and print out the converted temperature.
#
#-------------------------------------------------------------------------------

celsius = float(input('Enter a Celsius temperature: '))
fahrenheit = celsius * 1.8 + 32
print(celsius, 'Celsius ==', fahrenheit, 'Fahrenheit')
