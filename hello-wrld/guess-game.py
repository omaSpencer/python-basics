secret_number = 7
max_guess = 3
guess_count = 0
while guess_count < max_guess:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('Sorry you failed!')
