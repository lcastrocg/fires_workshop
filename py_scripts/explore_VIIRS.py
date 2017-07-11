#
# Purpose: to illustrate how to use h5py methods built
#          in Python to get the information from an HDF5 file 

# Date  :  July. 06, 2017



# importing the libraries needed
import h5py    # HDF5 support

# name of the h5 file
dir_data    = '../Data/'
fileName = "GDNBO-SVDNB_npp_d20160831_t1816216_e1822020_b25103_c20161105035502773833_noaa_ops.h5"

# opening h5 file
f = h5py.File(dir_data+fileName,  "r")

# reading global attributes of the file
for item in f.attrs.keys():
    print (item + ":", f.attrs[item])
    
# retrieving main gropus where data and metadata are stored
main_gps = list(f)
print(main_gps)

# retrieving sub-groups from 'All_Data' group
for gpos in f['All_Data']:
    print(gpos)
    
# getting name of datasets in VIIRS-DNB-GEO_All sub-group
for sds_geo in f['All_Data']['VIIRS-DNB-GEO_All']:
    print(sds_geo)

# getting name of datasets in VIIRS-DNB-SDR_All subgroup
for sds_sdr in f['All_Data/VIIRS-DNB-SDR_All']:
    print(sds_sdr)

# getting name of datasets in VIIRS-DNB-SDR_All subgroup
for sds_sdr in f['All_Data']['VIIRS-DNB-SDR_All'].keys():
    print (sds_sdr)
    
# All of the objects in the h5 file can be identified using the following commands
all_objects=[]
f.visit(all_objects.append)
for obj in all_objects:
    print(obj)

# retrieving shape, dtype of "VIIRS-DNB-SDR" datasets
for sds_sdr in f['Data_Products']['VIIRS-DNB-SDR']['VIIRS-DNB-SDR_Aggr']:
    print(f[sds_sdr])

# retrieving all attributes/metadata of all VIIRS-DNB-SDR datasets
for sds_sdr in f['Data_Products']['VIIRS-DNB-SDR'].values():
    print(sds_sdr, "\n")
    for sds_sdr_atts in  (sds_sdr.attrs):
        print (sds_sdr_atts, sds_sdr.attrs[sds_sdr_atts])
    print("----- next ------", "\n")

