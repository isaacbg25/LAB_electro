import numpy as np

W = np.diag([256000000, 85333333.33, 42666666.67, 21333333.33, 17066666.67])
X = ([0.0001,1],
     [0.0004,1],
     [0.0009,1],
     [0.0016,1],
     [0.0025,1])
Y = ([0],
     [0.000135],
     [0.000625],
     [0.00171875],
     [0.00234375])

Mβ = np.linalg.inv(np.transpose(X) @ W @ X )
β = Mβ @ np.transpose(X) @ W @ Y

print(β)
print(np.sqrt(np.diagonal(Mβ)))