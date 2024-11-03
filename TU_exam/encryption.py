word_for_encryption = list(input())
number = int(input())

for index in range(number):
    char = number - index
    character_index = len(word_for_encryption) - char
    character = word_for_encryption[character_index]
    word_for_encryption.pop(character_index)
    word_for_encryption.insert(0 + index, character)
character_index = []
for c in word_for_encryption:
    character_index.append(chr(ord(c) + number))
print(''.join(character_index))
