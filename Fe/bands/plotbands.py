import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np

plt.rcParams["figure.dpi"]=150
plt.rcParams["figure.facecolor"]="white"
plt.rcParams["figure.figsize"]=(8, 6)

# load data
data = np.loadtxt('bands_pp.dat.gnu')
fermi_energy = 19.9758
high_symmetry_point_lst = [0.0000, 0.5000, 1.0000, 1.5000, 2.2071, 2.9142]   # from bands_pp.out file
high_symmetry_pointlbl_lst = ["$\Gamma$", "X", "M", "X1", "R", "X"]          # from kpath.kpf file

k = np.unique(data[:, 0])
bands = np.reshape(data[:, 1], (-1, len(k)))
# print(bands)
# print(bands.shape)

plt.figure()
for band in range(len(bands)):
    plt.plot(k, bands[band, :], linewidth=1, alpha=0.5, color='k')
plt.xlim(min(k), max(k))

# Fermi energy
plt.axhline(fermi_energy, linestyle=(0, (5, 5)), linewidth=0.75, color='k', alpha=0.5)

for highigh_symmetry_point in high_symmetry_point_lst:
    plt.axvline(highigh_symmetry_point, linewidth=0.75, color='k', alpha=0.5)

# text labels
plt.xticks(ticks= high_symmetry_point_lst, labels=high_symmetry_pointlbl_lst)
plt.ylim(10, 62)
plt.ylabel("Energy (eV)")
plt.text(2.3, fermi_energy, 'Fermi energy', fontsize="small")
plt.tight_layout()
plt.show()
