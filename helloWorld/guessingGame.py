awnser = 5
print('Enter a number between 1 and 10')
for i in range(0, 4):
  guess = int(input(f'You have {4-i} guesses left: '))
  if guess == 5 or guess == 10:
    print('You guessed correct!')
    break
  else:
    print(f'The guess of {guess} was not correct')
    if guess > awnser:
      print('Your guess was too large')
    elif 4-i == 1:
      print('Youre out of chances :(')
      break
    else:
      print('Your guess was too small')