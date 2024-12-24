import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np

# load data
energy, dosup, dosdw, idos = np.loadtxt('./dos.dat', unpack=True)
fermi_energy = 19.973

# make plot
plt.figure(figsize = (10, 5))
plt.plot(energy, dosup, linewidth=0.75, color='red')
plt.plot(energy, -dosdw, linewidth=0.75, color='blue')
plt.yticks([])
plt.xlabel('Energy (eV)')
plt.ylabel('DOS')
plt.axvline(x=fermi_energy, linewidth=0.5, color='k', linestyle=(0, (8, 10)))
plt.xlim(12, 29)
plt.ylim(-12, 10)
plt.fill_between(energy, 0, dosup, where=(energy < fermi_energy), facecolor='red', alpha=0.25)
plt.fill_between(energy, 0, -dosdw, where=(energy < fermi_energy), facecolor='blue', alpha=0.25)
plt.text(fermi_energy-0.3, -8, 'Fermi energy', fontsize="medium", rotation=90)
plt.tight_layout()
plt.show()
