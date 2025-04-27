import numpy as np

W = np.diag([0.005333333, 0.029393877, 0.036950417, 0.081649658])
X = ([250,1],
     [167,1],
     [125,1],
     [100,1])
Y = ([62.0],
     [47.5],
     [40.0],
     [30.5])

Mβ = np.linalg.inv(np.transpose(X) @ W @ X )
β = Mβ @ np.transpose(X) @ W @ Y

print(β)
print(np.sqrt(np.diagonal(Mβ)))

#imprimeix uns valors: [m, n] i [u_m, u_n]
#
