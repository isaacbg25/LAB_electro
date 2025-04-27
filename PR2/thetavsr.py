import numpy as np

W = np.diag([3.07745E-11, 4.61618E-11, 6.1549E-11, 7.69363E-11])
X = ([62500,1],
     [27777.77778,1],
     [15625,1],
     [10000,1])
Y = ([62.0],
     [47.5],
     [40.0],
     [30.5])

Mβ = np.linalg.inv(np.transpose(X) @ W @ X )
β = Mβ @ np.transpose(X) @ W @ Y

print(β)
print(np.sqrt(np.diagonal(Mβ)))

#imprimeix uns valors: [m, n] i [u_m, u_n]
#[[5.79704667e-04][2.80722442e+01]][3.90976893e+00 1.12561168e+05]
