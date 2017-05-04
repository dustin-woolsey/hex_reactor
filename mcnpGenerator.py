import matplotlib.pyplot as plt
from numpy import sin, cos, linspace, array, pi
import csv


def gen_full_core(pin_pitch, el_rings, core_rings, assembly_pitch = None):
    pp = pin_pitch
    er = el_rings
    cr = core_rings


    if assembly_pitch:
        ap = assembly_pitch

    else:
        #ap = (pp) * (er + 1) *(1 + cos(60 * pi/180))
        ap = pp * sin(60 * (pi/180)) * ((2 * er ) - (.5 * pp * sin(60 * (pi/180))))



    yf = cos(60 * (pi/180)) * ap
    xf = sin(60 * (pi/180)) * ap


    x_1, y_1 = gen_initial_rod_pos(pp, er)
    x_list = [x_1]
    y_list = [y_1]

    for ring in range(cr - 1):
        x_list.append([item for item in x_1])
        y_list.append([item + (ap * (ring + 1)) for item in y_1])

        x_list.append([item for item in x_1])
        y_list.append(([item - (ap * (ring + 1)) for item in y_1]))

        ####################################################

        x_list.append([item + (xf * (ring+1)) for item in x_1])
        y_list.append([item + (yf * (ring + 1)) for item in y_1])

        x_list.append([item - (xf * (ring+1)) for item in x_1])
        y_list.append([item + (yf * (ring + 1)) for item in y_1])

        x_list.append([item + (xf * (ring+1)) for item in x_1])
        y_list.append([item - (yf * (ring + 1)) for item in y_1])

        x_list.append([item - (xf * (ring+1)) for item in x_1])
        y_list.append([item - (yf * (ring + 1)) for item in y_1])


    for ind, it in enumerate(x_list):
        plt.plot(it, y_list[ind], 'o')

    plt.show()
    return x_list, y_list


