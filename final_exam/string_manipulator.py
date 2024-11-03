string = input()

while True:
    user_input = input().split()
    user_command = user_input[0]
    if user_command == 'End':
        break

    if user_command == 'Translate':
        char = user_input[1]
        replacement = user_input[2]
        if char in string:
            string = string.replace(char, replacement)
            print(string)
        else:
            print(string)

    elif user_command == 'Includes':
        substring = user_input[1]
        if substring in string:
            print(True)
        else:
            print(False)

    elif user_command == 'Start':
        substring = user_input[1]
        if string.startswith(substring):
            print(True)
        else:
            print(False)

    elif user_command == 'Lowercase':
        string = string.lower()
        print(string)

    elif user_command == 'FindIndex':
        char = user_input[1]
        print(string.rfind(char))

    elif user_command == 'Remove':
        start_index = int(user_input[1])
        end_index = int(user_input[2]) + start_index
        string = string[:start_index] + '' + string[end_index:]
        print(string)
