def add(phone, given_list_of_phones):
    if phone in list_of_phones:
        return
    return given_list_of_phones.append(phone)


def remove(phone, given_list_of_phones):
    if phone in given_list_of_phones:
        return given_list_of_phones.remove(phone)
    return


def bonus_phone(phone, given_list_of_phones):
    phone = phone.split(':')
    old_phone = phone[0]
    new_phone = phone[1]
    if old_phone in given_list_of_phones:
        index = int(given_list_of_phones.index(old_phone))
        return given_list_of_phones.insert(index + 1, new_phone)
    return


def last(phone, given_list_of_phones):
    if phone in given_list_of_phones:
        index = len(given_list_of_phones)
        given_list_of_phones.remove(phone)
        given_list_of_phones.insert(index, phone)



list_of_phones = input().split(', ')

user_input = input().split(' - ')
while user_input[0] != 'End':
    command = user_input[0]
    current_phone = user_input[1]
    if command == 'Add':
        add(current_phone, list_of_phones)
    elif command == 'Remove':
        remove(current_phone, list_of_phones)
    elif command == 'Bonus phone':
        bonus_phone(current_phone, list_of_phones)
    elif command == 'Last':
        last(current_phone, list_of_phones)
    user_input = input().split(' - ')
print(', '.join(list_of_phones))