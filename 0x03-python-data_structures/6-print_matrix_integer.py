#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        if matrix[0]:
            for i in matrix:
                for j in i:
                    print("{:d}".format(j), end='')
                    if i.index(j) < (len(i) - 1):
                        print(" ", end='')
                    else:
                        print("")
        else:
            print("")
    else:
        print("")
