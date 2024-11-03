import re

number_of_bosses = int(input())

bosses_so_far = 0
pattern = r'((\|)[A-Z]{4,}(\|)):(#[A-Za-z]+\s+[A-Za-z]+#)'
while bosses_so_far != number_of_bosses:
    bosses_so_far += 1
    boss_string = input()
    boss_data = re.findall(pattern, boss_string)
    if len(boss_data) < 1:
        print('Access denied!')
        continue
    boss_data_tuple = boss_data[0]
    name_of_boss = boss_data_tuple[0]
    name_of_boss = name_of_boss.replace("|", "")
    boss_title = boss_data_tuple[-1]
    boss_armor = 0
    boss_title_in_string = ''
    for current_char in boss_title:
        if current_char.isalnum() or current_char == ' ':
            boss_title_in_string += f'{current_char}'
            boss_armor += 1
    print(f'{name_of_boss}, The {boss_title_in_string}')
    print(f'>> Strength: {len(name_of_boss)}'
          f'\n>> Armor: {boss_armor}')