def gen_initial_rod_pos(pin_pitch, el_rings):

    x_li = [0.0]
    y_li = [0.0]
    pp = pin_pitch
    nr = el_rings

    x_off = cos((pi / 180) * 60) * pp
    y_off =  sin((pi / 180) * 60) * pp

    for ring in range(nr- 1):

        #Generate horizontal components
        x_li.append(pp * (ring + 1))
        y_li.append(0.0)

        x_li.append(-pp * (ring + 1))
        y_li.append(0.0)

        #Generate upper and lower right elements
        x_li.append(x_off * (ring + 1))
        y_li.append(y_off * (ring + 1))

        x_li.append(x_off * (ring + 1))
        y_li.append(-y_off * (ring + 1))

        for el in range(ring + 1):
            x_li.append(x_off * (ring + 1) - (pp * (el + 1)))
            y_li.append(y_off * (ring + 1))

            x_li.append(x_off * (ring + 1) - (pp * (el + 1)))
            y_li.append(-y_off * (ring + 1))


        for r in range((nr - 1) - ring):
            x_li.append((pp * (ring + 1))+ (x_off * (r)))
            y_li.append(0.0 + (y_off * r))

            x_li.append((pp * (ring + 1))+ (x_off * r))
            y_li.append(0.0 - (y_off * r))

            x_li.append((-pp * (ring + 1))- (x_off * r))
            y_li.append(0.0 + (y_off * r))

            x_li.append((-pp * (ring + 1))- (x_off * r))
            y_li.append(0.0 - (y_off * r))



    def clean_list():

        coords = []
        coords_clean = []
        x_list = []
        y_list = []

        for index, item in enumerate(x_li):
            coords.append((item, y_li[index]))


        for it in coords:
            if it in coords_clean:
                pass
            else:
                coords_clean.append(it)


        for i in coords_clean:
            x_list.append(i[0])
            y_list.append(i[1])

        return x_list, y_list


    x_l, y_l = clean_list()
    #print len(x_l)

    #plt.plot(x_l, y_l, 'bo')
    #plt.show()

    return x_l, y_l


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

    #plt.plot(x, y, 'bo')
    #plt.show()

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

    x_8 = x_1
    y_8 = [item -(2 * 14.7) for item in y_1]

    x_9 = x_1
    y_9 = [item + (2 *14.7) for item in y_1]

    x_10 = [item + x_off for item in x_1]
    y_10 = [item + y_off + 14.7 for item in y_1]

    x_11 = [item - x_off for item in x_1]
    y_11 = [item + y_off + 14.7 for item in y_1]

    x_12 = [item + x_off for item in x_1]
    y_12 = [item - y_off  - 14.7 for item in y_1]

    x_13 = [item - x_off for item in x_1]
    y_13 = [item - y_off  - 14.7 for item in y_1]

    x_14 = [item + (2*x_off) for item in x_1]
    y_14 = [item + (2 *y_off) for item in y_1]

    x_15 = [item - (2*x_off) for item in x_1]
    y_15 = [item + (2*y_off) for item in y_1]

    x_16 = [item + (2*x_off) for item in x_1]
    y_16 = [item + (2 *y_off) - 14.7 for item in y_1]

    x_17 = [item - (2*x_off) for item in x_1]
    y_17 = [item + (2*y_off) - 14.7 for item in y_1]

    x_18 = [item + (2*x_off) for item in x_1]
    y_18 = [item + (2 *y_off) - (2*14.7) for item in y_1]

    x_19 = [item - (2*x_off) for item in x_1]
    y_19 = [item + (2*y_off)  - (2*14.7) for item in y_1]

    x_20 = x_1
    y_20 = [item + (3 *14.7) for item in y_1]

    x_21 = [item + x_off for item in x_1]
    y_21 = [item + y_off + (2 * 14.7) for item in y_1]

    x_22 = [item - x_off for item in x_1]
    y_22 = [item + y_off + (2 * 14.7) for item in y_1]

    x_23 = [item + x_off for item in x_1]
    y_23 = [item - y_off  - (2 *14.7) for item in y_1]

    x_24 = [item - x_off for item in x_1]
    y_24 = [item - y_off  - (2*14.7) for item in y_1]

    x_25 = [item + (2*x_off) for item in x_1]
    y_25 = [item + (2 *y_off)+14.7 for item in y_1]

    x_26 = [item - (2*x_off) for item in x_1]
    y_26 = [item + (2*y_off)+14.7 for item in y_1]

    x_27 = [item + (3*x_off) for item in x_1]
    y_27 = [item + (3 *y_off) for item in y_1]

    x_28 = [item - (3*x_off) for item in x_1]
    y_28 = [item + (3*y_off) for item in y_1]

    x_29 = [item + (3*x_off) for item in x_1]
    y_29 = [item + (3 *y_off)-14.7 for item in y_1]

    x_30 = [item - (3*x_off) for item in x_1]
    y_30 = [item + (3*y_off)-14.7 for item in y_1]

    x_31 = [item + (3*x_off) for item in x_1]
    y_31 = [item + (3 *y_off)-(2*14.7) for item in y_1]

    x_32 = [item - (3*x_off) for item in x_1]
    y_32 = [item + (3*y_off)-(2*14.7) for item in y_1]

    x_33 = [item + (3*x_off) for item in x_1]
    y_33 = [item + (3 *y_off)-(3*14.7) for item in y_1]

    x_34 = [item - (3*x_off) for item in x_1]
    y_34 = [item + (3*y_off)-(3*14.7) for item in y_1]

    x_35 = [item + (2*x_off) for item in x_1]
    y_35 = [item + (2 *y_off) - (3*14.7) for item in y_1]

    x_36 = [item - (2*x_off) for item in x_1]
    y_36 = [item + (2*y_off)  - (3*14.7) for item in y_1]

    x_37 = x_1
    y_37 = [item -(3 * 14.7) for item in y_1]


    x_list = [x_1, x_2, x_3, x_4, x_5 ,x_6 ,x_7,x_8, x_9, x_10, x_11, x_12 ,x_13 ,x_14,x_15, x_16, x_17, x_18, x_19,
              x_20, x_21, x_22, x_23, x_24, x_25, x_26, x_27, x_28, x_29, x_30, x_31, x_32, x_33, x_34, x_35, x_36, x_37]
    y_list = [y_1, y_2, y_3, y_4, y_5 ,y_6 ,y_7,y_8, y_9, y_10, y_11, y_12 ,y_13 ,y_14,y_15, y_16, y_17, y_18, y_19,
              y_20, y_21, y_22, y_23, y_24, y_25, y_26, y_27, y_28, y_29, y_30, y_31, y_32, y_33, y_34, y_35, y_36, y_37]



    #TEST POSITIONS

    plt.plot(x_1, y_1, 'ro', x_2, y_2, 'bo' , x_3, y_3, 'bo', x_4, y_4, 'bo', x_5, y_5, 'bo', x_6, y_6, 'bo', x_7, y_7, 'bo')
    plt.plot(x_8, y_8, 'yo', x_9, y_9, 'yo' , x_10, y_10, 'yo', x_11, y_11, 'yo', x_12, y_12, 'yo', x_13, y_13, 'yo')
    plt.plot( x_14, y_14, 'yo', x_15, y_15, 'yo', x_16, y_16, 'yo', x_17, y_17, 'yo', x_18, y_18, 'yo', x_19, y_19, 'yo')
    plt.plot( x_20, y_20, 'go', x_21, y_21, 'go', x_22, y_22, 'go',  x_23, y_23, 'go', x_24, y_24, 'go', x_25, y_25, 'go')
    plt.plot( x_26, y_26, 'go', x_27, y_27, 'go', x_28, y_28, 'go',  x_29, y_29, 'go', x_30, y_30, 'go', x_31, y_31, 'go')
    plt.plot( x_32, y_32, 'go', x_33, y_33, 'go', x_34, y_34, 'go',  x_35, y_35, 'go', x_36, y_36, 'go', x_37, y_37, 'go')


    plt.plot(x_1, y_1, 'bo')
    for index, x_item in enumerate(x_list):
        y_item = y_list[index]
        plt.text(x_item[0]-0.5, y_item[0]-0.5, str(index + 1), fontsize=20)
    plt.show()

