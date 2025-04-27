import numpy as np

W = np.diag([2.5E+05, 2.5E+05, 2.5E+05, 2.5E+05, 2.5E+05])
X = ([17,1],
     [31,1],
     [45,1],
     [58,1],
     [69,1])
Y = ([4.90E-05],
     [9.81E-05],
     [1.47E-04],
     [1.96E-04],
     [2.45E-04])

Mβ = np.linalg.inv(np.transpose(X) @ W @ X )
β = Mβ @ np.transpose(X) @ W @ Y

print(β)
print(np.sqrt(np.diagonal(Mβ)))

#imprimeix uns valors: [m, n] i [u_m, u_n]
#
