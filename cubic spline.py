import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import math

def funct(values):
    return [np.sin(np.cos(value)) for value in values]

def calculate_fault(xo, yo, yr, start, end, size):
    arrSize = len(yo)
    step = int(arrSize / size)
    fault = sum(abs(yo[step: arrSize - step + 1: step] - yr[step:arrSize - step + 1:step]))
    ys = cs(xs)
    yf = funct(xs)
    fault = calculate_fault(xs, yf, ys, start, end, size)
    return fault

if __name__ == '__main__':

    start = -5
    end = 5
    size = 4

    x = np.linspace(start, end, size)
    y = funct(x)
    plt.plot(x, y, 'o', label='knot',color="red")

    cs = interpolate.CubicSpline(x, y)
    xs = np.arange(start, end, 0.01)

    plt.plot(xs, funct(xs), label='f(x)')
    plt.plot(xs, cs(xs), '--', label="interpolate")

    ys = cs(xs)
    yf = funct(xs)
    # fault = calculate_fault(xs, yf, ys, start, end, size)
    
    for i in range(size - 1):
        coeff = [x[i] for x in cs.c]
        print(str(i + 1) + '. ' + str(coeff))

    # plt.text(end-3, -1, "fault {}".format(round(fault, 4)), fontsize=14)
    plt.legend()
    plt.title('Cubic-spline interpolation')
    plt.show()
