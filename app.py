import random
rand_num = random.randrange(1, 5)
num_of_tries = 0

while num_of_tries < 3:
	num_of_tries += 1
	user_guess = int(input("Guess a number between 1 and 5: "))
	if user_guess == rand_num:
		print(f"You won {user_guess}")
		break
	elif num_of_tries >= 3:
		print(f"You lost the number was {rand_num}")
		break
