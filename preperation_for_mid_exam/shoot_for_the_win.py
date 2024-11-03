def shots(some_targets):
    shot_targets = []
    user_input = input()
    while user_input != 'End':
        index_shot = int(user_input)
        if index_shot in shot_targets:
            user_input = input()
            continue
        if index_shot > total_targets:
            user_input = input()
            continue
        shot_targets.append(index_shot)
        balancer = some_targets[index_shot]
        some_targets[index_shot] = -1
        for i in range(len(some_targets)):
            if some_targets[i] == -1:
                continue
            if some_targets[i] > balancer:
                some_targets[i] -= balancer
            else:
                some_targets[i] += balancer
        user_input = input()
    total_shots = 0
    for shots in range(len(shot_targets)):
        total_shots += 1
    str_list = [str(x) for x in some_targets]
    return f"Shot targets: {total_shots} -> {' '.join(str_list)}"


targets = input().split()
targets_as_int = []
total_targets = -1
for index in range(len(targets)):
    current_number = int(targets[index])
    total_targets += 1
    targets_as_int.append(current_number)
print(shots(targets_as_int))