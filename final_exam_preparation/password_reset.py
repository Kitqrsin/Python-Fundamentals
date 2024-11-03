password = input()

while True:
    user_input = input().split()
    user_command = user_input[0]
    if user_command == 'Done':
        break

    if user_command == 'TakeOdd':
        new_password = ''
        for current_letter in range(1, len(password)+1, 2):
            if current_letter > len(password)-1:
                break
            new_password += password[current_letter]
        password = new_password
        print(password)
    elif user_command == 'Cut':
        start_index = int(user_input[1])
        end_index = int(user_input[2]) + start_index
        password = password[:start_index] + '' + password[end_index:]
        print(password)

    elif user_command == 'Substitute':
        substring = user_input[1]
        substitute = user_input[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

print(f'Your password is: {password}')
