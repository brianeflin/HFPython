vowels = {'a', 'e', 'i', 'o', 'u'}
#vowels_found = {}
word = input("Input a word for a vowel search: ")
vowels_found = vowels.intersection(set(word))
for vowel in sorted(vowels_found):
    print(vowel)
