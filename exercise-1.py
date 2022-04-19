# exercise-01 Vowel or Consonant
# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# user needs to input a letter:

# letter = input('Enter a letter :').upper()
letter = input("please enter a letter: ").upper()

while not letter.isalpha():
    print(f"{letter} is not a letter")
    letter = input("please input valid letter: ").upper()

else: 
    letter.isalpha()
    if letter in "AEIOU":
        print(f"{letter} is a vowel")
    elif letter == "Y":
        print(f'the letter {letter} is sometime a vowel')
    else:
        print(f"{letter} is a Consonant")
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':