import numpy as np

W = np.diag([1.2E+03, 5.4E+03, 8.4E+03, 1.8E+04])
X = ([250,1],
     [167,1],
     [125,1],
     [100,1])
Y = ([0.000231336],
     [0.000177233],
     [0.000149249],
     [0.000113802])

Mβ = np.linalg.inv(np.transpose(X) @ W @ X )
β = Mβ @ np.transpose(X) @ W @ Y

print(β)
print(np.sqrt(np.diagonal(Mβ)))

#imprimeix uns valors: [m, n] i [u_m, u_n]
#[[8.95251078e-07] [2.72168230e-05]][ 0.50592093 61.55581049]

#[8.57383097e-07] [3.22073990e-05]][0.00015939 0.02032939]