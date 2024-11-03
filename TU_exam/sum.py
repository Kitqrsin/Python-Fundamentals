command = input().split()
total_numbers = command[0]
total_numbers = int(total_numbers)
inputs = input().split()
while True:
    if total_numbers < 3 or total_numbers > 101:
        break
    max_number = command[1]
    max_number = int(max_number)
    if max_number < 3 or max_number > 300000:
        break
    while True:
        numbers = []
        for n in range(len(inputs)):
            if n > total_numbers:
                break
            else:
                numbers.append(int(inputs[n]))

        first_highest_number = -max_number
        second_highest_number = -max_number
        lowest_number = max_number
        for number1 in numbers:
            if number1 > first_highest_number:
                first_highest_number = number1
        numbers.remove(first_highest_number)

        for number2 in numbers:
            if number2 > second_highest_number:
                second_highest_number = number2

        for number3 in numbers:
            if number3 < lowest_number:
                lowest_number = number3

        print(first_highest_number + second_highest_number + lowest_number)
        command = input().split()
        total_numbers = command[0]
        total_numbers = int(total_numbers)
        if total_numbers < 3 or total_numbers > 101:
            break
        max_number = command[1]
        max_number = int(max_number)
        if max_number < 3 or max_number > 300000:
            break
        inputs = input().split()
