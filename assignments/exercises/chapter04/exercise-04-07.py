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
# Exercise 7: Rewrite the grade program from the previous chapter using a
# function called computegrade() that takes a score as its parameter and returns
# a grade as a string.
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
def computegrade(score):
    if score < 0.0 or score > 1.0:
        return 'Bad score'
    else:
        if score >= 0.9:
            return 'A'
        elif score >= 0.8:
            return 'B'
        elif score >= 0.7:
            return 'C'
        elif score >= 0.6:
            return 'D'
        else:
            return 'F'

try:
    score = float(input('Enter score: '))
    grade = computegrade(score)
    print(grade)

except:
    print('Bad score')
