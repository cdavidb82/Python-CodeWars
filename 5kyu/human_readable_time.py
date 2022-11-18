

def make_readable(seconds):
    return_string = str(seconds//(60*60)).zfill(2) + ":"
    for_min = seconds % (60 * 60)
    return_string = return_string + str(for_min//60).zfill(2) + ":"
    for_sec = for_min % 60
    return_string = return_string + str(for_sec).zfill(2)
    return return_string

if __name__ == "_main__":
    print(make_readable(0))
    print(make_readable(5))
    print(make_readable(60))
