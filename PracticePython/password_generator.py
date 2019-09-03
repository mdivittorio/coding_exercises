import random
import string


def main():
    print(generate_password(16))


def generate_password(length: int):
    available_chars = []
    available_chars.extend(list(string.printable))  # TODO get rid of CR
    reg_chars = list(string.ascii_letters)
    reg_chars.extend(list(string.digits))
    special_chars = [x for x in available_chars if x not in reg_chars]
    while True:
        pwd = ''
        has_upper = has_lower = has_num = has_special = False
        for i in range(length):
            current = random.choice(available_chars)
            pwd = pwd + current
            if current in list(string.ascii_lowercase):
                has_lower = True
            elif current in list(string.ascii_uppercase):
                has_upper = True
            elif current in list(string.digits):
                has_num = True
            elif current in special_chars:
                has_special = True
        if has_upper and has_lower and has_num and has_special:
            return pwd


main()
