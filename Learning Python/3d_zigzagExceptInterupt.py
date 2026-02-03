# Learn how to create a small animation with time module and Except Interupt

import time, sys
indent = 0 # First variable, how many spaces to indent
indentIncreasing = True # Second variable, used to change the direction

try:
    while True: # the main loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Puase for 1/10th of a second

        if indentIncreasing:
            indent = indent + 1 # increasing the number of spaces
            if indent == 20: # changing the direction after indent reaches this number
                indentIncreasing = False
        
        else:
            indent = indent - 1 # decreasing the number of spaces
            if indent == 0: #changing the direction after indent reaches this number
                indentIncreasing = True
    
except KeyboardInterrupt: # This try-except statement used to handling clean keyboard interupt error message
    sys.exit() 


