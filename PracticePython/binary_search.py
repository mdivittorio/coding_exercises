from math import ceil


def main():
    lis = [1, 4, 5, 9, 11, 13, 19, 22, 23, 24]
    print(binary_search(lis, 23))
    print(binary_search(lis, 24))
    print(binary_search(lis, 1))
    print(binary_search(lis, 4))
    print(binary_search(lis, 0))
    print(binary_search(lis, 25))
    print(binary_search(lis, 12))


def binary_search(inputs: list, value: int) -> bool:
    if not inputs:
        return False
    mid = ceil(len(inputs)/2) - 1
    current = inputs[mid]
    if current == value:
        return True
    elif len(inputs) == 1:
        return False
    elif current > value:
        return binary_search(inputs[:mid], value)
    else:
        return binary_search(inputs[mid+1:], value)


main()