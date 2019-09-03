def main():
    print(generate_fibonacci(0))
    print(generate_fibonacci(1))
    print(generate_fibonacci(2))
    print(generate_fibonacci(5))
    print(generate_fibonacci(10))


def generate_fibonacci(num: int):
    sequence = []
    for i in range(0, num):
        if i in [0, 1]:
            sequence.append(1)
        else:
            sequence.append(sequence[-1] + sequence[-2])
    return sequence


main()
