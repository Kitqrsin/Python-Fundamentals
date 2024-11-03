legendary_items = {"shards": 0, 'fragments': 0, 'motes': 0}

current_material = input().split()
obtained_item = False
while not obtained_item:
    for index in range(0, len(current_material), 2):
        value = int(current_material[index])
        key = current_material[index+1].lower()
        if key not in legendary_items.keys():
            legendary_items[key] = 0
        legendary_items[key] += value
        if legendary_items['shards'] >= 250:
            print('Shadowmourne obtained!')
            legendary_items['shards'] -= 250
            obtained_item = True
        elif legendary_items['fragments'] >= 250:
            print('Valanyr obtained!')
            legendary_items['fragments'] -= 250
            obtained_item = True
        elif legendary_items['motes'] >= 250:
            print('Dragonwrath obtained!')
            legendary_items['motes'] -= 250
            obtained_item = True
        if obtained_item:
            break
    if obtained_item:
        break
    current_material = input().split()

for material, quantity in legendary_items.items():
    print(f'{material}: {quantity}')

