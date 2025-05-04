import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.colors as mcolors


plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'Helvetica'
plt.rcParams.update({'font.size': 15})

# Llegir dades de potencial (x, y, V)
dades = np.loadtxt("cond_teo.txt", skiprows=1)  # salta la capçalera
x = dades[:, 0]
y = dades[:, 1]
V = dades[:, 2]/0.8

# Crear malla per fer el contour
nx = len(np.unique(x))
ny = len(np.unique(y))
X = x.reshape(ny, nx)
Y = y.reshape(ny, nx)
Z = V.reshape(ny, nx)

# Mascara per limitar l'àrea visualitzada
Z_masked = np.ma.masked_where(abs(Y) > 15, Z)
Z_masked = np.ma.masked_where(abs(X) > 15, Z_masked)

plt.figure(figsize=(8, 6))
# Dibuixar línies equipotencials
nivells = [-6.0, -4.5, 0.0, 2.5, 6.0]
#nivells = [x-7.5 for x in nivells]
#print(nivells)

cmap = plt.cm.Set1
norm = mcolors.Normalize(vmin=min(nivells), vmax=max(nivells))

contours = plt.contour(X, Y, Z_masked, levels=nivells,cmap=cmap, norm=norm, linewidths=1.5)
plt.clabel(contours, inline=True, fontsize=12, manual=[(3,1),(7,3),(-4,-1),(-6,-4),(0,4)],fmt='%1.1f V')

rectangle_1 = patches.Rectangle((1.4, -4), 0.3, 8, facecolor='black', label='Placa a -7.5 V')
plt.gca().add_patch(rectangle_1)

rectangle_1 = patches.Rectangle((-1.5, -4), 0.3, 8, facecolor='black', alpha=0.5, label='Placa a 7.5 V')
plt.gca().add_patch(rectangle_1)

# Llegir blocs de punts separats per línies en blanc
with open("cond_exp_2.txt") as f:
    blocs = []
    bloc_actual = []

    for linia in f:
        if linia.strip() == "":
            if bloc_actual:
                blocs.append(bloc_actual)
                bloc_actual = []
        else:
            bloc_actual.append([float(x) for x in linia.strip().split()])

    if bloc_actual:
        blocs.append(bloc_actual)

# Dibuixar els punts experimentals amb colors diferents per cada bloc
valors = [0.0,-6.0,-4.5,6.0,2.5]
for i, bloc in enumerate(blocs):
    bloc = np.array(bloc)
    color = cmap(norm(valors[i]))  #  Això fa que el color sigui igual al del contour
    plt.scatter(bloc[:, 0], bloc[:, 1], s=7, color=color)# label=f"potencial {valors[i]}")




# Estètica
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.ylim(-6.5,6.5)
plt.xlim(-10,10)
#plt.title("Línies equipotencials i punts experimentals")
from matplotlib.lines import Line2D

#handles, labels = plt.gca().get_legend_handles_labels()
#leg1 = plt.legend(handles, labels, loc='lower right', fontsize=10)

#plt.gca().add_artist(leg1)

# Crear símbols falsos per la llegenda
linea_computacional = Line2D([0], [0], color='black', lw=1.5, label='Simulació')
punts_experimentals = Line2D([0], [0], marker='o', color='none', markerfacecolor='black', markersize=4,
                             label='Experimental')

# Afegir llegenda amb aquests símbols + les corbes reals
plt.legend(handles=plt.gca().get_legend_handles_labels()[0], fontsize=12) #handles=[linea_computacional, punts_experimentals] 


plt.grid(True, linestyle=':', linewidth=1, alpha=0.5)
plt.tight_layout()
plt.tick_params(direction='in', top=True, right=True)
plt.gca().set_aspect('equal')
plt.savefig("cond_combi_epsilon.pdf")
plt.show()