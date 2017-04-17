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
    plt.plot(x_1, y_1, 'bo', x_2, y_2, 'bo' , x_3, y_3, 'bo', x_4, y_4, 'bo', x_5, y_5, 'bo', x_6, y_6, 'bo', x_7, y_7, 'bo')
    plt.show()

    print len(x_1)
    x_list = [x_1, x_2, x_3, x_4, x_5 ,x_6 ,x_7]
    y_list = [y_1, y_2, y_3, y_4, y_5, y_6, y_7]

    return  x_list , y_list



def fill_rod_position():
    x_l, y_l = get_all_rod_pos()

    fill = 101
    s = 'c ******************************************************************************\n'
    s += 'c ** Fuel Rod Position Filling\n'
    s += 'c ==============================================================================\n'

    for index, x_i in enumerate(x_l):
        y_i = y_l[index]

        for i, x_it in enumerate(x_i):
            y_it = y_i[i]

            assembly_ID = index + 1
            rod_ID = i + 1

            ID = assembly_ID * 10000 + rod_ID
            ID2 = assembly_ID * 1000 + rod_ID

            un = index + 1
            s+= '  {}     0         -{}  fill={:<3d} ({: 10.6f} {: 10.6f} {: 4.2f})  u={} $\n'.format(ID2, ID, fill, x_it, y_it, 0, un)

            fill += 1

    return s




