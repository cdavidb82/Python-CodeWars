def duplicate_count(text):
    check = text.lower()
    output = 0
    for l in check:
        if check.count(l) > 1:
            check = check.replace(l, '')
            output += 1
    return output


if __name__ == '__main__':
    pass
