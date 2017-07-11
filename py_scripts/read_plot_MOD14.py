#
# Purpose: to illustrate how to use netCDF4 methods built
#          in Python to get the information of fires from 
#          an HDF4 file and generate a plot 

# Date  :  July. 07, 2017

import numpy as np
from netCDF4 import Dataset
import os
import math
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


#
# Read HDF data files for get Fire and Thermal Anomalies and Geolocation information
#
dir_data    = '../Data/'
hdf_file    = 'MOD14.A2017001.1655.006.2017004111822.hdf'
hdf_geofile = 'MOD03.A2017001.1655.006.2017003202340.hdf'

sd     = Dataset(dir_data+hdf_file)
sd_geo = Dataset(dir_data+hdf_geofile)

#
# Retrieving the SDS we’re interested on
#
fire      = sd.variables['fire mask']
sds_lon   = sd_geo.variables['Longitude']
sds_lat   = sd_geo.variables['Latitude']

#
# obtaining max and min values from lat and lon
#
latmin = math.ceil(np.min(sds_lat))
latmax = math.ceil(np.max(sds_lat))
lonmin = math.ceil(np.min(sds_lon))
lonmax = math.ceil(np.max(sds_lon))

#
# creating geo-map and saving it
#
m = Basemap(projection='cyl',llcrnrlat=latmin,urcrnrlat=latmax,\
            llcrnrlon=lonmin,urcrnrlon=lonmax,lat_ts=10,resolution='l')
m.pcolormesh(sds_lon, sds_lat, fire, cmap=plt.cm.jet, latlon=True)

# setting plot
parales = np.arange(math.ceil(latmin),math.ceil(latmax),6)
medirians = np.arange(math.ceil(lonmin),math.ceil(lonmax),8)

m.drawparallels(parales, labels=[1,0,0,0],linewidth=0.01,labelstyle="N/S",fontsize=12)
m.drawmeridians(medirians,labels=[0,0,0,1],linewidth=0.01,labelstyle="E/w",fontsize=12)
cb=m.colorbar()
plt.title('Fire mask from MOD14 product')

# save plot
plt.savefig('fire_mask.png', dpi=300)
#plt.show()

