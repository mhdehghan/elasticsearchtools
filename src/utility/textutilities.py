import random
import string


def random_string(length=10):
    letter = string.ascii_letters + string.digits
    return ''.join(random.choice(letter) for i in range(length))

def random_digit(length=10):
    digit= string.digits
    return ''.join(random.choice(digit) for i in range(length))


if __name__ == "__main__":
    print(random_string())
    print(random_digit())
