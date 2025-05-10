import numpy as np

W = np.diag([9.605842129, 2.186674014, 3.201947376])
X = ([6.00,1],
     [8.00,1],
     [10.00,1])
Y = ([3.17E-05],
     [7.28E-05],
     [9.51E-05])

Mβ = np.linalg.inv(np.transpose(X) @ W @ X )
β = Mβ @ np.transpose(X) @ W @ Y

print(β)
print(np.sqrt(np.diagonal(Mβ)))

#imprimeix uns valors: [m, n] i [u_m, u_n]
#[[ 1.62857581e-05] [-6.51430322e-05]][0.15754156 1.1550062 ]