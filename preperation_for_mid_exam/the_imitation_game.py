first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students_count = int(input())

sum_of_total_efficiency = first_employee + second_employee + third_employee

hours_needed = 0

while students_count > 0:
    hours_needed += 1
    if hours_needed % 4 == 0:
        continue
    else:
        students_count -= sum_of_total_efficiency

print(f'Time needed: {hours_needed}h.')
