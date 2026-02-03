# Let's learn about how continue and break statement works

while True:
    print('Who Are You?')
    name = input('> ')
    if name != 'Joe':
        continue 
    # if the inputed name is True, the 'continue' statement is active
    # and it start looping from 'while' statement again
    # if the inputed name is False, the 'continue' statement is skipped to the next command 
    print('Hi, Joe. Please input your password')
    password = input('> ')
    if password == "swordfish":
        break
    # if the inputed password is True, the 'break' statement is active
    # and it stop the looping
    # if the inputed passsword is False, the loop for the block code is active and start from the 'while' statement again   
print('access granted, welcome Joe!')

