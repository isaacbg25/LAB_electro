import numpy as np
import matplotlib.pyplot as plt

# Dimensions de la malla
nx, ny = 132, 132
V = np.zeros((ny, nx))
d = 15
l = 40

# Condicions de contorn (dos rectangles com plaques)
V[int(ny/2-l/2):int(ny/2+l/2), int(nx/2 - d/2):int(nx/2 - d/2)+2] = 7.5  # placa esquerra
V[int(ny/2-l/2):int(ny/2+l/2), int(nx/2 + d/2):int(nx/2 + d/2)+2] = -7.5    # placa dreta

# Iteració per resoldre Laplace (mètode de Jacobi)
for _ in range(6000):
    V_new = V.copy()
    V_new[1:-1,1:-1] = 0.25 * (V[1:-1, :-2] + V[1:-1, 2:] + V[:-2, 1:-1] + V[2:, 1:-1])
    
    # Reaplica condicions de contorn a la nova matriu
    V_new[int(ny/2-l/2):int(ny/2+l/2), int(nx/2 - d/2):int(nx/2 - d/2)+2] = 7.5
    V_new[int(ny/2-l/2):int(ny/2+l/2), int(nx/2 + d/2):int(nx/2 + d/2)+2] = -7.5
    
    V = V_new

px1=int((-4.11+13.5)*132/28)
py1=int((-0.91+13.5)*132/28)
v1=6
px2=int((7.58175+13.5)*132/28)
py2=int((3.7608695652+13.5)*132/28)
v2=-4.5
px3=int((9.56+13.5)*132/28)
py3=int((0.13+13.5)*132/28)
v3=-4.5


"""
# Dibuixa les línies equipotencials
nivells = [6]
nivells = [6]  # Potencials concrets que vols mostrar
plt.contour(V, levels=nivells, colors='k')  # 'k' = negre
plt.scatter(px1,py1)
plt.title("Línies equipotencials (condensador no ideal)")
plt.gca().set_aspect('equal')
plt.show()
"""
e=np.average([(V[py1,px1]-7.5)/(v1-7.5),(V[py2,px2]+7.5)/(v2+7.5),(V[py3,px3]+7.5)/(v3+7.5)])
u=np.var([(V[py1,px1]-7.5)/(v1-7.5),(V[py2,px2]+7.5)/(v2+7.5),(V[py3,px3]+7.5)/(v3+7.5)])
print(e,u)

"""
x = np.linspace(0, 27, nx)  # coordenades x
y = np.linspace(0, 27, ny)  # coordenades y
X, Y = np.meshgrid(x, y)
ny, nx = V.shape


# Aplanem les dades, les posem per columnes i canviem el centre de coordenades
dades = np.column_stack((X.ravel()-13.5, Y.ravel()-13.5, V.ravel()))

# Guardem com a txt: una fila = x y v
#np.savetxt("cond_teo_prova.txt", dades, fmt="%.6f", header="x y V", comments='')

"""