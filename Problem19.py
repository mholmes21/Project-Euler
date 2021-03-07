# How many sundays fell on the first of the month in the 20th century?
# EDITS: 1. Take out the continue. 2. Need (month_len + 1) in the loop range. 3. Need to increment day of week always.
# Still something wrong - ans should be 171

month_len = 0
day = 0 # Monday = 0, Tues = 1, ... , Sunday = 6
sum = 0
leap_year = 0

# Cycle through the years
for year in range(1900, 2001):

    # Deal with leap year business
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 > 0:
            leap_year = 0

        leap_year = 1
    else:
        leap_year = 0

    for month in range(1,13):

        # Deal with month length
        if month == 4 or month == 6 or month == 9 or month == 11:
            month_len = 30
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 10:
            month_len = 31
        else:
            if leap_year:
                month_len = 29
            else:
                month_len = 28

        for date in range(1, month_len + 1):

            # Check if the 1st is a sunday

            if date == 1 and day == 6:
                sum += 1

            day = (day + 1)%7

print (sum, 'Sundays were on the 1st')
