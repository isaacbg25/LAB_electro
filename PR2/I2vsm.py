import numpy as np

W = np.diag([21484067.91, 2965136.488, 1884016.771, 2562773.838, 1989083.269])
X = ([7.254044444,1],
     [17.92111111,1],
     [27.7729,1],
     [40.3225,1],
     [59.23867778,1])
Y = ([0.000005],
     [0.00001],
     [0.000015],
     [0.00002],
     [0.000025])

Mβ = np.linalg.inv(np.transpose(X) @ W @ X )
β = Mβ @ np.transpose(X) @ W @ Y

print(β)
print(np.sqrt(np.diagonal(Mβ)))

#imprimeix uns valors: [m, n] i [u_m, u_n]
# 
