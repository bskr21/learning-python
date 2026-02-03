# Learn how to create a basic function
# It is good for duplicating code, it is like grouping a bunch of code

def hello(): # def for define the function
    print('Good Morning')
    print('Good afternoon')
    print('Good Evening')

# call (testing) the function
hello()
hello()
print('ONE MOMRE TIME')
hello()

# Learn create a function with arguments
def hello_with_name(name): # define the fucntion with added 'name' as parameters
    print('Good Morning ' + name)
    print('Good afternoon' + name)
    print('Good Evening' + name)

# call (testing) the function
hello_with_name('Akbar') # the function should be called with the argument to fill the parameters like 'Akbar'
hello_with_name('Bintoro')
hello_with_name() # this line will error becouse the arguments is missing
