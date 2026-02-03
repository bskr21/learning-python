# Learn how to build a simple number guessing game with all flow control's function

import random
secret_number = random.randint (1, 20)
print('I am thinking of a number between 1 an 20')
print('Can you guess it?')

for guesses_taken in range (1, 7):
    guess = int(input('> '))
    if guess > secret_number:
        print('Oops, your number is too high')
    elif guess < secret_number:
        print ('Uh oh! your number is too low')
    else:
        break # to exit the loop after player guess the correct number

if guess == secret_number:
    print ('You got it! you only need ' + str(guesses_taken) + ' to guess it!')
else :
    print ('Sorry, you already guess ' + str(guesses_taken) + ' times, the number is ' + str(secret_number) + ' Hope you are lucky next time 😁')
