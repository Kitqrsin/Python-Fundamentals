route = input().split('||')
# first element command, second int
fuel_tank = int(input())
ammunition = int(input())
mission_is_failed = False


def traveling(distance):
    global mission_is_failed
    global fuel_tank
    event_fuel = fuel_tank
    event_fuel -= distance
    # IMPORTANT
    if event_fuel >= 0:
        print(f"The spaceship travelled {distance} light-years.")
        fuel_tank = event_fuel
    else:
        mission_is_failed = True
        print("Mission failed.")


def enemy(enemy_armor):
    global mission_is_failed
    global ammunition
    global fuel_tank
    event_amunition = ammunition
    event_fuel = fuel_tank
    if event_amunition >= enemy_armor:
        event_amunition -= enemy_armor
        ammunition = event_amunition
        print(f"An enemy with {enemy_armor} armour is defeated.")
    else:
        event_fuel -= enemy_armor * 2
        if event_fuel >= 0:
            fuel_tank = event_fuel
            print(f"An enemy with {enemy_armor} armour is outmaneuvered.")
        else:
            mission_is_failed = True
            print("Mission failed.")


def repear(repair_value):
    global ammunition
    global fuel_tank
    event_fuel = fuel_tank
    event_ammunition = ammunition
    event_fuel += repair_value
    event_amunition = repair_value*2
    print(f"Ammunitions added: {repair_value*2}.")
    print(f"Fuel added: {repair_value}.")
    fuel_tank = event_fuel
    ammunition = event_ammunition


for index in range(len(route)):
    if mission_is_failed:
        break
    current_event = route[index].split(' ')

    event = current_event[0]
    if event == 'Titan':
        print("You have reached Titan, all passengers are safe.")
        break
    event_value = int(current_event[1])
    if event == 'Travel':
        traveling(event_value)
    elif event == 'Enemy':
        enemy(event_value)
    elif event == 'Repair':
        repear(event_value)
