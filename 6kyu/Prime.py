from math import sqrt


def is_prime(num):
    if num <= 1:
        return False
    i = 2
    while i <= sqrt(num):
        if num % i == 0:
            return False
        i += 1
    return True


if __name__ == '__main__':
    print("Program is running.....\n")
    test_num = is_prime(73)
    print(test_num)
