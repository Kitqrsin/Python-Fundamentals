import math


def percentage(value, some_numbers):
    percentage_value = (some_numbers/value) * 100
    return percentage_value


biscuit_per_day = int(input())
number_of_workers = int(input())
competing_factory_production = int(input())

third_day_value = biscuit_per_day * .75

count_of_biscuits = 0
for day in range(1, 31):
    if day % 3 == 0:
        third_day_biscuit = number_of_workers * third_day_value
        third_day_biscuit = math.floor(third_day_biscuit)
        count_of_biscuits += third_day_biscuit
        continue
    count_of_biscuits += number_of_workers * biscuit_per_day
print(f"You have produced {int(count_of_biscuits)} biscuits for the past month.")

difference = count_of_biscuits - competing_factory_production
difference = abs(difference)
percentage_value = percentage(competing_factory_production, difference)

if count_of_biscuits > competing_factory_production:
    print(f"You produce {percentage_value:.2f} percent more biscuits.")
elif competing_factory_production > count_of_biscuits:
    print(f"You produce {percentage_value:.2f} percent less biscuits.")
