import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np

# load data
energy, dos, idos = np.loadtxt('./dos.dat', unpack=True)
fermi_energy = 6.553

# make plot
plt.figure(figsize = (10, 5))
plt.plot(energy, dos, linewidth=0.75, color='red')
plt.yticks([])
plt.xlabel('Energy (eV)')
plt.ylabel('DOS')
plt.axvline(x=fermi_energy, linewidth=0.5, color='k', linestyle=(0, (8, 10)))
plt.xlim(-6, 16)
plt.ylim(0, )
plt.fill_between(energy, 0, dos, where=(energy < fermi_energy), facecolor='red', alpha=0.25)
plt.text(fermi_energy-0.4, 1.7, 'Fermi energy', fontsize="medium", rotation=90)
plt.tight_layout()
plt.show()
