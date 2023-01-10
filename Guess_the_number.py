
# This is a Guess the Number game.
import random

new_request = True

while new_request:

	guessesTaken = 0

	print('Hello! What is your name?')
	myName = input()

	number = random.randint(1, 30)
	print('Well, ' + myName + ', I am thinking of a number between 1 and 30.')

	for guessesTaken in range(6):
		print('Take a guess.') # Four spaces in front of "print"
		guess = input()
		guess = int(guess)

		if guess < number:
			print('Your guess is too low.') # Eight spaces in front of "print"

		if guess > number:
			print('Your guess is too high.')

		if guess == number:
			break

	if guess == number:
		guessesTaken = str(guessesTaken + 1)
		print('Good job, ' + myName + '! You guessed my number in ' +
		guessesTaken + ' guesses!')

	if guess != number:
		number = str(number)
		print('Nope. The number I was thinking of was ' + number + '.')

	user_response = input("Do you want to perform another operation?(yes or no)")

	if user_response == 'no':
		print("thank you for playing with me")
		new_request = False
