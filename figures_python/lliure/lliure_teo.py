import matplotlib.pyplot as plt
import numpy as np


nx, ny = 132, 132
V = np.zeros((ny, nx))
fixed = np.zeros_like(V, dtype=bool)  # Nova màscara de punts fixos

l1 = int(1.35*132/28)
l2 = int(3*132/28)
l = int(7.8*132/28)
e = 0#int((8*132/28) - l)
g = int(1*132/28)

# Assignem valors i marquem com fixos
V[int(ny/2+e):int(ny/2+e+l), int(nx/2 - l1-g):int(nx/2 - l1)] = 7.5
fixed[int(ny/2+e):int(ny/2+e+l), int(nx/2 - l1-g):int(nx/2 - l1)] = True

V[int(ny/2-e-l):int(ny/2-e), int(nx/2 - l1-g):int(nx/2 - l1)] = 7.5
fixed[int(ny/2-e-l):int(ny/2-e), int(nx/2 - l1-g):int(nx/2 - l1)] = True

V[int(ny/2-g//2):int(ny/2+g//2), int(nx/2 + l2-g//2):int(nx/2 + l2+g//2)] = -7.5
fixed[int(ny/2-g//2):int(ny/2+g//2), int(nx/2 + l2-g//2):int(nx/2 + l2+g//2)] = True
print(int(ny/2-e-l),int(ny/2-e), int(nx/2 - l1-g))
# Iteració per resoldre Laplace (mètode de Jacobi)
for _ in range(6000):
    V_new = V.copy()
    V_new[1:-1,1:-1] = 0.25 * (V[1:-1, :-2] + V[1:-1, 2:] + V[:-2, 1:-1] + V[2:, 1:-1])
    
    # Els punts fixos NO es toquen
    V_new[fixed] = V[fixed]
    
    V = V_new

# Dibuixem el resultat
plt.contour(V, levels=[7.4], colors='k')
plt.title("Línies equipotencials (condensador no ideal - correció)")
plt.gca().set_aspect('equal')
#plt.show()


#V[0,:]=100
#V[:,0]=100
#V[90:99,:]=0.1
#V[:,90:99]=0.1

# Dibuixa les línies equipotencials
nivells = [0,3,6,7.5,10,12,14.99]
nivells = [(x-7.5) for x in nivells] 
nivells =[-7.5,-7.49,7.49,7.5] # Potencials concrets que vols mostrar
#print(nivells)

x = np.linspace(0, 27, nx)  # coordenades x
y = np.linspace(0, 27, ny)  # coordenades y
X, Y = np.meshgrid(x, y)
ny, nx = V.shape


# Aplanem les dades, les posem per columnes i canviem el centre de coordenades
dades = np.column_stack((X.ravel()-13.5, Y.ravel()-13.5, V.ravel()))

# Guardem com a txt: una fila = x y v
np.savetxt("lliure_teo_0.txt", dades, fmt="%.6f", header="x y V", comments='')
