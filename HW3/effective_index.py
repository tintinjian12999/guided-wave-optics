import numpy as np
import math
from scipy.optimize import newton
def effective_index_TE(ns, na, nc, lambda0, s, d1):
    k0 = 2 * np.pi / lambda0
    d = np.linspace(d1, d1 + s, 1000)
    eff_idx = np.linspace(1, 10, 1000)
    phi = []
    psi = []
    func = []
    kappa = k0 * np.sqrt(nc ** 2 - eff_idx ** 2)
    sigma = k0 * np.sqrt(eff_idx ** 2 - ns ** 2)
    gamma = k0 * np.sqrt(eff_idx ** 2 - na ** 2)
    for i in range(len(sigma)):    
        phi.append(math.atan(sigma[i] / kappa[i]))
        psi.append(math.atanh(sigma[i] / gamma[i]))
    for i in range(len(d)):
        func.append([])
        for j in range(len(sigma)):
            func[i].append(math.sin(kappa[j] * d[i] - 2 * phi[j]) - math.sin(kappa[j] * d[i]) * math.exp(-2 * (sigma[j] * s + psi[j])))
    for i in range(len(d)):
        for j in range(len(sigma)):
            if (abs(func[i][j] - 0) < 1E-5):
                return eff_idx[j]

print(effective_index_TE(1.46, 1, 3.6, 1.55E-6, 2E-6, 1E-6))
