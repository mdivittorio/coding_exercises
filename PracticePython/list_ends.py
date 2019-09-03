def main():
    a = [5, 10, 15, 20, 25]
    print(get_ends(a))


def get_ends(lis: list):
    return [lis[0], lis[-1]]


main()
