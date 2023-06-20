# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 23:13:25 2021
Author: Chrys

Python script for generating a Circular Geometric String Art Pattern using matplotlib.

"""

import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def draw_string_art(r, noPins, n, threeD):
    X = [r * np.cos(angle) for angle in np.linspace(0, 2 * np.pi, noPins)]
    Y = [r * np.sin(angle) for angle in np.linspace(0, 2 * np.pi, noPins)]
    k = 0

    # For the pins around the frame
    sp = noPins // 4  # Number of pins at each side of the frame
    l = 4  # Length of each side
    Xsquare = np.concatenate((l * np.ones(sp), np.linspace(l, -l, sp), -l * np.ones(sp), np.linspace(-l, l, sp)))
    Ysquare = np.concatenate((np.linspace(-l, l, sp), l * np.ones(sp), np.linspace(l, -l, sp), -l * np.ones(sp)))

    fig = plt.figure()
    if threeD:
        ax = fig.add_subplot(111, projection='3d')
    else:
        ax = fig.add_subplot(111)

    for _ in range(2 * noPins):
        if _ % 5 == 0:
            k += 1

        x_values = [X[(_ + k) % noPins], X[(noPins // n + _) % noPins]]
        y_values = [Y[(_ + k) % noPins], Y[(noPins // n + _) % noPins]]
        z_values = [_, _]

        if threeD:
            ax.plot(x_values, y_values, z_values)
        else:
            ax.plot(y_values, x_values)
            ax.scatter(X[_ % noPins], Y[_ % noPins])

    if not threeD:
        rectangle = plt.Rectangle((-l, -l), 2 * l, 2 * l, fc='white', ec="white")
        ax.add_patch(rectangle)
        for i in range(noPins):
            x = [X[i], Xsquare[i]]
            y = [Y[i], Ysquare[i]]
            ax.plot(y, x, color='black')

        ax.set_xlim(-l, l)
        ax.set_ylim(-l, l)
        ax.axis('equal')

    if len(sys.argv) > 5 and sys.argv[5].lower() == 'true':
        if len(sys.argv) > 6:
            filename = sys.argv[6]
        else:
            filename = "2Dstring_art.png"
        plt.savefig(filename)

    plt.show()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        r = float(sys.argv[1])
    else:
        r = 2

    if len(sys.argv) > 2:
        noPins = int(sys.argv[2])
    else:
        noPins = 72

    if len(sys.argv) > 3:
        n = int(sys.argv[3])
    else:
        n = 2

    if len(sys.argv) > 4 and sys.argv[4].lower() == 'true':
        threeD = True
    else:
        threeD = False

    draw_string_art(r, noPins, n, True)