import numpy as np
import matplotlib.pyplot as plt

# Dimensions de la malla
nx, ny = 132, 132
V = np.zeros((ny, nx))
d = int(8*132/28)
l = int(1*132/28)

# Condicions de contorn (dos rectangles com plaques)
V[int(ny/2-l/2):int(ny/2+l/2), int(nx/2 - d/2):int(nx/2 - d/2)+l] = 7.5  # placa esquerra
V[int(ny/2-l/2):int(ny/2+l/2), int(nx/2 + d/2):int(nx/2 + d/2)+l] = -7.5    # placa dreta

# Iteració per resoldre Laplace (mètode de Jacobi)
for _ in range(6000):
    V_new = V.copy()
    V_new[1:-1,1:-1] = 0.25 * (V[1:-1, :-2] + V[1:-1, 2:] + V[:-2, 1:-1] + V[2:, 1:-1])
    
    # Reaplica condicions de contorn a la nova matriu
    V_new[int(ny/2-l/2):int(ny/2+l/2), int(nx/2 - d/2):int(nx/2 - d/2)+l] = 7.5
    V_new[int(ny/2-l/2):int(ny/2+l/2), int(nx/2 + d/2):int(nx/2 + d/2)+l] = -7.5
    
    V = V_new

#V[0,:]=100
#V[:,0]=100
#V[90:99,:]=0.1
#V[:,90:99]=0.1

# Dibuixa les línies equipotencials
nivells = [0,3,6,7.5,10,12,14.99]
nivells = [(x-7.5) for x in nivells]  # Potencials concrets que vols mostrar
plt.contour(V, levels=nivells, colors='k')  # 'k' = negre
plt.title("Línies equipotencials (condensador no ideal)")
plt.gca().set_aspect('equal')
#plt.show()
#print(nivells)

x = np.linspace(0, 27, nx)  # coordenades x
y = np.linspace(0, 27, ny)  # coordenades y
X, Y = np.meshgrid(x, y)
ny, nx = V.shape


# Aplanem les dades, les posem per columnes i canviem el centre de coordenades
dades = np.column_stack((X.ravel()-13.8, Y.ravel()-13.5, V.ravel()))

# Guardem com a txt: una fila = x y v
np.savetxt("fils_teo.txt", dades, fmt="%.6f", header="x y V", comments='')
