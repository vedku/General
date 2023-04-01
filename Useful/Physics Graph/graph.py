import numpy as np
import matplotlib.pyplot as plt

def remove_outliers(x_values, y_values, threshold=2):
    xy_pairs = np.column_stack((x_values, y_values))
    mean_xy = np.mean(xy_pairs, axis=0)
    std_xy = np.std(xy_pairs, axis=0)
    z_scores = np.abs((xy_pairs - mean_xy) / std_xy)
    filtered_entries = (z_scores < threshold).all(axis=1)
    return xy_pairs[filtered_entries, 0], xy_pairs[filtered_entries, 1]

def graph(x_values, y_values):
    plt.scatter(x_values, y_values, label='Data Points')

    #removing anomalies
    x_values_filtered, y_values_filtered = remove_outliers(x_values, y_values)

    #gradient
    min_index = np.argmin(x_values_filtered)
    max_index = np.argmax(x_values_filtered)
    x1, y1 = x_values_filtered[min_index], y_values_filtered[min_index]
    x2, y2 = x_values_filtered[max_index], y_values_filtered[max_index]
    gradient = (y2 - y1) / (x2 - x1)
    y_intercept = y1 - gradient * x1
    print("Gradient:", gradient)
    print("Y-Intercept:", y_intercept)

    #lobf
    best_fit_line = [gradient * x + y_intercept for x in x_values]
    plt.plot(x_values, best_fit_line, label=f'(Gradient = {gradient:.3f}, Y-Intercept = {y_intercept:.3f})', color='red')

    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.title('title')
    plt.grid()
    plt.legend(loc="upper left") #feel free to change the location based on the correlation so it doesn't cover a point
    plt.show()

#changed the 700 y value to 2.3 to demonstrate how outliers are ignored
x_values = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y_values = [0.28, 0.56, 0.81, 1.08, 1.34, 2.3, 1.86, 2.13, 2.40, 2.61]

graph(x_values, y_values)
