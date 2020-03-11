letters = 'all the things i do'

guess = input('Guess a letter: ')


# use 'casefold()' when comparing strings. 
# No 'toUpper()' or 'toLower()'
if guess not in letters.casefold():
  print('dont need that letter')
else:
  print('Yes, we needed that letter') 
