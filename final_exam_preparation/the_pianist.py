songs_composers_and_keys = {}
times_for_an_action = int(input())

for _ in range(times_for_an_action):
    user_input = input().split("|")
    piece = user_input[0]
    composer = user_input[1]
    key = user_input[2]
    songs_composers_and_keys[piece] = [composer, key]

while True:
    user_input = input()
    if user_input == 'Stop':
        break
    command = user_input.split('|')[0]
    if command == 'Add':
        none, piece, composer, key = user_input.split('|')
        if piece not in songs_composers_and_keys:
            songs_composers_and_keys[piece] = [composer, key]
            print(f'{piece} by {composer} in {key} added to the collection!')
        else:
            print(f"{piece} is already in the collection!")

    elif command == 'Remove':
        none, piece = user_input.split('|')
        if piece not in songs_composers_and_keys:
            print(f'Invalid operation! {piece} does not exist in the collection.')
        else:
            songs_composers_and_keys.pop(piece)
            print(f"Successfully removed {piece}!")

    elif command == 'ChangeKey':
        none, piece, new_key = user_input.split('|')
        if piece not in songs_composers_and_keys:
            print(f'Invalid operation! {piece} does not exist in the collection.')
        else:
            songs_composers_and_keys[piece][1] = new_key
            print(f'Changed the key of {piece} to {new_key}!')

sorted_list = []
for piece, content in songs_composers_and_keys.items():
    composer, key = content
    sorted_list.append(f'{piece} -> Composer: {composer}, Key: {key}')
    sorted(sorted_list)
print("\n".join(sorted_list))

