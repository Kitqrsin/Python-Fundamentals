parking_lot = {}
number_of_commands = int(input())

for n in range(number_of_commands):
    command = input().split()
    name = command[1]
    if command[0] == 'register':
        code = command[2]
        if name in parking_lot:
            print(f"ERROR: already registered with plate number {code}")
            continue
        else:
            print(f'{name} registered {code} successfully')
            parking_lot[name] = code
    elif command[0] == 'unregister':
        if name not in parking_lot:
            print(f"ERROR: user {name} not found")
        else:
            parking_lot.pop(name)
            print(f'{name} unregistered successfully')

for name, code in parking_lot.items():
    print(f'{name} => {code}')