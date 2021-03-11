"""
input: integer == month, integer == year
output: integer - number of days in that month

Notes:
leap year happens % 4 == 0 years --> feb has 29 instead of 28
EXCEPT year % 100  = NOT leap year
EXCEPT year % 400 = IS leap year

Pseudocode:
empty dictionary = months (nums) key: days (value)

check to see if looking for feb.
if looking at feb = leap year check

return diction[month] = value
"""

def days_in_month(month, year):
    num_of_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    if year % 100 == 0 and year % 400 != 0:
        return num_of_days[month]

    if month == 2 and year % 4 == 0:
        return 29

    return num_of_days[month]


month1 = 1
month2 = 2
print(days_in_month(month1, 1980)) #31
print(days_in_month(month2, 400)) #29
print(days_in_month(2, 1000)) #28
