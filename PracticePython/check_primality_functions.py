def main():
    print(is_prime(5))
    print(is_prime(7))
    print(is_prime(8))
    print(is_prime(13))
    print(is_prime(22))


def is_prime(value: int):
    if value == 1:
        return False
    elif value == 2:
        return True
    else:
        for num in range(2, int(value/2)+1):
            if value % num == 0:
                return False
        return True


main()
