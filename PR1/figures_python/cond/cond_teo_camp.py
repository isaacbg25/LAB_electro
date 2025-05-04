import numpy as np
import matplotlib.pyplot as plt

# --- Paràmetres i condicions inicials ---
nx, ny = 132, 132
V = np.zeros((ny, nx))
d = 15
l = 40
V[int(ny/2-l/2):int(ny/2+l/2), int(nx/2 - d/2):int(nx/2 - d/2)+2] = 7.5
V[int(ny/2-l/2):int(ny/2+l/2), int(nx/2 + d/2):int(nx/2 + d/2)+2] = -7.5

# --- Resolució amb Jacobi ---
for _ in range(6000):
    V_new = V.copy()
    V_new[1:-1,1:-1] = 0.25 * (V[1:-1, :-2] + V[1:-1, 2:] + V[:-2, 1:-1] + V[2:, 1:-1])
    V_new[int(ny/2-l/2):int(ny/2+l/2), int(nx/2 - d/2):int(nx/2 - d/2)+2] = 7.5
    V_new[int(ny/2-l/2):int(ny/2+l/2), int(nx/2 + d/2):int(nx/2 + d/2)+2] = -7.5
    V = V_new

# --- Coordenades i gradients ---
x = np.linspace(0, 27, nx)
y = np.linspace(0, 27, ny)
X_t, Y_t = np.meshgrid(x, y)
Ey_t, Ex_t = np.gradient(-V)
E_t = np.sqrt(Ex_t**2 + Ey_t**2)

# --- Selecció de punts amb camp fort per començar línies ---
threshold = np.percentile(E_t, 80)  # només el 15% més fort
seeds_y, seeds_x = np.where(E_t > threshold)

# Transformar a coordenades reals
seeds = np.column_stack((x[seeds_x], y[seeds_y]))

# --- Gràfic ---
plt.figure(figsize=(8, 6))

# Línies equipotencials
nivells = np.linspace(-7.5, 7.5, 11)
plt.contour(X_t, Y_t, V, levels=nivells, colors='lightblue', linewidths=0.7)

# Línies de camp amb streamplot + punts forts com a fonts
plt.streamplot(X_t, Y_t, Ex_t, Ey_t, color='black', linewidth=0.6, arrowsize=1.0, start_points=seeds)

plt.title("Línies de camp amb densitat adaptativa (zones de camp intens)")
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.grid(True)
plt.tight_layout()
plt.show()
