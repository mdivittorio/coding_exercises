from datetime import date


def main():
    """
    Create a program that prints a message addressed to user
    that tells them the year they'll turn 100.
    """
    name = input('Please enter your name: ')
    age = input('Please enter your age: ')
    copies = input('How many would you like? ')
    for _ in range(int(copies)):
        print(f'{name.capitalize()}, you will turn 100 years old in the year {100-int(age)+date.today().year}')


main()
