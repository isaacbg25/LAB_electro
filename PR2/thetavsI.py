import numpy as np

W = np.diag([6.804138174, 2.665008954, 4.082482905])
X = ([36,1],
     [64,1],
     [100,1])
Y = ([8.5],
     [19.5],
     [25.5])

Mβ = np.linalg.inv(np.transpose(X) @ W @ X )
β = Mβ @ np.transpose(X) @ W @ Y

print(β)
print(np.sqrt(np.diagonal(Mβ)))







