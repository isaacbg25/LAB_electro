import numpy as np

W = np.diag([81.64965809, 42.64014327, 81.64965809])
X = ([6.00,1],
     [8.00,1],
     [10.00,1])
Y = ([8.5],
     [19.5],
     [25.5])

Mβ = np.linalg.inv(np.transpose(X) @ W @ X )
β = Mβ @ np.transpose(X) @ W @ Y

print(β)
print(np.sqrt(np.diagonal(Mβ)))

#imprimeix uns valors: [m, n] i [u_m, u_n]
#



