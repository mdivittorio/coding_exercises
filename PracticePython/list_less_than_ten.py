def main():
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    less_than_five(numbers)
    print('------')
    less_than_five_list(numbers)
    print('------')
    less_than_five_one_liner(numbers)
    print('------')
    less_than_given(9, numbers)


def less_than_given(expected: int, numbers: list):
    for number in numbers:
        if number < expected:
            print(f'{number} is less than {expected}.')


def less_than_five(numbers: list):
    less_than_given(5, numbers)


def less_than_five_list(numbers: list):
    less_than_five = []
    for number in numbers:
        if number < 5:
            less_than_five.append(number)
    print(less_than_five)


def less_than_five_one_liner(numbers: list):
    [print(x) for x in numbers if x < 5]


main()
