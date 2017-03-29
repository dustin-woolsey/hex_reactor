import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos, linspace, array, pi
import csv




letter = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7}


def read_rod_pos():
    x = []
    y = []



    with open('hex_from_sat_4.txt', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
            if ((int(row[2]) - 1) % 3) == 0:
                x_p = float(row[10])
                y_p = float(row[11])

                if abs(x_p) <= 1E-10:
                    x_p = 0

                if abs(y_p) <= 1E-10:
                    y_p = 0



                x.append(x_p)
                y.append(y_p)




    plt.plot(x, y, 'bo')
    plt.show()

    return x, y


def get_all_rod_pos():
    x_1, y_1 = read_rod_pos()

    x_2 = x_1
    y_2 = [item - 14.7 for item in y_1]

    x_3 = x_1
    y_3 = [item + 14.7 for item in y_1]

    plt.plot(x_1, y_1, 'bo', x_2, y_2, 'bo' , x_3, y_3, 'bo')
    plt.show()

def get_assembly_rod_pos(n_rings, fuel_pitch):
    '''

    :param n_rings:  number of rings
    :param fuel_pitch: center to center distance of individual fuel elements
    :return: central rod positions
    '''

    x = [0]
    y = [0]

    vert_dist = sin(60) * fuel_pitch
    hor_dist = cos(60) * fuel_pitch

    for ring in range(n_rings):    # rings range from 0 to n_rings - 1



        if ring == 0:
            pass                # Center position is already generated

        else:

            #Generate elements along symmetry lines
            x.append(fuel_pitch * ring)
            y.append(0)

            x.append( - fuel_pitch * ring)
            y.append(0)

            x.append(hor_dist * ring)
            y.append(vert_dist * ring)

            x.append(-hor_dist * ring)
            y.append(vert_dist * ring)

            x.append(hor_dist * ring)
            y.append(-vert_dist * ring)

            x.append(-hor_dist * ring)
            y.append(-vert_dist * ring)


            #generate elements on horizontal planes

            n = None

            if ring > 1:
                n = ring - 1


            if n and n % 2 == 0:    # IF EVEN

                cyd = int(n / 2)

                for num_d in range(cyd):
                    num_d = (num_d * 2) +  1

                    x.append(num_d * hor_dist)
                    y.append(vert_dist * ring)

                    x.append(-num_d * hor_dist)
                    y.append(vert_dist * ring)

                    x.append(num_d * hor_dist)
                    y.append(-vert_dist * ring)

                    x.append(-num_d * hor_dist)
                    y.append(-vert_dist * ring)



            elif n and n % 2 != 0:   # IF ODD
                x.append(0)
                y.append(vert_dist * ring)

                x.append(0)
                y.append(-vert_dist * ring)

                cyc = int(n / 2)

                for num_c in range(cyc):
                    num_c += 1
                    x.append(num_c * hor_dist * 2 )
                    y.append(vert_dist * ring)

                    x.append(-num_c * hor_dist * 2 )
                    y.append(vert_dist * ring)

                    x.append(num_c * hor_dist * 2 )
                    y.append(-vert_dist * ring)

                    x.append(-num_c * hor_dist * 2 )
                    y.append(-vert_dist * ring)


            else:
                pass
            #generate intermediate elements



                angle = 60 / n      # angle between rods on side of hexagon (Distance is pitch)

                for item in range(n):
                    pass               #TODO USE 60-90-30 triangle to find x  and y shift from x max  and y max for angled sides
                                       # Top and bottom will have constant y value








    centers = []


    return centers



def write_file(outputName, s):

    with open(outputName if outputName else 'hex.i', 'w') as f:
             f.write(s)




if __name__ == '__main__':
    get_all_rod_pos()