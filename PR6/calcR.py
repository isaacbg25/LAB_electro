import numpy as np

W = np.diag([12499722.23, 8308241.358, 6226659.182, 4977745.027, 4142675.376])
X = ([0.000400018,1],
     [0.000905444,1],
     [0.001612018,1],
     [0.002522404,1],
     [0.003641818,1])
Y = ([0.000266667],
     [0.004666667],
     [0.006933333],
     [0.009466667],
     [0.012933333])

Mβ = np.linalg.inv(np.transpose(X) @ W @ X )
β = Mβ @ np.transpose(X) @ W @ Y

print(β)
print(np.sqrt(np.diagonal(Mβ)))

#imprimeix uns valors: [m, n] i [u_m, u_n]
#













