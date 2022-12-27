#!/usr/local/bin/python
import random as r

def create_phone_number():
    digit = []
    digit.append(r.randint(6, 9))
    for i in range(1, 10):
        digit.append(r.randint(0, 9))

    phone_number = "{}{}{} {}{}{}-{}{}{}{}".format(*digit)
    print(phone_number)




if __name__ == '__main__':
    create_phone_number()
