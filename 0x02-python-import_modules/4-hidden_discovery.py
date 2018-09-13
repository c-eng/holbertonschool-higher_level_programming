#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for idx in range(len(names)):
        if names[idx][0] != "_" and names[idx][1] != "_":
            print("{:s}".format(names[idx]))
