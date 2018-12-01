# Continue write game.
import random 
print('Hello. Welcome to the game.')


def randomNumber():
	changeNumber = random.randint(1, 30)
	return changeNumber


def main():
	random_number = randomNumber()
	wrong = 4
	while wrong > 0:
		try:
			user = int(input('Enter a number. (You have {}-attempts): '.format(wrong)))
			if isinstance(user, int):
				if random_number == user:
					print('Congratulation! You won...')
					break
				elif random_number < user:
					print('System the number: LESS')
					wrong -= 1
				elif random_number > user:
					print('System the number: MORE')
					wrong -= 1
				continue
		except ValueError as e:
			print('''Hey, you enter not number, friend :D

		------->> Try again <<-------'''
		'\n')
	else:
		print('You have has zero attempts. The numbers was is ', random_number)


main() 