# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 

word = input('please enter a word or phrase: ').lower()

if word != ('quit').lower():
    while not word.isalpha():
        print(f"{word}, <--- word var in block2")
        word = input('please enter a word or phrase: ').lower()
        print(f"{word} is not a word/phrase")
    while word != ("quit").lower():
        word.isalpha()
        print(f'that word/phrase is {len(word)} charecters long')
        word = input('please enter a word or phrase: ').lower()
        print("goodbye")
elif word == ('quit').lower():
    print("goodbye")
     

# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

