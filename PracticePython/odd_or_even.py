def main():
    """
    Check if provided value is odd or even.
    Print something else if multiple of 4.
    """
    value = int(input('Please enter a number: '))
    if value % 4 == 0:
        print('Looks like you have a multiple of 4 there, partner.')
    else:
        evenity = 'even' if (value % 2) == 0 else 'odd'
        print(f'The number {value} is {evenity}.')

main()
