import re
user_input = input()
pattern = r'(@|#)([a-zA-Z]{3,})(\1{2,})([a-zA-Z]{3,})\1'
fixed_result = re.findall(pattern, user_input)
mirror_words = []
the_count_of_words = 0

for pair in fixed_result:
    if pair[1] == pair[3][::-1]:
        mirror_words.append(f'{pair[1]} <=> {pair[3]}')
    the_count_of_words += 1

if the_count_of_words > 0:
    print(f'{the_count_of_words} word pairs found!')
    if len(mirror_words) > 0:
        print('The mirror words are:')
        print(', '.join(mirror_words))
    else:
        print('No mirror words!')
else:
    print('No word pairs found!'
          '\nNo mirror words!')
