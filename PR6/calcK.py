import numpy as np

W = np.diag([25000000, 16666666.67, 12500000, 10000000, 8333333.333])
X = ([0.0004,1],
     [0.0009,1],
     [0.0016,1],
     [0.0025,1],
     [0.0036,1])
Y = ([0.000133333],
     [0.002333333],
     [0.003466667],
     [0.004733333],
     [0.006466667])

Mβ = np.linalg.inv(np.transpose(X) @ W @ X )
β = Mβ @ np.transpose(X) @ W @ Y

print(β)
print(np.sqrt(np.diagonal(Mβ)))

#imprimeix uns valors: [m, n] i [u_m, u_n]
#
