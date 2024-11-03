food = float(input())
hay = float(input())
cover = float(input())
pig_weight = float(input())
food *= 1000
hay *= 1000
cover *= 1000
pig_weight *= 1000
month_has_passed = True

for day in range(1, 30 + 1):
    food -= 300
    if day % 2 == 0:
        hay -= food * 0.05
    if day % 3 == 0:
        cover -= pig_weight/3
    if food <= 0 or hay <= 0 or cover <= 0:
        print('Merry must go to the pet store!')
        month_has_passed = False
        break

if month_has_passed:
    food /= 1000
    hay /= 1000
    cover /= 1000
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
