# Learn how to create function which have multiple other function with return statement

def a():
    print('a-start')
    b() # will call b() function
    d() # will call d() funtion
    print('a-retrun')

def b():
    print('b-start')
    c() # will call c() funtion
    print('b-return') # after b() function called, return to a() function

def c():
    print('c-start')
    print('c-return') # after c() function called, return to b() function

def d():
    print('d-start')
    print('d-return') # after d() function called, return to a() function

a() # call a() function