# Learning how to use all the Boolean values into one short program called Dishonest Capacity

print('Enter TB or GB for the advertised unit:')
unit = input('> ')

# Calcilate the amount that the advertised capacity lies
if unit == 'TB' or unit == 'tb':
    discrepancy = 1000000000000 / 1099511627776
elif unit == 'GB' or unit == 'gb':
    discrepancy = 1000000000 / 1073741824

print('Enter the advirtised capcaity:')
advertised_capacity = input('> ')
advertised_capacity = float(advertised_capacity)

# Calculate the real capacity, round it to the nearest hundredths,
# and convert it to a string so it can be concatenated
real_capacity = str(round(advertised_capacity * discrepancy, 2))

print('The real capcaity is ' + real_capacity + ' ' + unit)