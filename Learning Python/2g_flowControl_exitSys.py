# Learn how to terminate the program with sys.exit() function

import sys #sys.exit is in the sys module, so we need to import sys module first

while True:
    print('Type exit to exit')
    response = input('> ')
    if response == 'exit':  
        sys.exit() # if true, this line will be executed and the program will exit
    print('You type ' + response + '.')