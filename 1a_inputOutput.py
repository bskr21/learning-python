# this program says hello and will determine your age

print('Hello, World')
print('What is your name') # ask for ther name
my_name = input('masukin namamu : ')
print('it is good to meet you, ' + my_name)
print('The lenght of your name is:')
print(len(my_name))
print('what year was your born?') # ask for their year of birth
my_age = input ('coba isi tahun lahir : ')
print('Wow, now You are ' + str(2026 - int(my_age)) + ' this year') # it transform my_age into int and after that transform in again into str
