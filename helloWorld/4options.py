
options = ['north', 'south', 'east', 'west']

finish = '4'
dr = ''

print('Chose from one of the options below')
print(f'Press "1" {options[0]}')
print(f'Press "2" {options[1]}')
print(f'Press "3" {options[2]}')
print(f'Press "4" {options[3]}')
print(f'Press "0" exit')
while dr != finish:
  dr = input(f'Chose a direction: ')
  if dr == '0':
    print('You gave up too eaily')
    break
  elif dr != finish:
    print('Wrong direction, try again.')
  else:
    print('You\'re out!')