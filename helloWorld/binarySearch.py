low = 1
high = 1000

print('think of a number between 1 and 1000')
input('Press ENTER to start')
count = 0
# guess = high//2
while low != high:
  count = count + 1
  guess = low + (high - low) // 2
  high_low = input(f'My guess is {guess}. Should i guess higher or lower? '
                    'Enter h for higher, l for lower and c for correct: ')
  if high_low == 'h':
    # guess = guess // 2
    low = guess + 1
  elif high_low == 'l':
    # guess = guess + (guess // 2)
    high = guess - 1
  elif high_low == 'c':
    print(f'I got it in {count} guesses')
  else:
    print('Enter h, l or c')
    break 
 