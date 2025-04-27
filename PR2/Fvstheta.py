import numpy as np

W = np.diag([7497.913331, 4111.758923, 2832.545036, 2197.664252, 1847.31198])
X = ([289,1],
     [961,1],
     [2025,1],
     [3364,1],
     [4761,1])
Y = ([4.90E-05],
     [9.81E-05],
     [1.47E-04],
     [1.96E-04],
     [2.45E-04])

Mβ = np.linalg.inv(np.transpose(X) @ W @ X )
β = Mβ @ np.transpose(X) @ W @ Y

print(β)
print(np.sqrt(np.diagonal(Mβ)))





