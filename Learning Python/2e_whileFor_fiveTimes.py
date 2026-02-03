# Let's learn how to execute loop only in a ceratin number of times

print('Hello')
for i in range(1,6): 
    # i stand for variable that will change into counts
    # (1,6) means counting start from 1 and stop counting before 6
    print('I eat ' + str(i) + ' candy' ) # becasue i is int, need change into str to combine with the sentence
print('Goodbye')


# let's try another one, counting 1 + 2 + 3 + .... + 100
total = 0
for num in range(5):
    print(total + num)
    total = total + num

# Equivalent fiveTimes with while loop
print('Hello')
i = 1
while i < 5:
    print('I eat ' + str(i) + ' candy')
    i = i + 1
print('Goodbye!')