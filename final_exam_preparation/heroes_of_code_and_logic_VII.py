number_of_heroes = int(input())
heroes = {}

for current_hero in range(number_of_heroes):
    hero_name, hp, mp = input().split()
    hp = int(hp)
    mp = int(mp)
    if hp > 100 or mp > 200:
        pass
    else:
        heroes[hero_name] = [hp, mp]

while True:
    user_command = input().split(' - ')
    current_command = user_command[0]
    if current_command == 'End':
        break

    if current_command == 'CastSpell':
        selected_hero = user_command[1]
        mp_needed = int(user_command[2])
        spell_name = user_command[3]
        hero_data = heroes[selected_hero]
        current_mp = int(hero_data[1])
        if current_mp >= mp_needed:
            current_mp -= mp_needed
            hero_data[1] = current_mp
            heroes[selected_hero] = hero_data
            print(f"{selected_hero} has successfully cast {spell_name} and now has {current_mp} MP!")
        else:
            print(f"{selected_hero} does not have enough MP to cast {spell_name}!")

    elif current_command == 'TakeDamage':
        selected_hero = user_command[1]
        damage = int(user_command[2])
        attacker = user_command[3]
        hero_data = heroes[selected_hero]
        current_hp = int(hero_data[0])
        if current_hp > damage:
            current_hp -= damage
            hero_data[0] = current_hp
            heroes[selected_hero] = hero_data
            print(f"{selected_hero} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
        else:
            del heroes[selected_hero]
            print(f'{selected_hero} has been killed by {attacker}!')

    elif current_command == 'Recharge':
        selected_hero = user_command[1]
        amount = int(user_command[2])
        hero_data = heroes[selected_hero]
        current_mp = int(hero_data[1])
        current_mp += amount
        if current_mp > 200:
            subtraction = current_mp - 200
            amount -= subtraction
            current_mp = 200
        hero_data[1] = current_mp
        heroes[selected_hero] = hero_data
        print(f"{selected_hero} recharged for {amount} MP!")

    elif current_command == 'Heal':
        selected_hero = user_command[1]
        amount = int(user_command[2])
        hero_data = heroes[selected_hero]
        current_hp = int(hero_data[0])
        current_hp += amount
        if current_hp > 100:
            subtraction = current_hp - 100
            amount -= subtraction
            current_hp = 100
        hero_data[0] = current_hp
        heroes[selected_hero] = hero_data
        print(f"{selected_hero} healed for {amount} HP!")

for hero, hero_data in heroes.items():
    hero_hp = int(hero_data[0])
    hero_mp = int(hero_data[1])
    print(f'{hero}'
          f'\n  HP: {hero_hp}'
          f'\n  MP: {hero_mp}')
