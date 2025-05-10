import numpy as np

W = np.diag([213800.6473, 135846.6994, 184788.3589, 143422.5])
X = ([17.92111111,1],
     [27.7729,1],
     [40.3225,1],
     [59.23867778,1])
Y = ([9.80665E-05],
     [0.00014715],
     [0.000196133],
     [0.000245166])

Mβ = np.linalg.inv(np.transpose(X) @ W @ X )
β = Mβ @ np.transpose(X) @ W @ Y

print(β)
print(np.sqrt(np.diagonal(Mβ)))

#imprimeix uns valors: [m, n] i [u_m, u_n]
#[[4.04546663e-06] [2.13663461e-05]][4.40545408e-05 9.60557680e-04]

#amb un punt eliminat
#[[3.59551654e-06] [4.08366356e-05]][7.93271687e-05 3.01192277e-03]