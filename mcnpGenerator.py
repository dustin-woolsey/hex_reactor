import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos, linspace, array, pi







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