import numpy as np
import matplotlib.pyplot as plt

amplitude = 1.0
frequency = 1.0
wavelength = 2.0 * np.pi / frequency
speed = 1.0

x_start = 0.0
x_end = 10.0
num_points = 500
x = np.linspace(x_start, x_end, num_points)

phase_difference = np.pi / 2.0
wave_1 = amplitude * np.sin((2.0 * np.pi * x/wavelength) - phase_difference)
wave_2 = amplitude * np.sin((2.0 * np.pi * x/wavelength) + phase_difference)

interference = wave_1 + wave_2

x_ticks = np.linspace(0, 10, 11)
x_ticklabels = [r'$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$', r'$\frac{5\pi}{2}$', r'$3\pi$', r'$\frac{7\pi}{2}$', r'$4\pi$', r'$\frac{9\pi}{2}$', r'$5\pi$']

plt.plot(x*wavelength, wave_1, label='Wave 1')
plt.plot(x*wavelength, wave_2, label='Wave 2')
plt.plot(x*wavelength, interference, label='Interference')
plt.xticks(x_ticks * np.pi, x_ticklabels)
plt.xlabel(r'x ($\pi$)')
plt.legend()
plt.draw()

def on_key_press(event):
    global phase_difference, wave_1, wave_2, interference
    if event.key == 'left':
        phase_difference -= np.pi / 50.0
    elif event.key == 'right':
        phase_difference += np.pi / 50.0
    elif event.key == 'q' or event.key == 'Q':
        plt.close()
    wave_1 = amplitude * np.sin((2.0 * np.pi * x/wavelength) - phase_difference)
    wave_2 = amplitude * np.sin((2.0 * np.pi * x/wavelength) + phase_difference)
    interference = wave_1 + wave_2
    plt.clf()
    plt.plot(x*wavelength, wave_1, label='Wave 1')
    plt.plot(x*wavelength, wave_2, label='Wave 2')
    plt.plot(x*wavelength, interference, label='Interference')
    plt.xticks(x_ticks * np.pi, x_ticklabels)
    plt.xlabel(r'x ($\pi$)')
    plt.legend()
    plt.draw()

fig = plt.gcf()
fig.canvas.mpl_connect('key_press_event', on_key_press)

print('Use the arrow keys to adjust phase difference. Press Q to quit.')
while True:
    plt.pause(0.001)
    if not plt.fignum_exists(fig.number):
        break

plt.close()
