year = int(input())
year_found = False
while not year_found:
    year += 1
    set_year = set()
    for i in range(len(str(year))):
        set_year.add(str(year)[i])

    year_found = len(set_year) == len(str(year))

print(year)