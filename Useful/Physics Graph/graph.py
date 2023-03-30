import matplotlib.pyplot as plt
import numpy as np

def create_scatter_plot_with_best_fit_line(x_values, y_values):
    plt.scatter(x_values, y_values, label='Data Points')
    
    #gradient
    min_index = np.argmin(x_values)
    max_index = np.argmax(x_values)
    x1, y1 = x_values[min_index], y_values[min_index]
    x2, y2 = x_values[max_index], y_values[max_index]
    gradient = (y2 - y1) / (x2 - x1)
    y_intercept = y1 - gradient * x1
    print(f"Gradient: {gradient}, Y-Intercept: {y_intercept}")

    #lobf
    best_fit_line = [gradient * x + y_intercept for x in x_values]
    plt.plot(x_values, best_fit_line, label='Best Fit Line', color='red')

    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.title('title')
    plt.legend()
    plt.show()

#these values are from an Ohm's law experiment
x_values = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y_values = [0.28, 0.56, 0.81, 1.08, 1.34, 1.63, 1.86, 2.13, 2.40, 2.61]

create_scatter_plot_with_best_fit_line(x_values, y_values)
