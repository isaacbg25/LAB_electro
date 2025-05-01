import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.colors as mcolors

plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'

# Dimensions de la malla
nx, ny = 132, 132
V_t = np.zeros((ny, nx))
d = 15
l = 40
plt.figure(figsize=(8, 6))

# Condicions de contorn (dos rectangles com plaques)
V_t[int(ny/2-l/2):int(ny/2+l/2), int(nx/2 - d/2):int(nx/2 - d/2)+2] = 7.5  # placa esquerra
V_t[int(ny/2-l/2):int(ny/2+l/2), int(nx/2 + d/2):int(nx/2 + d/2)+2] = -7.5    # placa dreta

# Iteració per resoldre Laplace (mètode de Jacobi)
for _ in range(6000):
    V_t_new = V_t.copy()
    V_t_new[1:-1,1:-1] = 0.25 * (V_t[1:-1, :-2] + V_t[1:-1, 2:] + V_t[:-2, 1:-1] + V_t[2:, 1:-1])
    
    # Reaplica condicions de contorn a la noV_ta matriu
    V_t_new[int(ny/2-l/2):int(ny/2+l/2), int(nx/2 - d/2):int(nx/2 - d/2)+2] = 7.5
    V_t_new[int(ny/2-l/2):int(ny/2+l/2), int(nx/2 + d/2):int(nx/2 + d/2)+2] = -7.5
    
    V_t = V_t_new

V_t[0,:]=100
V_t[:,0]=100
#V_t[90:99,:]=0.1
#V_t[:,90:99]=0.1
"""
# Dibuixa les línies equipotencials
niV_tells = [0,1.5,3,7.5,10,13.5,14.99]
niV_tells = [x-7.5 for x in niV_tells]  # Potencials concrets que V_tols mostrar
plt.contour(V_t, leV_tels=niV_tells, colors='k')  # 'k' = negre
plt.title("Línies equipotencials (condensador no ideal)")
plt.gca().set_aspect('equal')
#plt.show()
#print(niV_tells)
"""
x = np.linspace(0, 27, nx)  # coordenades x
y = np.linspace(0, 27, ny)  # coordenades y
X_t, Y_t = np.meshgrid(x, y)
ny, nx = V_t.shape


# Aplanem les dades, les posem per columnes i canV_tiem el centre de coordenades
#dades = np.column_stack((X.raV_tel()-13.5, Y.raV_tel()-13.5, V_t.raV_tel()))

# Guardem com a txt: una fila = x y V_t
#np.saV_tetxt("cond_teo.txt", dades, fmt="%.6f", header="x y V_t", comments='')

# Calcular components del camp elèctric
Ey_t, Ex_t = np.gradient(-V_t)
E_t = np.sqrt(Ex_t**2 + Ey_t**2)

# --- Selecció de punts amb camp fort per començar línies ---
threshold = np.percentile(E_t, 80)  # només el 15% més fort
seeds_y, seeds_x = np.where(E_t > threshold)

# Transformar a coordenades reals
seeds = np.column_stack((x[seeds_x]-13.5, y[seeds_y]-13.5))
# Representar línies de camp elèctric
plt.streamplot(X_t-13.5, Y_t-13.5, Ex_t, Ey_t, color='darkslategrey', linewidth=0.6, arrowsize=1.0, start_points=seeds)

# Línies equipotencials (opcional)
#plt.contour(X, Y, V, levels=nivells, colors='black')
"""
# Format de gràfica
plt.gca().set_aspect('equal')
plt.title("Línies de camp elèctric i equipotencials")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
"""

import numpy as np
import matplotlib.pyplot as plt

def llegir_equipotencials(filename):
    with open(filename, 'r') as f:
        contingut = f.read()

    blocs = contingut.strip().split('\n\n')
    llistes_coords = []

    for bloc in blocs:
        linies = bloc.strip().split('\n')
        coords = [list(map(float, linia.strip().split())) for linia in linies]
        llistes_coords.append(np.array(coords))

    return llistes_coords

def representar_segments_llargs(equipotencials, salt=2, llargada=0.5):
    
    for coords in equipotencials:
        x = coords[:, 0]
        y = coords[:, 1]
        dx = np.gradient(x)
        dy = np.gradient(y)

        # Vector perpendicular
        Ex = -dy
        Ey = dx

        # Normalitzar
        mag = np.sqrt(Ex**2 + Ey**2)
        Ex_unit = Ex / mag
        Ey_unit = Ey / mag

        # Posicions i vectors reduïts
        x_plot = x[::salt]
        y_plot = y[::salt]
        u = Ex_unit[::salt] * llargada / 2
        v = Ey_unit[::salt] * llargada / 2

        # Dibuixar segments (centrats)
        for xi, yi, ui, vi in zip(x_plot, y_plot, u, v):
            plt.plot([xi - ui, xi + ui], [yi - vi, yi + vi], color='lightskyblue')

    #plt.streamplot(X_t, Y_t, Ex_t, Ey_t, color='blue', density=1.2, linewidth=0.8, arrowsize=1)
    rectangle_1 = patches.Rectangle((1.4, -4), 0.3, 8, facecolor='black', label='Placa a -7.5 V')
    plt.gca().add_patch(rectangle_1)

    rectangle_1 = patches.Rectangle((-1.5, -4), 0.3, 8, facecolor='black', alpha=0.5, label='Placa a 7.5 V')
    plt.gca().add_patch(rectangle_1)
    
    from matplotlib.lines import Line2D
    from matplotlib.patches import FancyArrow

    # Segment simple (línia experimental)
    segment_experimental = Line2D([0], [0], color='lightskyblue', lw=2, label='Resultat experimental')

    # Fletxa (línia computacional amb punta)
    # FancyArrow no es pot posar directament a la llegenda, però podem fer servir una línia amb un capçal de fletxa
    fletxa_computacional = Line2D([0], [0], color='darkslategrey', lw=2, label='Càlcul computacional')

    # Crear la llegenda
    plt.legend(handles=[segment_experimental, fletxa_computacional]+plt.gca().get_legend_handles_labels()[0])

    plt.xlim(-13,13)
    plt.ylim(-10,10)
    plt.xlabel('x(cm)')
    plt.ylabel('y(cm)')
    plt.gca().set_aspect('equal')
    #plt.title('Camp elèctric amb segments llargs')
    plt.grid(True, linestyle=':', linewidth=1, alpha=0.7)
    plt.tight_layout()
    plt.tick_params(direction='in', top=True, right=True)
    plt.savefig("cond_camp.png", dpi=300)
    plt.show()

# === Executar ===
fitxer = 'cond_exp_2.txt'
equipotencials = llegir_equipotencials(fitxer)
representar_segments_llargs(equipotencials, salt=2, llargada=1.2)
