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
# Write a program to prompt for a score between 0.0 and 1.0. If the score is out
# of range, print an error message. If the score is between 0.0 and 1.0, print a
# grade using the following table:
#
#  Score   Grade
# >= 0.9     A
# >= 8.0     B
# >= 7.0     C
# >= 6.0     D
#  > 6.0     F
#
# [example output]:
#
# Enter score: 0.95
# A
# 
# Enter score: perfect
# Bad score
#
# Enter score: 10.0
# Bad score
#
# Enter score: 0.75
# C
#
# Enter score: 0.5
# F
#-------------------------------------------------------------------------------

try:
    score = float(input('Enter score: '))
    if score < 0.0 or score > 1.0:
        print('Bad score')
    else:
        if score >= 0.9:
            print('A')
        elif score >= 0.8:
            print('B')
        elif score >= 0.7:
            print('C')
        elif score >= 0.6:
            print('D')
        else:
            print('F')

except:
    print('Bad score')
