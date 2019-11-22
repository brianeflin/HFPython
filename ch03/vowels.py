vowels = ['a', 'e', 'i', 'o', 'u']
vowels_found = []
word = input("Input a word for a vowel search: ")
for letter in word:
    if letter in vowels and letter not in vowels_found:
        vowels_found.append(letter)
for vowel in vowels_found:
    print(vowel)
