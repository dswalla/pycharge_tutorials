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