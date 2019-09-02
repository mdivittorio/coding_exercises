import random


def main():
    guesses = 0
    while True:
        rand = random.choice(range(1, 10))
        guess = input("I'm thinking of a number between 1 and 10...what is it? ")
        if guess == 'exit':
            break
        elif int(guess) == rand:
            print('Congratulations! You guessed correctly!')
        else:
            print(f'Oof, it was actually {rand}, better luck next time!')
        guesses += 1
    print(f'User guessed a total of {guesses} times.')


main()
