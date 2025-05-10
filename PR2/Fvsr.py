import numpy as np

W = np.diag([8.6E-05, 6.2E-04, 9.2E-04, 2.7E-03])
X = ([250,1],
     [167,1],
     [125,1],
     [100,1])
Y = ([0.000231336],
     [0.000177233],
     [0.000149249],
     [0.000113802])

Mβ = np.linalg.inv(np.transpose(X) @ W @ X )
β = Mβ @ np.transpose(X) @ W @ Y

print(β)
print(np.sqrt(np.diagonal(Mβ)))

#imprimeix uns valors: [m, n] i [u_m, u_n]
