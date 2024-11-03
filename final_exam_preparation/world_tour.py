all_tour_stops = list(input())


def add_stop(index, string, tour_list):
    if index > len(tour_list):
        return tour_list
    for letter in string:
        tour_list.insert(index, letter)
        index += 1
    return tour_list


def remove_stop(start_index, end_index, tour_list):
    cloned_tour_list = tour_list.copy()
    if start_index > len(tour_list) or end_index > len(tour_list):
        return tour_list
    del tour_list[start_index:end_index+1]
    return tour_list


def switch_stops(old_string, new_string, tour_list):
    list_as_str = ''.join(tour_list)
    if old_string in list_as_str:
        list_as_str = list_as_str.replace(old_string, new_string)
        tour_list = [*list_as_str]
        return tour_list
    return tour_list


while True:
    user_input = input().split(':')

    command = user_input[0]
    if command == 'Travel':
        break

    if command == 'Add Stop':
        index = int(user_input[1])
        string = user_input[2]
        all_tour_stops = add_stop(index, string, all_tour_stops)
        print(''.join(all_tour_stops))

    elif command == 'Remove Stop':
        start_index = int(user_input[1])
        end_index = int(user_input[2])
        all_tour_stops = remove_stop(start_index, end_index, all_tour_stops)
        print(''.join(all_tour_stops))

    elif command == 'Switch':
        old_string = user_input[1]
        new_string = user_input[2]
        all_tour_stops = switch_stops(old_string, new_string, all_tour_stops)
        print(''.join(all_tour_stops))
tour = ''.join(all_tour_stops)
print(f"Ready for world tour! Planned stops: {tour}")
