import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np

energy, pdos_s = np.loadtxt('atom_Si_s.dat', unpack=True)
_, pdos_p = np.loadtxt('atom_Si_p.dat', unpack=True)
_, dos, pdos_tot = np.loadtxt('pdos.pdos_tot', unpack=True)
fermi_energy = 6.553

plt.figure(figsize = (8, 4))
plt.plot(energy, pdos_s, linewidth=0.75, color='#006699', label='s-orbital PDOS')
plt.plot(energy, pdos_p, linewidth=0.75, color='r', label='p-orbital PDOS')
plt.plot(energy, pdos_tot, linewidth=0.75, color='k', label='Total PDOS')
plt.plot(energy, dos, linewidth=0.75, color='g', label='DOS')
plt.yticks([])
plt.xlabel('Energy (eV)')
plt.ylabel('DOS')
plt.axvline(x= fermi_energy, linewidth=0.5, color='k', linestyle=(0, (8, 10)))
plt.xlim(-6, 16)
plt.ylim(0, )
plt.fill_between(energy, 0, pdos_s, where=(energy < fermi_energy), facecolor='#006699', alpha=0.25)
plt.fill_between(energy, 0, pdos_p, where=(energy < fermi_energy), facecolor='r', alpha=0.25)
plt.fill_between(energy, 0, pdos_tot, where=(energy < fermi_energy), facecolor='k', alpha=0.25)
plt.fill_between(energy, 0, dos, where=(energy < fermi_energy), facecolor='k', alpha=0.25)
plt.text(fermi_energy-0.4, 1.7, 'Fermi energy', fontsize="medium", rotation=90)
plt.legend(frameon=False)
plt.tight_layout()
plt.show()
