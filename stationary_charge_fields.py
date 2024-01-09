import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

import pycharge as pc

source = pc.StationaryCharge(position=(0,0,0))
simulation = pc.Simulation(source)

lim = 10e-9
npoints = 1000
coordinates = np.linspace(-lim,lim,npoints)
x, y, z = np.meshgrid(coordinates, coordinates, 0, indexing='ij')

E_x, E_y, E_z = simulation.calculate_E(t=0, x=x, y=y, z=z)

E_x_plane = E_x[:,:,0]
E_y_plane = E_y[:,:,0]
E_z_plane = E_z[:,:,0]

fig, axs = plt.subplots(1, 3, sharey=True)
norm = mpl.colors.SymLogNorm(linthresh=1.01e6, linscale=1, vmin=-1e9, vmax=1e9)
extent = [-lim, lim, -lim, lim]
im_0 = axs[0].imshow(E_x_plane.T, origin='lower', norm=norm, extent=extent)
im_1 = axs[1].imshow(E_y_plane.T, origin='lower', norm=norm, extent=extent)
im_2 = axs[2].imshow(E_z_plane.T, origin='lower', norm=norm, extent=extent)

for ax in axs:
    ax.set_xlabel('x (nm)')
axs[0].set_ylabel('y (nm)')
axs[0].set_title('E_x (N/C)')
axs[1].set_title('E_y (N/C)')
axs[2].set_title('E_z (N/C)')

Ecax = inset_axes(
    axs[2], width="6%", height="100%", loc='lower left',
    bbox_to_anchor=(1.05, 0., 1, 1), bbox_transform=axs[2].transAxes, borderpad=0
)
E_cbar = plt.colorbar(im_2, cax=Ecax)  # right of im_2
E_cbar.ax.set_ylabel('E (N/C)', rotation=270, labelpad=12)

plt.show()