#    print len(x_1)
    #x_list = [x_1, x_2, x_3, x_4, x_5 ,x_6 ,x_7]
    #y_list = [y_1, y_2, y_3, y_4, y_5, y_6, y_7]

    #x_list = [x_1, x_2, x_3, x_4, x_5 ,x_6 ,x_7,x_8, x_9, x_10, x_11, x_12 ,x_13 ,x_14,x_15, x_16, x_17, x_18, x_19]
    #y_list = [y_1, y_2, y_3, y_4, y_5 ,y_6 ,y_7,y_8, y_9, y_10, y_11, y_12 ,y_13 ,y_14,y_15, y_16, y_17, y_18, y_19]

    #x_list = [x_1]
    #y_list = [y_1]
    return  x_list , y_list


def fill_rod_position():
    x_l, y_l = get_all_rod_pos()

    fill = 100
    s = 'c ******************************************************************************\n'
    s += 'c ** Fuel Rod Position Filling\n'
    s += 'c ==============================================================================\n'

    for index, x_i in enumerate(x_l):
        y_i = y_l[index]

        for i, x_it in enumerate(x_i):
            y_it = y_i[i]

            assembly_ID = index + 1
            rod_ID = i + 1

            ID = assembly_ID * 1000 + rod_ID + 10000
            ID2 = assembly_ID * 1000 + rod_ID + 900000

            un = index + 1
            s+= '  {}     0     -{} fill={:<3d} ({:10.6f} {:10.6f} 0.0) imp:n=1 u=0\n'.format(ID2, ID, fill, x_it, y_it)

            fill += 1

    return s


