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

    x_off = 12.7305
    y_off = 14.7 / 2.0

    x_4 = [item + x_off for item in x_1]
    y_4 = [item + y_off for item in y_1]

    x_5 = [item - x_off for item in x_1]
    y_5 = [item + y_off for item in y_1]

    x_6 = [item + x_off for item in x_1]
    y_6 = [item - y_off for item in y_1]

    x_7 = [item - x_off for item in x_1]
    y_7 = [item - y_off for item in y_1]

    #TEST POSITIONS
    #plt.plot(x_1, y_1, 'bo', x_2, y_2, 'bo' , x_3, y_3, 'bo', x_4, y_4, 'bo', x_5, y_5, 'bo', x_6, y_6, 'bo', x_7, y_7, 'bo')
    #plt.show()

    x_list = [x_1, x_2, x_3, x_4, x_5 ,x_6 ,x_7]
    y_list = [y_1, y_2, y_3, y_4, y_5, y_6, y_7]

    return  x_list , y_list


def write_rod_surfaces():

    s = 'c ***************************************************************\n'
    s += 'c ROD SURFACES\n'
    s += 'c ***************************************************************\n'
    s += ' 11000         pz 126.8     $  Top of Fuel Rod\n' \
        ' 22000         pz -126.8    $  Bottom of Fuel Rod\n'


    x_l, y_l = get_all_rod_pos()

    for index, x_i in enumerate(x_l):
        y_i = y_l[index]

        for i, x_it in enumerate(x_i):
            y_it = y_i[i]

            assembly_ID = index + 1
            rod_ID = i + 1

            ID = assembly_ID * 10000 + rod_ID

            s += ' {}       c/z   {: 10.6f}   {: 10.6f}   0.4572 \n'.format(ID,x_it, y_it )

    return s

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


def write_materials():
    s = 'c ***************************************************************\n'
    s += 'c MATERIAL CARDS\n'
    s += 'c ***************************************************************\n'
    s += 'c FUEL for neutron transport (by mass fraction)\n'
    s += 'c (only U-235, U-238) rho = 10.970 g/cc\n'
    s += 'm1    92235.60c -0.05000 $ U-235 and mass fraction\n'
    s += '      92238.60c -0.95000 $ U-238 and mass fraction\n'
    s += 'c ==============================================================\n'
    s += 'c Cladding E-110 Zr(98.78)+Nb(1.00)+O(0.10)+Fe(0.05)+Ni(0.02)\n'
    s += 'c +Cr(0.02)+C(0.02)+Hf(0.01) [w %]\n'
    s += 'c **From VVER440.pdf**\n'
    s += 'c Density: 6.55 g/cc\n'
    s += 'm2     40000.42c    -0.9878 $ Zr\n'
    s += '       41000.70c    -0.01   $ NB\n'
    s += '       8016.70c     -0.001  $ O\n'
    s += '       26000.42c    -0.0005 $ Fe\n'
    s += '       28000.42c    -0.0002 $ Ni\n'
    s += '       24000.42c    -0.0002 $ Cr\n'
    s += '       6000.70c     -0.0002 $ C\n'
    s += '       72000.42c    -0.0001 $ Hf \n'
    s += 'c===============================================================\n'
    s += 'c Gas gap material\n'
    s += 'c **Unknown**\n'
    s += 'c m3\n'
    s += 'c===============================================================\n'
    s += 'c Moderator (H2O (99.70)+H3BO3 (0.30)) [w %]\n'
    s += 'c Density: 0.777537g/cc ** From VVER 440.pdf**\n'
    s += 'm4    1001.70c   -0.063116 $ H\n'
    s += '      8016.70c   -0.80149  $ O\n'
    s += '      5010.70c   -0.135394 $ B\n'

    return s

def write_file(outputName, s):

    with open(outputName if outputName else 'hex.i', 'w') as f:
        f.write(s)


def form_string():
    s = write_rod_surfaces()
    s+= write_materials()
    return s

if __name__ == '__main__':
    write_file(outputName = 'surf_test.i', s =form_string())