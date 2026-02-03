# Learn how to create a function with return values and return statement

# this program will tell a fortune randomly

import random
import sys

# define a function that return a different string value, depend on the number as argument
def get_answer(number):
        if number == 1:
            return 'It is certain'
        elif number == 2:
            return 'it is decidedly so'
        elif number == 3:
            return 'yes'
        elif number == 4: 
            return 'Try again'
        elif number == 5:
            return 'ask again later'
        elif number == 6:
            return 'concentrate and ask again'
        elif number == 7:
            return 'it is no'
        elif number == 8:
            return 'not so good'
        elif number == 9:
            return 'very doubtful'

while True: 
    print('Ask a yes or no question :')
    question = input('> ')
    if question == 'quit':
        sys.exit()
    else: 
        print('The answer is ' + str(get_answer(random.randint(1, 9))) + '\n')
    
    

