#
# Purpose: to illustrate how to use h5py methods built
#          in Python to get the information from an HDF5 file 

# The example reads "Radiance" sds and it's asociated geo-location sds, then a geo-map is created

# Date  :  July. 06, 2017

# importing the libraries needed
import numpy as np
import h5py
import os
import math
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

#
# Read HDF5 file
#
dir_data    = '../Data/'
fileName = "GDNBO-SVDNB_npp_d20160831_t1816216_e1822020_b25103_c20161105035502773833_noaa_ops.h5"
f = h5py.File(dir_data+fileName,'r')

# retrieving sds 
dnblat = f['All_Data/VIIRS-DNB-GEO_All/Latitude'][:]
dnblon = f['All_Data/VIIRS-DNB-GEO_All/Longitude'][:]
dnbrad = f['All_Data/VIIRS-DNB-SDR_All/Radiance'][:]

# defining sub-domain for plotting (Seoul)
latmax = 38
latmin = 37
lonmin = 126
lonmax = 128 

# creating the plot
m = Basemap(projection='cyl',llcrnrlat=latmin,urcrnrlat=latmax,llcrnrlon=lonmin,urcrnrlon=lonmax,lat_ts=10,resolution='l')
m.pcolormesh(dnblon, dnblat, dnbrad, latlon=True)
m.drawparallels(np.arange(math.ceil(37),math.ceil(38.01),.2),labels=[1,0,0,0],linewidth=0.01,labelstyle="N/S",fontsize=12)		#lat scale line (latM)+1,5) so the every degrees there is a scale mark
m.drawmeridians(np.arange(math.ceil(126),math.ceil(lonmax),.5),labels=[0,0,0,1],linewidth=0.01,labelstyle="E/w",fontsize=12)		#long scale line

plt.savefig('rad.png', bbox_inches='tight', dpi=200)
#plt.show()