def write_fuel_universes(x_l, y_l):
    s = 'c ******************************************************************************\n'
    s += 'c ** FUEL UNIVERSES: Individual FE"s\n'
    s += 'c ==============================================================================\n'
    s += '  100100     1  -10.5     -100 101 -20            u=100 $ Meat\n'
    s += '  100101     2  -6.55     -102 105 21 -22         u=100 $ Cladding\n'
    s += '  100102     2  -0.000001 -100 101 20 -21         u=100 $ Gas Gap\n'
    s += '  100103     2  -6.55      102 -103 -22           u=100 $ Top Cap\n'
    s += '  100104     2  -6.55     -105 106 -22            u=100 $ Bottom Cap\n'
    s += '  100105     2  -6.55      103 -104 -23           u=100 $ Top Plug\n'
    s += '  100106     2  -6.55     -106 107 -24            u=100 $ Bottom Plug\n'
    s += '  100107     3  -0.777537  104                    u=100 $ Water Above Plug\n'
    s += '  100108     3  -0.777537 -104 103 23             u=100 $ Water RadiallyTop\n'
    s += '  100109     3  -0.777537 -107                    u=100 $ Water Below pin\n'
    s += '  100110     3  -0.777537  107 -106 24            u=100 $ Water RadiallyBottom\n'
    s += '  100111     3  -0.777537 -102 105 22             u=100 $ Water Around pin\n'
    s += 'c ******************************************************************************\n'

    u = 101
    ID = 100200


    for index, x_i in enumerate(x_l):
        y_i = y_l[index]

        for ind, x_it in enumerate(x_i):
            y_it = y_i[ind]

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
    s += '  30    cz 40                          $ Water boundary\n'
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
    s += 'c ROD SURFACES\n'
    s += 'c ***************************************************************\n'
    s += ' 11000         pz 126.8     $  Top of Fuel Rod\n' \
        ' 22000         pz -126.8    $  Bottom of Fuel Rod\n'
    s += 'c ***************************************************************\n'
    s += 'c Hexagonal SURFACES ALL FUEL ASSEMBLY DEFS\n'
    s += 'c ***************************************************************\n'



    s += 'c ==============================================================================\n'
    s += 'c Cylinders for core boundaries \n'
    s += '  305   cz 40                          $ Water boundary\n'
    s += 'c ==============================================================================\n'
    s += 'c Planes for core boundaries\n'
    s += '  505   pz     926.8                   $ Water top\n'
    s += '  515   pz    -226.8                   $ Water bottom\n'
    s += 'c ==============================================================================\n'
    s += 'c Planes fro hexagonal cells\n'
    s += '  701         p -0.86602540378444 0 0.49999999999999 14.5 \n'
    s += '  702         p -1.0713652187633e-014 0 1 -1.8467333635044e-014\n'
    s += '  703         p 0.86602540378443 0 0.50000000000001 -7.25\n'
    s += '  704         p 0.86602540378444 0 -0.49999999999999 9.7699626167014e-015\n'
    s += '  705         p 1.1879386363489e-014 0 -1 14.5\n'
    s += '  706         p -0.86602540378443 0 -0.50000000000001 21.75\n'
    s += '  707         p -8.0491169285324e-015 0 1 14.5\n'
    s += '  708         p 0.86602540378443 0 0.50000000000001 -1.8651746813703e-014\n'
    s += '  709         p 0.86602540378444 0 -0.49999999999999 -7.25\n'
    s += '  710         p 8.7707618945387e-015 0 -1 8.1704531989996e-015\n'
    s += '  711         p -0.86602540378443 0 -0.50000000000001 14.5\n'
    s += '  712         p -0.86602540378444 0 0.49999999999999 21.75\n'
    s += '  713         p 0.86602540378444 0 0.5 14.5\n'
    s += '  714         p 0.86602540378444 0 -0.5 -1.8651746813703e-014\n'
    s += '  715         p -4.9731793613368e-016 0 -1 -7.25\n'
    s += '  716         p -0.86602540378444 0 -0.5 7.105427357601e-015\n'
    s += '  717         p -0.86602540378444 0 0.5 14.5\n'
    s += '  718         p 0 0 1 21.75\n'
    s += '  719         p 0.86602540378444 0 -0.5 14.5\n'
    s += '  720         p 3.663735981263e-015 0 -1 -1.852483103461e-014\n'
    s += '  721         p -0.86602540378444 0 -0.5 -7.25\n'
    s += '  722         p -0.86602540378444 0 0.5 8.8817841970013e-015\n'
    s += '  723         p -4.8294701571194e-015 0 1 14.5\n'
    s += '  724         p 0.86602540378444 0 0.5 21.75\n'
    s += '  725         p 1.0547118733939e-015 0 -1 14.5\n'
    s += '  726         p -0.86602540378444 0 -0.5 -1.6875389974302e-014\n'
    s += '  727         p -0.86602540378444 0 0.5 -7.25\n'
    s += '  728         p -1.7763568394003e-015 0 1 8.9186554055332e-015\n'
    s += '  729         p 0.86602540378444 0 0.5 14.5\n'
    s += '  730         p 0.86602540378444 0 -0.5 21.75\n'
    s += '  731         p -0.86602540378444 0 -0.5 14.5\n'
    s += '  732         p -0.86602540378444 0 0.5 -1.8651746813703e-014\n'
    s += '  733         p 4.9731793613368e-016 0 1 -7.25\n'
    s += '  734         p 0.86602540378444 0 0.5 7.105427357601e-015\n'
    s += '  735         p 0.86602540378444 0 -0.5 14.5\n'
    s += '  736         p 0 0 -1 21.75\n'
    s += '  737         p -0.86602540378444 0 -0.5 7.25\n'
    s += '  738         p -0.86602540378444 0 0.5 7.25\n'
    s += '  739         p 4.9731793613368e-016 0 1 7.25\n'
    s += '  740         p 0.86602540378444 0 0.5 7.25\n'
    s += '  741         p 0.86602540378444 0 -0.5 7.25\n'
    s += '  742         p 0 0 -1 7.25\n'






    for index, x_i in enumerate(x_l):
        y_i = y_l[index]

        for i, x_it in enumerate(x_i):
            y_it = y_i[i]

            assembly_ID = index + 1
            rod_ID = i + 1

            ID = assembly_ID * 10000 + rod_ID

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
    s_prime += 'c Flux average tally for active fuel region of all 85 elements\n'
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
    s+= 'si2 0 15            $ radius of the active region\n'
    s+= 'si3 -125.7 116.8    $ height of the active region\n'

    return s

def write_imp():

    s = 'c ***************************************************************\n'
    s += 'imp:n             0            1        11567r       $\n'
    return s


