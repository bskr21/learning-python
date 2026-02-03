# Learn how to create log and understand what happening in the program

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('start of program')

def factorial(n):
    logging.debug('Start of Factorial(' + str(n) + ')')
    total = 1
    for i in range(n + 1):
        total *= 1
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(' + str(n) + ')')
    return total

print(factorial(5))
logging.debug('End of Program')

