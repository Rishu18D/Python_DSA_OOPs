user_input = input("Enter your sentence: ")

count_A = 0
count_a = 0
count_C = 0

for letter in user_input:
    if letter.isupper():
        count_A += 1
    elif letter.islower():
        count_a += 1
    elif letter.isdigit():
        count_C += 1

print("Number of uppercase characters:", count_A)
print("Number of lowercase characters:", count_a)
print("Number of digits:", count_C)
