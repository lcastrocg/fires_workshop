#
# Purpose: to illustrate how to use netCDF4 methods built
#          in Python to get the information of a HDF4 file
# Author:  Lorena Castro
# Date  :  Jan. 24, 2017
#
# Read HDF file
#

#librarty needed to explore HDF4 files in python
from netCDF4 import Dataset

#
# See what is inside
#

# Open the HDF file
dir_data    = '../Data/'
filename = "MOD14.A2017001.1655.006.2017004111822.hdf"
hdf_file   = Dataset(dir_data+filename)

# reading the datasets and file attibutes in file
hdf_datasets = hdf_file.variables
hdf_attrs   = hdf_file.ncattrs()

# print No. of datasets and attributes
print ("No. of datasets :   ", len(hdf_datasets))
print ("No. of attributes : ", len(hdf_attrs))

# print name of each  attribute
# enumerate create a list to iterate over it,
# this return and index and each element
for idx, attribute in enumerate(hdf_attrs):
    print ("File Attibute # ", idx, attribute)
    
# print name of each SDS and associated attributes
for idx, sds_name in enumerate(hdf_datasets):
    print  ('SDS No.', idx, hdf_datasets[sds_name].name)
    SDS_dimensions = hdf_datasets[sds_name].dimensions
    
    # reading an specific attribute of the SDS
    SDS_size = hdf_datasets[sds_name].shape
    
    # reading all the SDS attributes
    SDS_attributes = hdf_datasets[sds_name].ncattrs()
    
    # read and print dimension attributes
    for i in range(len(SDS_dimensions)):
        print ('Dim:', i, 'size:',SDS_size[i], 'name:', SDS_dimensions[i])
    
    # get and print SDS attribites
    for attr in SDS_attributes:
        print ('\tData Attribute:', attr)
    
    print('\n')
    
