#program that counts number of vowels and consonents in a word.
user_input = input("Enter a word: ")
vowels = "AEIOUaeiou"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

vowel_count = 0
consonant_count = 0

for letter in user_input:
    if letter in vowels:
        vowel_count += 1
    elif letter in consonants:
        consonant_count += 1

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)

        

