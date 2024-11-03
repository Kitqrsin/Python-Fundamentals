given_numbers = input().split()
removed_numbers = int(input())
given_numbers_integer = []
for number in range(0, len(given_numbers)):
    given_numbers_integer.append(int(given_numbers[number]))


while removed_numbers != 0:
    smallest_number = min(given_numbers_integer)
    given_numbers_integer.remove(smallest_number)
    removed_numbers -= 1
print(', '.join(map(str, given_numbers_integer)))

