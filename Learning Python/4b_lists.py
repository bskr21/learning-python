# Learn how list works in Python

# this is how to create list inside variable
spam = ['Arif', 'Brian', 'Chimoy', 'Dedy']
print(spam) # it will shows the lsit
print(len(spam)) # it will shows how many value in the list
print(spam[0:2]) # it will shows the first value [0] and the length of the list [2]
print(spam + ['Ermono', 'Felix', 'Giany']) # it will concatenate the previous list
del spam[2] # it removes the third values [2] in the list
print(spam) # it shows only 3 values from the original list

print('=========================' + '\n' + 'Creating cat names in the lsit')

cat_names = []
while True:
    print('Enter the name of the cat ' + str(len(cat_names)+1) + ' or enter nothing to stop :')
    name = input()
    if name == '':
        break
    cat_names = cat_names + [name]  # to cincatenate the list
print('The cat names are: ')
for name in cat_names:
    print('  ' + name)


