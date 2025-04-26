import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.colors as mcolors


plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'

# Llegir dades de potencial (x, y, V)
dades = np.loadtxt("lliure_teo_e.txt", skiprows=1)  # salta la capçalera
x = dades[:, 0]
y = dades[:, 1]
V = dades[:, 2]

# Crear malla per fer el contour
nx = len(np.unique(x))
ny = len(np.unique(y))
X = x.reshape(ny, nx)
Y = y.reshape(ny, nx)
Z = V.reshape(ny, nx)

# Mascara per limitar l'àrea visualitzada
Z_masked = np.ma.masked_where(abs(Y) > 15, Z)
Z_masked = np.ma.masked_where(abs(X) > 15, Z_masked)

cmap = plt.cm.viridis  # o plasma, inferno, coolwarm, etc.

# Dibuixar contorn ple (contourf)



plt.figure(figsize=(8, 6))
# Dibuixar línies equipotencials
nivells = [0.1,0.5,1.5]
nivells = [7.5-x for x in nivells]

nivells.extend([10-7.5,3-7.5])
nivells = sorted(nivells)
print(nivells)


nivells = np.linspace(-3.4, 7.1, 15)  # 20 nivells de color
contours = plt.contour(X, Y, Z_masked, levels=nivells,cmap=cmap)
plt.clabel(contours, inline=True, fontsize=7,fmt='%1.1f V') #manual=[(3,1),(7,3),(-4,-1),(-6,-4),(0,4)]

rectangle_1 = patches.Circle((3, 0), 0.5, facecolor='black', label='Fil a -7.5 V')
plt.gca().add_patch(rectangle_1)

rectangle_1 = patches.Rectangle((-2, 0.2), 0.5,7.2, facecolor='black', alpha=0.5, label='Plaques a 7.5 V')
plt.gca().add_patch(rectangle_1)

rectangle_1 = patches.Rectangle((-2, -7.4), 0.5,7.2, facecolor='black', alpha=0.5)
plt.gca().add_patch(rectangle_1)



# Llegir blocs de punts separats per línies en blanc
with open("lliure_exp.txt") as f:
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
valors = [-4.5, 2.5, 7.4, 7.0,6.0]
colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231']
for i, bloc in enumerate(blocs):
    bloc = np.array(bloc)
    color = colors[i]#cmap(norm(valors[i]))  #  Això fa que el color sigui igual al del contour
    plt.scatter(bloc[:, 0], bloc[:, 1], s=20, color=color)# label=f"potencial {valors[i]}")




# Estètica
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')

plt.ylim(-6.5*1.3,6.5*1.3)
plt.xlim(-10*1.3,10*1.3)
#plt.title("Línies equipotencials i punts experimentals")
from matplotlib.lines import Line2D

# Crear símbols falsos per la llegenda
linea_computacional = Line2D([0], [0], color='black', lw=1, label='Càlcul computacional')
punts_experimentals = Line2D([0], [0], marker='o', color='none', markerfacecolor='red', markersize=5,
                             label='Dades experimentals')

# Afegir llegenda amb aquests símbols + les corbes reals
plt.legend(handles=[linea_computacional, punts_experimentals] + plt.gca().get_legend_handles_labels()[0])

plt.grid(True, linestyle=':', linewidth=1, alpha=0.5)
plt.tight_layout()
plt.tick_params(direction='in', top=True, right=True)
plt.gca().set_aspect('equal')
plt.savefig("lliure_combi_e_vermell.png", dpi=300)
plt.show()