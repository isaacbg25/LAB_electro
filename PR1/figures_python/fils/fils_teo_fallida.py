import numpy as np
import matplotlib.pyplot as plt

# Dimensions de la malla
nx, ny = 132, 132
V = np.zeros((ny, nx))

#generem les condicions de contorn
xv=np.linspace(0,131,nx)
yv=np.linspace(0,131,ny)
Xv,Yv=np.meshgrid(xv,yv)
x_centre=10+14
y_centre=0+14
radi=5
dist=np.sqrt((Xv-x_centre)**2 +(Yv-y_centre)**2)
mask=dist <= radi
puntsx1=Xv[mask]
puntsy1=Yv[mask]

x_centre=-10+14
ist=np.sqrt((Xv-x_centre)**2 +(Yv-y_centre)**2)
mask=dist <= radi
puntsx2=Xv[mask]
puntsy2=Yv[mask]
# Condicions de contorn (dos rectangles com plaques)
V[puntsx1.astype(int),puntsy1.astype(int)] = 7.5  # placa esquerra
V[puntsx2.astype(int),puntsy2.astype(int)] = -7.5  

# Iteració per resoldre Laplace (mètode de Jacobi)
for _ in range(6000):
    V_new = V.copy()
    V_new[1:-1,1:-1] = 0.25 * (V[1:-1, :-2] + V[1:-1, 2:] + V[:-2, 1:-1] + V[2:, 1:-1])
    
    # Reaplica condicions de contorn a la nova matriu
    V[puntsx1.astype(int),puntsy1.astype(int)] = 7.5  # placa esquerra
    V[puntsx2.astype(int),puntsy2.astype(int)] = -7.5 
    
    V = V_new

#V[0,:]=100
#V[:,0]=100
#V[90:99,:]=0.1
#V[:,90:99]=0.1

# Dibuixa les línies equipotencials
nivells = [3,7.5,10,12]
nivells = [x-7.5 for x in nivells]  # Potencials concrets que vols mostrar
plt.contour(V, levels=6, colors='k')  # 'k' = negre
plt.title("Línies equipotencials (condensador no ideal)")
plt.gca().set_aspect('equal')
plt.show()
#print(nivells)

"""""
x = np.linspace(0, 27, nx)  # coordenades x
y = np.linspace(0, 27, ny)  # coordenades y
X, Y = np.meshgrid(x, y)
ny, nx = V.shape


# Aplanem les dades, les posem per columnes i canviem el centre de coordenades
dades = np.column_stack((X.ravel()-13.5, Y.ravel()-13.5, V.ravel()))

# Guardem com a txt: una fila = x y v
np.savetxt("cond_teo.txt", dades, fmt="%.6f", header="x y V", comments='')
"""