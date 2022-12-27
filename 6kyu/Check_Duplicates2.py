def duplicate_count(text):

    return len([c for c in set(text.lower()) if text.lower().count(c) > 1])


if __name__ == '__main__':
    pass
