print('to go on this trip you must be older than')
print('18 but under 31 and provide your name')

name = input('Type name here: ')
age = int(input('Type age here: '))

if 18 <=  age < 31:
  print(f'Well go get ready {name}, were leaving in an hour!')
else:
  print(f'Sorry {name} you cant come this time.')