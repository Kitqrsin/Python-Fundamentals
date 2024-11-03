concealed_message = input()
while True:
    user_command = input().split(':|:')
    command = user_command[0]
    if command == 'Reveal':
        break
    if command == 'InsertSpace':
        index_of_space = int(user_command[1])
        concealed_message = concealed_message[:index_of_space] + ' ' + concealed_message[index_of_space:]
        print(''.join(concealed_message))
    elif command == 'Reverse':
        string_to_reverse = user_command[1]
        if string_to_reverse in concealed_message:
            concealed_message = concealed_message.replace(string_to_reverse, '', 1)
            concealed_message = concealed_message + string_to_reverse[::-1]
            print(concealed_message)
        else:
            print('error')

    elif command == 'ChangeAll':
        string_to_replace = user_command[1]
        replacement = user_command[2]
        concealed_message = concealed_message.replace(string_to_replace, replacement)
        print(concealed_message)
print(f'You have a new text message: {concealed_message}')