def write_fuel_universes(x_l, y_l):
    s = 'c ******************************************************************************\n'
    s += 'c ** FUEL UNIVERSES: Individual FE"s\n'
    s += 'c ==============================================================================\n'
    s += '  100100     1  -10.5     -100 105 -20    imp:n=1 u=100 $ Meat\n'
    s += '  100101     2  -6.55     -102 105 21 -22 imp:n=1 u=100 $ Cladding\n'
    s += '  100102     2  -0.001    -100 105 20 -21 imp:n=1 u=100 $ Gas Gap\n'
    s += '  100103     2  -6.55      102 -103 -22 imp:n=1   u=100 $ Top Cap\n'
    s += '  100104     2  -6.55     -105 106 -22  imp:n=1   u=100 $ Bottom Cap\n'
    s += '  100105     2  -6.55      103 -104 -23 imp:n=1   u=100 $ Top Plug\n'
    s += '  100106     2  -6.55     -106 107 -24  imp:n=1   u=100 $ Bottom Plug\n'
    s += '  100107     3  -0.777537  104          imp:n=1   u=100 $ Water Above Plug\n'
    s += '  100108     3  -0.777537 -104 103 23   imp:n=1   u=100 $ Water RadiallyTop\n'
    s += '  100109     3  -0.777537 -107          imp:n=1   u=100 $ Water Below pin\n'
    s += '  100110     3  -0.777537  107 -106 24  imp:n=1   u=100 $ Water RadiallyBottom\n'
    s += '  100111     3  -0.777537 -102 105 22   imp:n=1   u=100 $ Water Around pin\n'
    s += '  100112     3  -0.777537 -103 102 22   imp:n=1   u=100 $ Water upcap\n'
    s += '  100113     2  -0.001     100 -102 -21 imp:n=1   u=100 $ UpperGas Gap\n'
    s += '  100114     3  -0.777537 -105 106 22   imp:n=1 u=100 $ WaterRadial 100110\n'
    s += 'c ******************************************************************************\n'

    u = 101
    ID = 100200


    for index, x_i in enumerate(x_l):
        y_i = y_l[index]

        for ind, x_it in enumerate(x_i):
            y_it = y_i[ind]

            if index == 0 and ind == 0:
                pass
            else:

                s += 'c ==============================================================================\n'
                s += '  {} like {} but u={}\n'.format(ID, 100100, u)
                s += '  {} like {} but u={}\n'.format(ID + 1, 100101, u)
                s += '  {} like {} but u={}\n'.format(ID + 2, 100102, u)
                s += '  {} like {} but u={}\n'.format(ID + 3, 100103, u)
                s += '  {} like {} but u={}\n'.format(ID + 4, 100104, u)
                s += '  {} like {} but u={}\n'.format(ID + 5, 100105, u)
                s += '  {} like {} but u={}\n'.format(ID + 6, 100106, u)
                s += '  {} like {} but u={}\n'.format(ID + 7, 100107, u)
                s += '  {} like {} but u={}\n'.format(ID + 8, 100108, u)
                s += '  {} like {} but u={}\n'.format(ID + 9, 100109, u)
                s += '  {} like {} but u={}\n'.format(ID + 10, 100110, u)
                s += '  {} like {} but u={}\n'.format(ID + 11, 100111, u)
                s += '  {} like {} but u={}\n'.format(ID + 12, 100112, u)
                s += '  {} like {} but u={}\n'.format(ID + 13, 100113, u)
                s += '  {} like {} but u={}\n'.format(ID + 14, 100114, u)

                ID += 100


                u += 1

    return s

def write_rod_surfaces(x_l, y_l):

    s = 'c ***************************************************************\n'
    s += 'c ELEMENT SURFACES\n'
    s += 'c ***************************************************************\n'
    s += 'c ** Cylinders: Surface 20\n'
    s += 'c ** Planes: Surface 100  \n'
    s += 'c ==============================================================================\n'
    s += 'c Cylinders **From VVER Fuel Specs PPT**\n'
    s += '  20    cz 0.38              $ Fuel\n'
    s += '  21    cz 0.3865            $ Cladding inner\n'
    s += '  22    cz 0.455             $ Cladding outer\n'
    s += '  23    cz 0.3               $ Top plug\n'
    s += '  24    cz 0.25              $ Bottom Plug\n'
    s += 'c ==============================================================================\n'
    s += 'c Cylinders for core boundaries \n'
    s += '  30    cz 115                          $ Water boundary\n'
    s += 'c ==============================================================================\n'
    s += 'c Planes for core boundaries\n'
    s += '  40    pz     926.8                   $ Water top\n'
    s += '  41    pz    -226.8                   $ Water bottom\n'
    s += 'c ==============================================================================\n'
    s += 'c Planes **Elevations from VVER Fuel Specs PPT**\n'
    s += '  100 pz  116.8              $ Fuel top\n'
    s += '  101 pz -125.7              $ Fuel bottom\n'
    s += '  102 pz  125.75             $ Cladding top/Bottom of Top Cap\n'
    s += '  103 pz  126.25             $ Top of Top cap/Bottom of Top Plug\n'
    s += '  104 pz  126.8              $ Top of Top Plug\n'
    s += '  105 pz -125.2              $ Cladding bottom/Top of Bottom Cap\n'
    s += '  106 pz -125.7              $ Bottom of Bottom Cap/Top of Bottom Plug\n'
    s += '  107 pz -126.8              $ Bottom of Bottom Plug\n'
    s += 'c ***************************************************************\n'

    for index, x_i in enumerate(x_l):
        y_i = y_l[index]

        for i, x_it in enumerate(x_i):
            y_it = y_i[i]

            assembly_ID = index + 1
            rod_ID = i + 1

            ID = assembly_ID * 1000 + rod_ID + 10000

            s += ' {}       c/z   {: 10.6f}   {: 10.6f}   0.4572\n'.format(ID,x_it, y_it )

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
    s += '       41093.80c    -0.01   $ NB\n'
    s += '       8016.70c     -0.001  $ O\n'
    s += '       26000.42c    -0.0005 $ Fe\n'
    s += '       28000.42c    -0.0002 $ Ni\n'
    s += '       24000.42c    -0.0002 $ Cr\n'
    s += '       6000.70c     -0.0002 $ C\n'
    s += '       72000.42c    -0.0001 $ Hf \n'
    s += 'c ===============================================================\n'
    s += 'c Moderator (H2O (99.70)+H3BO3 (0.30)) [w %]\n'
    s += 'c Density: 0.777537g/cc ** From VVER 440.pdf**\n'
    s += 'm3    1001.70c   -0.063116 $ H\n'
    s += '      8016.70c   -0.80149  $ O\n'
    s += '      5010.70c   -0.135394 $ B\n'

    return s

