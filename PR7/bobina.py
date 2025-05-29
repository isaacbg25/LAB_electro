import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool, cpu_count
from functools import partial

def biot_savart_loop(R, I, N, L, point):
    z0, r0 = point
    mu0 = 4 * np.pi * 1e-7
    Bz_total = 0
    Br_total = 0
    dl = 2 * np.pi * R / 100  # longitud de cada element de corrent
    phi_vals = np.linspace(0, 2 * np.pi, 100)

    for i in range(N):
        z_i = -L / 2 + i * L / (N - 1)
        for phi in phi_vals:
            x = R * np.cos(phi)
            y = R * np.sin(phi)

            rx = r0 * np.cos(0)  # eix radial
            ry = r0 * np.sin(0)
            rz = z0

            dx = rx - x
            dy = ry - y
            dz = rz - z_i
            r_vec = np.array([dx, dy, dz])
            r_mag = np.linalg.norm(r_vec)

            if r_mag == 0:
                continue

            dL = np.array([-R * np.sin(phi), R * np.cos(phi), 0]) * dl
            dB = mu0 * I / (4 * np.pi) * np.cross(dL, r_vec) / r_mag**3

            Br_total += dB[0] * np.cos(0) + dB[1] * np.sin(0)
            Bz_total += dB[2]

    return Br_total, Bz_total

def compute_point(R, I, N, L, point):
    return biot_savart_loop(R, I, N, L, point)

def plot_field_parallel(R, I, N, L, res=40):
    z = np.linspace(-2 * R, 2 * R, res)
    r = np.linspace(0, 2 * R, res)
    Z, R_grid = np.meshgrid(z, r)
    points = [(zi, ri) for zi, ri in zip(Z.ravel(), R_grid.ravel())]

    print(f"Usando {cpu_count()} núcleos... Calculando {len(points)} puntos.")
    with Pool() as pool:
        results = pool.map(partial(compute_point, R, I, N, L), points)

    Br = np.array([res[0] for res in results]).reshape(R_grid.shape)
    Bz = np.array([res[1] for res in results]).reshape(R_grid.shape)
    Bmag = np.sqrt(Br**2 + Bz**2)

    # Bz
    plt.figure(figsize=(8, 6))
    plt.pcolormesh(Z, R_grid, Bz, shading='auto', cmap='viridis')
    plt.colorbar(label=r"$B_z$ (T)")
    plt.title("Component axial $B_z$ en el pla (z, r)")
    plt.xlabel("z (m)")
    plt.ylabel("r (m)")
    plt.tight_layout()
    plt.show()

    # |B|
    plt.figure(figsize=(8, 6))
    skip = (slice(None, None, 3), slice(None, None, 3))
    plt.pcolormesh(Z, R_grid, Bmag, shading='auto', cmap='plasma')
    plt.colorbar(label=r"$|\vec{B}|$ (T)")
    plt.quiver(Z[skip], R_grid[skip], Bz[skip], Br[skip], color='white', scale=5e-5)
    plt.title("$|\vec{B}|$ i direcció en el pla (z, r)")
    plt.xlabel("z (m)")
    plt.ylabel("r (m)")
    plt.tight_layout()
    plt.show()

    # Bz (r = 0)
    z_axis = np.linspace(-2 * R, 2 * R, res)
    points_z = [(zi, 0) for zi in z_axis]
    with Pool() as pool:
        results_z = pool.map(partial(compute_point, R, I, N, L), points_z)

    Bz_axis = np.array([res[1] for res in results_z])

    plt.figure(figsize=(8, 4))
    plt.plot(z_axis, Bz_axis, label=r"$B_z$ en $r = 0$")
    plt.title("Evolució de $B_z$ al llarg de l'eix axial")
    plt.xlabel("z (m)")
    plt.ylabel(r"$B_z$ (T)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    from multiprocessing import freeze_support
    freeze_support()
    R = 0.05  # radi de la bobina (m)
    I = 5     # corrent (A)
    N = 100   # núm espires
    L = 0.1   # longitud de la bobina (m)
    plot_field_parallel(R, I, N, L, res=40)
