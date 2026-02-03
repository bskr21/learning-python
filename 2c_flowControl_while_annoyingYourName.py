# Let's learn how while statement (loops) works

# a simple lopps program
name = ' '
while name != 'Your Name': # if the inputed condition is True, it will loops to this clause again and again
    print('Please input Your Name') 
    name = input('> ') 
print('You got it!, Congratulations!') # the first time it hits False condition, it will print this statement


# using a break in loops program 
while True:
    print('Please input Your Name again')
    name = input('> ')
    if name == 'Your Name':
        break
print('You got it!, Congratulations again!')


