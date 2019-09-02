def main():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print(get_evens(a))


def get_evens(lis: list):
    return [x for x in lis if x % 2 == 0]


main()
