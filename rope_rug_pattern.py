import math
from math import sqrt
import matplotlib.pyplot as plt


def place_nails(num_nails):
    if num_nails < 4 or (num_nails - 2) % 4 != 0:
        print("Invalid number of nails. Please provide a number that is one more than a multiple of four.")
        return

    length = int((num_nails/2-1)/2 + 1)
    width = int(num_nails/2 - length)
    print(length)
    print(width)
    nails = []
    max_length = length + sqrt(2)/2
    max_width = width + sqrt(2)/2
    c = sqrt(2)/2

    for i in range(length):
        nails.append((i + c, 0))
    for i in range(width):
            nails.append((max_length , i + c))
    for i in range(length):
        nails.append((max_length +c - i, max_width))
    for i in range(width):
        nails.append((0 , max_width - i ))

    distances = []
    for i in range(len(nails) - 1):
        x1, y1 = nails[i]
        x2, y2 = nails[i + 1]
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        distances.append(distance)



    print(nails)
    print(distances)
    # Plotting
    plt.figure()
    plt.plot([nail[0] for nail in nails], [nail[1] for nail in nails], 'ro')
    #plt.plot([nails[-1][0], nails[0][0]], [nails[-1][1], nails[0][1]], 'r-')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Placement of Nails')
    plt.grid(True)
    plt.axis('equal')
    plt.show()


# Example usage
num_nails = 10#int(input("Enter the number of nails: "))
place_nails(num_nails)
