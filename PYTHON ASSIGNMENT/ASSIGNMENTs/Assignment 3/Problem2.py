# 2 Write a program to input any alphabet and check whether it is a vowel or
# consonant.
char = input("Enter an alphabet:")
if char in 'aeiouAEIOU':
    print("The alphabet is a vowel.")
else:
    print("The alphabet is a consonant.")
