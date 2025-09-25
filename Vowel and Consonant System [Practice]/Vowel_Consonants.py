print("Vowel and Consonant System")
print()

vowels = []
consonants = []
total_vowels = 0
total_consonants = 0

word = input("Enter your word: ")
for letter in word:
    if letter in ['a', 'e', 'i', 'o', 'u']:
        total_vowels += 1
        vowels.append(letter)
    elif letter.isalpha():
        total_consonants += 1
        consonants.append(letter)

print(f"Vowels: {vowels}. Total vowels: {total_vowels}")
print(f"Consonants: {consonants}. Total consonants: {total_consonants}")

