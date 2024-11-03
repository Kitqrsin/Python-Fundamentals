birthday_day, birthday_month = input().split()
present_day, present_month, present_year = input().split()

birthday_day = int(birthday_day)
birthday_month = int(birthday_month)
present_day = int(present_day)
present_month = int(present_month)
present_year = int(present_year)

leap_year = False
years_till_leap_year = 0
if present_year % 400 == 0 or (present_year % 4 == 0 and present_year % 100 != 0):
    leap_year = True
else:
    for current_year in range(present_year, 3000):
        if current_year % 400 == 0 or (current_year % 4 == 0 and current_year % 100 != 0):
            break
        years_till_leap_year += 1
day_limit = 0

days_till_next_birthday = 0
months_passed = 0
months_needed = 0
if birthday_day == 29 and birthday_month == 2 and leap_year == False:
    months_needed += years_till_leap_year * 12
if present_month == birthday_month:
    months_needed += 1
elif birthday_month > present_month:
    months_needed += birthday_month - present_month + 1
for current_month in range(months_needed):
    if present_month > 12:
        present_month = 1
    if months_passed >= 1:
        present_day = 0
    if present_month == 1 or present_month == 3 or present_month == 5 or present_month == 7 or present_month == 8 \
            or present_month == 10 or present_month == 12:
        day_limit += 31
    elif present_month == 4 or present_month == 6 or present_month == 9 or present_month == 11:
        day_limit += 30
    elif present_month == 2:
        if leap_year:
            day_limit += 29
        else:
            day_limit += 28
    if present_month == birthday_month:
        if present_month == 2 and leap_year is False:
            if months_passed == years_till_leap_year * 12:
                day_limit = birthday_day
            else:
                day_limit = birthday_day - 1
        else:
            day_limit = birthday_day
    days_to_roll = day_limit - present_day
    for current_day in range(days_to_roll):
        days_till_next_birthday += 1
    months_passed += 1
    present_month += 1
    day_limit = 0
print(days_till_next_birthday)