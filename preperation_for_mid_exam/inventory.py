def collect(something, a_list):
    if something in a_list:
        return
    return a_list.append(something)


def drop(something, a_list):
    if something in a_list:
        return a_list.remove(something)
    return


def combine(a_list, new_item):
    index_of_new_item = new_item.split(':')
    if index_of_new_item[0] in a_list:
        the_index = a_list.index(index_of_new_item[0]) + 1
        return a_list.insert(the_index, index_of_new_item[1])
    return


def renew(something, a_list):
    if something in a_list:
        a_list.remove(something)
        return a_list.insert(len(a_list), something)
    return


given_items = input().split(', ')
user_input = input().split(' - ')
while user_input[0] != 'Craft!':
    if user_input[0] == 'Collect':
        collect(user_input[1], given_items)
    elif user_input[0] == 'Drop':
        drop(user_input[1], given_items)
    elif user_input[0] == 'Combine Items':
        combine(given_items, user_input[1])
    elif user_input[0] == 'Renew':
        renew(user_input[1], given_items)
    user_input = input().split(' - ')
print(', '.join(given_items))