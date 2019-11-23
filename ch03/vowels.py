vowels = ['a', 'e', 'i', 'o', 'u']
vowels_found = {}
for vowel in vowels:
    vowels_found[vowel] = 0
# print(vowels_found)
word = input("Input a word for a vowel search: ")
for letter in word:
    if letter in vowels:
        vowels_found[letter] += 1
for k, v in sorted(vowels_found.items()):
    print(k, ':', v)
