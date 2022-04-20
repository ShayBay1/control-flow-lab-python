# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
number = 0
term = 0 
state = 1
while term < 51:
    if term < 2:
        print(f"term: {term} / number {term}")
    else:
        next = number + state
        print(f"term: {term} / number {next}")
        number = state 
        state = next 
    term += 1
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it
