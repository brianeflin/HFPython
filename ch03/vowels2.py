vowels = ['a', 'e', 'i', 'o', 'u']
vowels_found = {}
word = input("Input a word for a vowel search: ")
for letter in word:
    if letter in vowels:
        if letter not in vowels_found:
            vowels_found[letter] = 0
        vowels_found[letter] += 1
for k, v in sorted(vowels_found.items()):
    print(k, ':', v)
