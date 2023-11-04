import random
number = random.randint(1, 10000)

player_name = input("Hello, who are you?: ")
guesses_left = 0
print('Welcome '+ player_name+ '. I am thinking of a number between 1 and 10,000. You have 100 guesses. Can you perservere and guess the number? What is your first guess?: ')

while guesses_left < 100:
    guess = int(input())
    guesses_left += 1
    if guess < number:
        print('Nope, the number is higher.')
    if guess > number:
        print('Not quite, the number is lower.')
    if guess == number:
        break
if guess == number: 
    print('Good job! You guessed the number in ' + str(guesses_left) + ' tries!')
else:
    print('Ouch, tough luck. You did not guess the number. It was ' + str(number))