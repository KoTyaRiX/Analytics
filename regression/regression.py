import numpy as np
from scipy.optimize import minimize

# Define the sinusoidal function
def sinusoidal(x, a, b, c, d):
    return a * np.sin(b * x + c) + d

# Define the sum of squared distances
def objective(params, x, y):
    return np.sum((sinusoidal(x, *params) - y) ** 2)

# Generate some example data points
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(3*x + 1) + np.random.normal(0, 0.1, len(x))

# Perform the optimization
initial_guess = [1, 1, 0, 0]
result = minimize(objective, initial_guess, args=(x, y))

# Print the optimal parameters
print(result.x)

# Plot the results
import matplotlib.pyplot as plt
new_x = np.linspace(0, 20, 1000)
plt.xlim([0, 20])
plt.scatter(x, y)
plt.plot(new_x, sinusoidal(new_x, *result.x), 'r')
plt.show()
