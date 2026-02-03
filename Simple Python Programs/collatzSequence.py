# Learn how to create Collatz Sequence
# Check how every integer will return at 1 at the end with Collatz formula

def collatz(number):
    # to detect the number is even or not with remainder
    # if the remainder == 0, the number is even
    if number % 2 == 0:  
        result = (number // 2)
    else :
        result = (3 * number + 1)
    print(result, end = ' ') # use end = ' ' to prints on the same line with one space
    return result 

# This is the main program

while True: 
    print('Input number: ')

    try:
        inputed_number = int(input('> ')) # transform inputted value into integer
        print(inputed_number, end = ' ') # print inputted number again on the same line with the result

        # Main looping
        while inputed_number != 1:
            inputed_number = collatz(inputed_number)

    except ValueError :
             print('Please input number again') # Using Try and Except statement to cover non integer input
    print('\n')





       


        


