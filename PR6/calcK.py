import numpy as np

W = np.diag([50000000 ,25000000, 16666666.67, 12500000, 10000000])
X = ([0.0001,1]
     [0.0004,1],
     [0.0009,1],
     [0.0016,1],
     [0.0025,1],)
Y = ([0],
     [0.000204082],
     [0.001020408],
     [0.002142857],
     [0.003265306])

Mβ = np.linalg.inv(np.transpose(X) @ W @ X )
β = Mβ @ np.transpose(X) @ W @ Y

print(β)
print(np.sqrt(np.diagonal(Mβ)))

#imprimeix uns valors: [m, n] i [u_m, u_n]
#
