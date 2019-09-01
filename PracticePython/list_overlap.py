import random


def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    list_overlap(a, b)

    lists = random_lists()
    list_overlap(lists[0], lists[1])


def list_overlap(list_a: list, list_b: list):
    common = []
    max_min = (list_a, list_b) if len(list_a) >= len(list_b) else (list_b, list_a)
    for num in max_min[0]:
        if num in max_min[1] and num not in common:
            common.append(num)
    print(f'Common values: {common}')


def random_lists() -> tuple:
    # return 10 values between 1 and 49
    list_a = random.sample(range(1, 51), 10)

    # return 15 values between 1 and 100
    list_b = random.sample(range(1, 101), 15)
    return list_a, list_b


main()
