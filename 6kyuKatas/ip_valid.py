#!/usr/local/bin/python

"""
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
IPs should be considered valid if they consist of four octets,
with values between 0 and 255, inclusive.

Note: leading 00 is considered invalid
"""


def is_valid_ip(strng):
    ip_check = strng.split('.')
    if len(ip_check) < 4 or len(ip_check) > 4:
        return False

    for ip_oct in ip_check:
        if not ip_oct.isdigit():
            return False
        a = int(ip_oct)
        if ip_oct.find('0') == 0 and a != 0:
            return False
        if a < 0 or a > 255:
            return False
        if ip_oct == "00" or ip_oct == "000":
            return False
    return True


if __name__ == '__main__':
    test_ip1 = "10.0.0.1"
    test_ip2 = "10.0.0.0.0"
    test_ip3 = "1402938.2314082104.1203948"
    test_ip4 = "192.168.10.20"
    test_new = "00.102.203.44"

    print(is_valid_ip(test_ip1))
    print(is_valid_ip(test_ip2))
    print(is_valid_ip(test_ip3))
    print(is_valid_ip(test_ip4))
    print(is_valid_ip(test_new))

