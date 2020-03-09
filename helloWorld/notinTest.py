letters = 'all the things i do'

guess = input('Guess a letter: ')

if guess not in letters:
  print('dont need that letter')
else:
  print('Yes, we needed that letter')