import re
user_input = input()
pattern = r'(=|\/)[A-Z][a-zA-Z]{2,}\1'
fixed_result = re.finditer(pattern, user_input)
points = 0
all_destinations = []


for destination in fixed_result:
    current_destination = re.split('\/|=', destination.group())[1]
    all_destinations.append(current_destination)
    points += len(current_destination)

print(f'Destinations: {", ".join(all_destinations)}')
print(f'Travel Points: {points}')