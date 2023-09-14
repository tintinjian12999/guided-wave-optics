
import numpy as np
import matplotlib.pyplot as plt
n1 = 1.516
n0 = 1
a = 4E-6
lambda1 = 1.55E-6
k = 2 * np.pi / lambda1
interval_num = 0
interval = lambda1 / (4 * n1 * a)  #This is the interval for each tan function
delta = (n1 ** 2 - n0 ** 2) / (2 * n1 ** 2) 
while (interval_num * interval < np.sqrt(delta * 2)):
    interval_num += 1 
def func_left (x, m):  #Here x = sin(phi) in the dispersion equ (1.14)
    return np.tan(k * n1 * a *  x - (m * np.pi) / 2)
def func_right (x):
    return np.sqrt((2 * delta / (x ** 2)) - 1)
points = np.arange(0, interval, 1E-8)
result_left = []
result_right = []
intersection_y = []
intersection_x = []
for i in range(interval_num):
    result_left.append(func_left(points + i * interval, i))
    result_right.append(func_right(points + i * interval))
    for idx in range(len(result_left[i])): #Find intersection
        if (abs(result_left[i][idx] - result_right[i][idx]) < 1e-4):
            intersection_y.append(result_left[i][idx])
            intersection_x.append(points[idx] + i * interval)
            break
    plt.scatter(np.array(intersection_x[i]), np.array(intersection_y[i]), c = 'r')
    plt.axvline(x = interval * (i + 1), color='red', linestyle='--')
    #plt.scatter(np.array(points + i * interval), np.array(result_left[i]))
    #plt.scatter(np.array(points + i * interval), np.array(result_right[i]))
    plt.plot(points + i * interval, func_left(points + i * interval, i), 'k')
    plt.plot(points + i * interval, func_right(points + i * interval), 'k')
print(intersection_x)
plt.xlim([0, interval * interval_num])
plt.ylim([0, 15])
plt.xlabel(r"sin $\phi$")
plt.show()
