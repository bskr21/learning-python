# Learning how to use all the Boolean values into one program called Opposite Day

today_is_opposite_day = False
# If it's True, the final output should be "Today is not opposite day"
# If it's False, the final output should be "Today is opposite day"

# First command : Set say_it_is_opposite_day based on today_is_opposite_day
if today_is_opposite_day == True:
    say_it_is_opposite_day = True
else :
    say_it_is_opposite_day = False

# Second command : If it is opposite day, toggle say_it_is_opposite_day 
if today_is_opposite_day == True :
    say_it_is_opposite_day = not say_it_is_opposite_day
else: # if this statement removed, the program will give outputs "Today is not opposite day", no matter True or False the today_is_opposite_day variable "
    say_it_is_opposite_day = not say_it_is_opposite_day

# Final command : Say what day it is
if say_it_is_opposite_day == True:
    print('Today is opposite day')
else:
    print('Today is not opposite day')