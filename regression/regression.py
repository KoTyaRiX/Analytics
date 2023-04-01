import numpy as np
from scipy.optimize import minimize
import analize.Main

# Define the sinusoidal function
def sinusoidal(x, a, b, c, d):
    return a * np.sin(b * x + c) + d


def sinusoidal_function(a, b, c, d):
    return lambda x: a * np.sin(b * x + c) + d


# Define the sum of squared distances
def objective(params, x, y):
    return np.sum((sinusoidal(x, *params) - y) ** 2)


def get_sinusoidal_regression(x, y):
    # Perform the optimization
    initial_guess = [1, 1, 0, 0]
    result = minimize(objective, initial_guess, args=(x, y))
    return sinusoidal_function(*result.x)


def get_polinomial_regression(x, y, deg=3):
    # Fit a polynomial of degree 2 to the data
    p = np.polyfit(x, y, deg=deg)
    # Create a function for the polynomial
    f = np.poly1d(p)
    return f


def getJsonFromFunction(x, y, from_time, to_time, display=False):
    f = get_sinusoidal_regression(x, y)
    xx = np.linspace(from_time, to_time)
    yy = f(xx)
    if display:
        plt.xlim([from_time, to_time])
        plt.scatter(xx, yy)
        plt.plot(xx, yy, 'r')
        plt.show()
    return xx, yy


# Generate some example data points
x = np.linspace(0, 2 * np.pi, 100)
y = 5 + np.sin(3 * x + 3) + np.random.normal(0, 2, len(x))

ff = get_sinusoidal_regression(x, y)
f = get_polinomial_regression(x, y)

# Plot the results
import matplotlib.pyplot as plt
#
# x_max = 10
# new_x = np.linspace(0, x_max, 1000)
# plt.xlim([0, x_max])
# plt.scatter(x, y)
# plt.plot(new_x, ff(new_x), 'r')
# plt.plot(new_x, f(new_x))
# plt.show()

