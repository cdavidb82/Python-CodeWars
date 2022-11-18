def narcissistic(value):
    return value == sum([int(n) ** len(str(value)) for n in str(value)])


if __name__ == "__main__":
    this_number = narcissistic(20348902034957)
    print(this_number)
