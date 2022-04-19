# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 

word = input('please enter a word or phrase: ').upper()
if word != "quit":
    while not word.isalpha():
        print(f"{word} is not a word/phrase")
        word = input('please enter a word or phrase: ').upper()
    while word != "quit":
        word.isalpha()
        print(f'that word/phrase is {len(word)} charecters long')
        word = input('please enter a word or phrase: ').upper()
else:
    print('goodbye')
     

# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

