# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
dog = int(input('enter your dogs age: '))
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
if(dog>0): 
    if dog<3:
        h=dog*10
        print(f"The dogs age in dog years is {h}")
    elif dog>2:
        h=(dog/dog)*20+(dog-2)*7
        print(f"The dogs age in dog years is {h}")
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer