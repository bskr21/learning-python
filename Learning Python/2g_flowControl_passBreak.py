# Learn how to pass and break the flow based on the the certain condition

names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']

# Pass the command
for name in names:
    if 'j' in name.lower(): 
        pass # this will skip all names contain 'j' in it
    else:
        print(name)


# Break the command
for name in names:
    if 'h' in name.lower():
        break # the loop stops iterating and breaks after met the condition.
    else:
        print(name)