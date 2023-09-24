import numpy as np
import matplotlib.pyplot as plt
a = 4E-6
upper_bound = 4 * a  # Substrate to waveguide: a, waveguide: 2a, waveguide to cladding: 2a
n1 = 1.516
ns = 1
n0 = 1
N = 120000 # It's better to be multiplies of 4
points = np.linspace(0, upper_bound, N)
step = upper_bound / N  # Delta_x
lambda1 = 1.55E-6
k = 2 * np.pi / lambda1
# Define the refractive index in each layer
refractive_index = []
for i in range(int(N / 4)):
    refractive_index.append(ns)
for i in range(int(N / 4) ,int(3 * N / 4)):
    refractive_index.append(n1)
for i in range(int(3 * N / 4) ,int(N)):
    refractive_index.append(n0)

refractive_index = np.array(refractive_index)
mu_n = (k ** 2) * (refractive_index ** 2) * (step ** 2) - 2
array = np.zeros((N,N))
for i in range(N):
    if (i == 0):
        array[0][0] = mu_n[0] / (step ** 2)
        array[0][1] = 1 / (step ** 2)
    elif (i == (N - 1)):
        array[i][i] = mu_n[i] / (step ** 2)
        array[i][i - 1] = 1 / (step ** 2)
    else:
        array[i][i - 1] = 1 / (step ** 2)
        array[i][i] = mu_n[i] / (step ** 2)
        array[i][i + 1] = 1 / (step ** 2)
eigenvalues, eigenvectors = np.linalg.eig(array)
filter = eigenvalues >= 0
eigenvalues = eigenvalues[filter]
eigenvectors = eigenvectors[filter]
effective_refractive_index = np.sqrt(eigenvalues) / k
filter = effective_refractive_index <= n1
eigenvectors = eigenvectors[filter]
effective_refractive_index = effective_refractive_index[filter]
filter = effective_refractive_index >= ns
eigenvectors = eigenvectors[filter]
effective_refractive_index = effective_refractive_index[filter]
beta = [round(number * k, 3) for number in effective_refractive_index]
print(beta)

