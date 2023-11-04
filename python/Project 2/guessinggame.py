import random
number = random.randint(1, 100)
guess = None

guess = int(input("Guess a number!: "))

while guess != number:
    if guess > number:
        print('Hmm. Too high. Try again!')
        guess = int(input("What's your next guess?: "))
    elif guess < number:
        print('Hmm. Too low. Try again!')
        guess = int(input("What's your next guess?: "))
    else:
        break

print('Nicely done! You guess the number!')