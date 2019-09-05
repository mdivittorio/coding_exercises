def main():
    expected = 1234
    guess1 = 9087   # 0 cows, 0 bulls
    guess2 = 9256   # 1 cow, 0 bulls
    guess3 = 1408   # 1 cow, 1 bull
    guess4 = 1111   # 1 cow, 3 bulls
    guess5 = 1231   # 3 cows, 1 bull
    guess6 = 1234   # 4 cows, 0 bulls
    guess7 = 4321   # 0 cows, 4 bulls
    cows_and_bulls(expected, guess1)
    cows_and_bulls(expected, guess2)
    cows_and_bulls(expected, guess3)
    cows_and_bulls(expected, guess4)
    cows_and_bulls(expected, guess5)
    cows_and_bulls(expected, guess6)
    cows_and_bulls(expected, guess7)


def cows_and_bulls(expected, guess):
    expected_str = str(expected)
    guess_str = str(guess)
    if len(guess_str) != len(expected_str):
        raise ValueError(f'Expected {len(str(expected))} digits, received {len(str(guess))} digits.')
    cows, bulls = 0, 0
    for index, digit in enumerate(guess_str):
        if digit == expected_str[index]:
            cows += 1
        elif digit in expected_str:
            bulls += 1
        else:
            continue
    print(f'{cows} cow(s), {bulls} bull(s)')


main()
