
# adding spaces with formatting keyword
for i in range(0, 5):
  print('Number of {0:<4} times the code loops {0:5} \n testing {0:^10} things'.format(i+1))

print()
tint = 'car tints'
for i in range(0, 5):
  print(f'Number of {tint} times the code loops {tint}')

 # python2 interpolation
age = 21
cost = 3.5
month = 'Jan'
print('My age is %d years' % age)
print('it costs %f' % cost)
print('it is %s right now' % month)

# adding persision to floats
print()
print('My age is %d years. \nit costs %.3f \nit is %s right now' % (age, cost, month))

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print('testing',data[::5])


# how if's work in python
name = (str(input('What is your name?: ')))
age = (int(input('What is your age?: ')))
print(f'Your name is {name} and you\'re {age}')
pie = str(input('Would you like some pie???: '))
if 'y' in pie:
  print('HERES SOME PIE FOR YOU!')
elif 'n' in pie:
  print('MORE FOR ME!')
else:
  print('or dont awnser to questing')