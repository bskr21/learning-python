# This is where I learn about Flow Control.
# It said that it can decide which Python instruction to execute under which condition

# Comparison Operators evaluates into Boolean Values
5 == 5 # Equal to
5 != 4 # Not Equal to
4 < 5 # Less than
7 > 6 # Greater than
4 <= 5 # Less than or equal to
7 >= 6 # Greater than or equal to
# All this command will evaluates into Boolean values 'True'

# Boolean Operators will also evaluates expression into Boolean Values
True and False # Evaluates into False (not both True)
True or False # Evaluates into True (one of the expression is True)
not True # Evaluates into False (oppsote of the expression)

trial1 = (4 < 5) and (5 < 6) # Should be evaluated into True

trial2 = (4 < 5 ) and (9 < 6) # Should be evaluated into False

Trial3 = (1 == 2) or (2 == 2) # Should be evaluated into True

spam = 4
Trial4 = 2 + 2 == spam and not 2 + 2 == (spam + 1) and 2 * 2 == 2 + 2
# Should be evaluated into True


# Let's try to use some basic flow control statement with code blocks
username = input('input username : ')
if username == 'Mary':
    print('Hello, Mary')
else:
     print('Wow, you are not Mary, please input correct username')
password = input('input password : ')
if password == 'swordfish':
     print('Acces Granted, welcome Mary')
else:
     print('Sorry, you are not Mary')


# Trying if and elif  statement
name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice')
elif age < 12:
    print('You are not Alice Kiddo')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire')
elif age > 100 :
    print('You are not Alice, grannie')
# the result shuold be 'Unlike you, Alice is not an undead, immortal vampire'