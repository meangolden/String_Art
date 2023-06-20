# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 13:34:41 2021
Author: chrys

Suspension Bridge String Art

This code generates a string art pattern resembling a suspension bridge. It uses the 'put_strings_btw_lines' function to connect points between two lines, creating an intricate design. The pattern is saved as a PDF file named 'bloooha.pdf'.

"""

import numpy as np
import matplotlib.pyplot as plt


def put_strings_btw_lines(AB, CD, no_pins, clr='black'):
    '''
    AB: vector of two points: start point and end point. Determines a line.
    CD: similar.
    no_pins: the number of pins across each line.
    clr: color of the strings (default: black).

    Description: connects the ith point of AB with the (no_pins-i)th point of CD.
    '''
    A, B, C, D = AB[0], AB[1], CD[0], CD[1]
    ABxs = np.linspace(A[0], B[0], no_pins)
    ABys = np.linspace(A[1], B[1], no_pins)
    CDxs = np.linspace(D[0], C[0], no_pins)
    CDys = np.linspace(D[1], C[1], no_pins)
    plt.plot((ABxs, CDxs), (ABys, CDys), color=clr)


if __name__ == "__main__":
    # Define the points for the lines
    AB, CD = [[-6.5, 0], [-6.5, 1]], [[-6.5, 0], [6.5, 0]]
    EF, GH = [[6.5, 0], [6.5, 1]], [[6.5, 0], [-6.5, 0]]
    AB1, CD1 = [[-7, 0], [-7, 1]], [[-7, 0], [6, 0]]
    EF1, GH1 = [[6, 0], [6, 1]], [[6, 0], [-7, 0]]

    no_pins = 33
    plt.figure(figsize=(8, 1))
    put_strings_btw_lines(AB, CD, no_pins, 'gray')
    put_strings_btw_lines(EF, GH, no_pins, 'gray')
    put_strings_btw_lines(AB1, CD1, no_pins)
    put_strings_btw_lines(EF1, GH1, no_pins)
    plt.savefig("daves_present.pdf")
    plt.show()
