#!/usr/bin/python3
for i1 in range(10):
    for i2 in range(i1 + 1, 10):
        print("{}{}".format(i1, i2), end='')
        if i1 != 8 or i2 != 9:
            print(", ", end='')
print('')