def write_tallys(x_l, y_l):
    ID = 100100
    count = 0

    s = ''

    for index, x_i in enumerate(x_l):
        y_i = y_l[index]

        for ind, x_it in enumerate(x_i):
            y_it = y_i[ind]


            if count == 8:
                s += '&\n      '
                count = 0

            s += str(ID) + ' '

            ID += 100
            count += 1


    s_prime = 'c ************************* TALLY SPECIFICATION ********************************\n'
    s_prime += 'c Flux average tally for active fuel region of all elements\n'
    s_prime += 'f4:n  ' + s + '\n'
    s_prime += 'f7:n  ' + s

    return s_prime


def write_sdef():

    s= 'c ******************************************************************************\n'
    s+= 'c Source cards \n'
    s+= 'c ******************************************************************************\n'
    s+= 'c SOURCE DISTRIBUTED ACROSS THE CORE VOLUME\n'
    s+= 'sdef ERG=D1 POS=0 0 0 AXS=0 0 1 RAD=D2 EXT=D3\n'
    s+= 'sp1 -3\n'
    s+= 'si2 0 56.5            $ radius of the active region\n'
    s+= 'si3 -126 117    $ height of the active region\n'

    return s

def write_imp():

    s = 'c ***************************************************************\n'
    s += 'imp:n             0            1        11567r       $\n'
    return s


def write_kcode_ect():
    s = 'c ***************************************************************\n'
    s += 'mode  n\n'
    s += 'kcode 10000 1.500000 30 250 300000\n'
    return s

def write_intro_mat():
    s = 'c ******************************************************************************\n'
    s+= 'c ** VVER 440 practice core design\n'
    s+= 'c ==============================================================================\n'
    return s


def write_main_cells():
    s = 'c ***************************************************************\n'
    s += 'c Primary Cells\n'
    s += 'c ***************************************************************\n'
    s += '  2      0      30 : 40  :-41  imp:n=0           $ Graveyard\n'

    return s

def write_core_water_cell(x_l, y_l):
    cnt = 5

    s = ''
    for index, x_i in enumerate(x_l):


        y_i = y_l[index]

        for i, x_it in enumerate(x_i):
            y_it = y_i[i]

            assembly_ID = index + 1
            rod_ID = i + 1

            ID = assembly_ID * 1000 + rod_ID + 10000
            cnt += 1

            if cnt == 10:
                s += '\n             '
                cnt = 0
            s += str(ID) + ' '


    s_prime = 'c **********************************************************************\n'
    s_prime += 'c Water around core\n'
    s_prime += 'c **********************************************************************\n'
    s_prime += '  668     3   -0.777537   -30   -40   41   '+ s + 'imp:n=1\n'

    return s_prime

def write_file(outputName, s):

    with open(outputName if outputName else 'hex.i', 'w') as f:
        f.write(s)


def form_string():

    gen_full_core(2, 7, 3, assembly_pitch = None)
    exit()
    x_l, y_l = get_all_rod_pos()
    s = write_intro_mat()
    s += 'c\n'
    s += write_main_cells()
    s += fill_rod_position()
    s += write_core_water_cell(x_l, y_l)
    s += write_fuel_universes(x_l, y_l)
    s += 'c\n'


    s += '\n'
    s += write_rod_surfaces(x_l, y_l)
    s+= '\n'
    s += write_kcode_ect()
    s += write_materials()
    #s += write_imp()
    s += write_sdef()
    s += write_tallys(x_l, y_l)

    return s

if __name__ == '__main__':
    write_file(outputName = 'test.i', s =form_string())