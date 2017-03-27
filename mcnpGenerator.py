import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos, linspace, array, pi


letter = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7}


def get_assembly_rod_pos(n_rings, fuel_pitch):
    '''

    :param n_rings:  number of rings
    :param fuel_pitch: center to center distance of individual fuel elements
    :return: central rod positions
    '''

    x = [0]
    y = [0]



    for ring in range(n_rings):



        if ring == 0:
            pass                # Center position is already generated

        else:

            #Generate elements along symmetry lines
            x.append(fuel_pitch * n_rings)
            y.append(0)

            x.append( - fuel_pitch * n_rings)
            y.append(0)

            x.append(cos(60) * fuel_pitch * n_rings)
            y.append(sin(60) * fuel_pitch * n_rings)

            x.append(-cos(60) * fuel_pitch * n_rings)
            y.append(sin(60) * fuel_pitch * n_rings)

            x.append(cos(60) * fuel_pitch * n_rings)
            y.append(-sin(60) * fuel_pitch * n_rings)

            x.append(-cos(60) * fuel_pitch * n_rings)
            y.append(-sin(60) * fuel_pitch * n_rings)

            #generate intermediate elements








    centers = []


    return centers



def write_file(outputName, s):

    with open(outputName if outputName else 'hex.i', 'w') as f:
             f.write(s)




if __name__ == '__main__':


    s_test = 'Lorem ipsum dolor sit amet, eu vix tamquam definitiones, ad mel eligendi postulant.' \
             ' \nVix ut mollis reprimique, ea vim habeo modus nonumes.' \
             ' \nEa eligendi copiosae vis.' \
             ' \nMolestie lobortis dignissim id eam, eum paulo quando primis ei.' \
             ' \nAt qui ocurreret prodesset posidonium, quo putant platonem ea.'

    write_file('test.i', s_test)