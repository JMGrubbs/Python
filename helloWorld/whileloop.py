import random

answer = random.randint(1,10)
guess = None
print('Guess a number between 1 and 10 to win')
print()
count = 4

while count > 0:
  count = count - 1
  guess = int(input('guess a number: '))
  if guess > answer:
    print('guess too high')
  elif guess < answer:
    print('Guess too low')
  
  if guess == answer:
    print('You guessed correct!')
    break
  elif count == 0:
    print('You are out of guesses :(')
    print(f'The answer was {answer}')
  else:
    print(f'You have {count} guesses left')