def main():
    not_pal = 'fish'
    not_pal2 = 'pony'
    pal = 'madam'
    pal2 = 'racecar'
    print(f'{not_pal}: {is_palindrome(not_pal)}')
    print(f'{not_pal2}: {is_palindrome(not_pal2)}')
    print(f'{pal}: {is_palindrome(pal)}')
    print(f'{pal2}: {is_palindrome(pal2)}')
    print(f'{not_pal}: {is_palindrome_efficient(not_pal)}')
    print(f'{not_pal2}: {is_palindrome_efficient(not_pal2)}')
    print(f'{pal}: {is_palindrome_efficient(pal)}')
    print(f'{pal2}: {is_palindrome_efficient(pal2)}')


def is_palindrome(input: str):
    reversed_str = input[::-1]
    for index, char in enumerate(input):
        if char != reversed_str[index]:
            return False
    return True


def is_palindrome_efficient(input: str):
    str_len = len(input)
    for index, char in enumerate(input):
        reverse_index = str_len-index-1
        if char != input[reverse_index]:
            return False
        if index >= reverse_index:
            return True



main()
