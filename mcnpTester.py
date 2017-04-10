import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos, linspace, array, pi
import csv


def get_column(col):

    with open('test.i', 'r') as infile:

        data = infile.read()  # Read the contents of the file into memory.

    # Return a list of the lines, breaking at line boundaries.
    my_list = data.splitlines()

    line = 1
    for row in my_list:

            if len(row) == 0:
                pass
            else:
                line += 1
                item = row[col - 1]


                if str(item) == 'c' or str(item) == ' ':
                    pass
                else:
                    print 'VAL: ' + str(item)  + ' LINE: ' + str(line) + ' \n'



if __name__ == '__main__':
    get_column(1)