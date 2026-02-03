# Learn how to create scrolling spike animation

import time, sys

try:
    while True : # main program loopong
        # Draw line with increasing length:
        for i in range(1,9):
            print('-' * (i * i)) # Printing - * 2, - * 4, and so on with max - * 49
            time.sleep(0.1)
        
        # Draw line with decreasing length:
        for i in range(7,1,-1): # Start with - * 49 to draw the bottom half of the spike
            print('-' * (i * i)) 
            time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()