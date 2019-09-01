def main():
    get_divisors(50)


def get_divisors(num: int):
    divisors = []
    for i in range(num):
        current = num-i
        if num % current == 0:
            divisors.append(current)
    print(f'Divisors of {num} are: {divisors}')


main()