def write_kcode_ect():
    s = 'c ***************************************************************\n'
    s += 'mode  n\n'
    s += 'kcode 100000 1.500000 30 250 300000\n'
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
    #s+= 'c Water around core\n'
    #s+= '  1     0       -30 -50 51             $ Water in core\n'
    #s+= '  2     0       -300                   $ Center FA\n'
    #s+= '  3     0       -301                   $ Top middle FA\n'
    #s+= '  4     0       -302                   $ Top left FA\n'
    #s+= '  5     0       -303                   $ Top right FA\n'
    #s+= '  6     0       -304                   $ Bot middle FA\n'
    #s+= '  7     0       -305                   $ Bot left FA\n'
    #s+= '  8     0       -306                   $ Bot right FA\n'
    s+= 'c Planes for hexagonal cells\n'
    s+= '  9      0 fill=7  (-701 -702 -703 -704 -705 -706 ) $ bottom left\n'
    s+= '  10     0 fill=5  (-707 -708 -709 702 -711 -712 ) $ upper left\n'
    s+= '  11     0 fill=3  (-713 -704 -715 708 -701 -718 ) $ top mid\n'
    s+= '  12     0 fill=4  (-719 702 -721 704 -707 -724 ) $ top right\n'
    s+= '  13     0 fill=6  (-705 708 -727 -702 -713 -730 ) $ bottom right\n'
    s+= '  14     0 fill=2  (-711 704 -733 -708 -719 -736 ) $ bottom mid\n'
    s+= '  15     0 fill=1  (703 709 715 721 727 733 ) $ center\n'
    s+= '  16     0 fill=8  (701 :702 :703 :704 :705 :706 )\n'
    s+= '     (707 :708 :709 :-702 :711 :712)(713 :704 :715 :-708 :701 :718 )\n'
    s+= '     (719 :-702 :721 :-704 :707 :724 )(705 :-708 :727 :702 :713 :730)\n'
    s+= '     (711 :-704 :733 :708 :719 :736 )(-703 :-709 :-715 :-721 :-727 :-733 ) $CR\n'
   #TODO FIX THIS s+= '    1     0       -30 -40 41             $ Water in core \n'
    #s+= '    2     0       -300          fill=1   $ Center FA\n'
    #s+= '    3     0       -301          fill=2   $ Top middle FA\n'
    #s+= '    4     0       -302          fill=3   $ Top left FA\n'
    #s+= '    5     0       -303          fill=4   $ Top right FA\n'
    #s+= '    6     0       -304          fill=5   $ Bot middle FA\n'
    #s+= '    7     0       -305          fill=6   $ Bot left FA\n'
    #s+= '    8     0       -306          fill=7   $ Bot right FA\n'


    return s

def write_core_water_cell(x_l, y_l):
    s = '-0.777537  '
    cnt = 2
    for index, x_i in enumerate(x_l):
        y_i = y_l[index]

        for i, x_it in enumerate(x_i):
            y_it = y_i[i]

            assembly_ID = index + 1
            rod_ID = i + 1

            ID = assembly_ID * 10000 + rod_ID
            cnt += 1

            if cnt == 10:
                s += '\n             '
                cnt = 0
            s += str(ID) + ' '

    s_prime = 'c**********************************************************************\n'
    s_prime += 'c Water around core\n'
    s_prime += 'c**********************************************************************\n'
    s_prime += '  666     3   '+ s + ' u=8 \n'

    return s_prime

def write_file(outputName, s):

    with open(outputName if outputName else 'hex.i', 'w') as f:
        f.write(s)


def form_string():
    x_l, y_l = get_all_rod_pos()
    s = write_intro_mat()
    s += 'c\n'
    s += write_main_cells()
    s += write_fuel_universes(x_l, y_l)
    s += 'c\n'
#TODO REIMPLIMENT    s += write_core_water_cell(x_l, y_l)
    s += fill_rod_position()
    s += '\n'
    s += write_rod_surfaces(x_l, y_l)
    s+= '\n'
    s += write_kcode_ect()
    s += write_materials()
    s += write_imp()
    s += write_sdef()
    s += write_tallys(x_l, y_l)

    return s



if __name__ == '__main__':
    write_file(outputName = 'test.i', s =form_string())