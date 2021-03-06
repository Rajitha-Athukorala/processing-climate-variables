# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 13:52:11 2020

@author: Rajitha
"""
from __future__ import print_function
from netCDF4 import Dataset
from wrf import getvar, ALL_TIMES
import numpy as np
from osgeo import gdal
from osgeo import osr

#get the user input file
filename = input("Enter the file name:")

#get the user input variable
variable =input("Enter the required variable:")
ncfile = Dataset(filename)
# Get the lat,lon, and T2
lat = getvar(ncfile, "LAT", meta=False)
lon = getvar(ncfile, "LON", meta=False)
timeindex= getvar(ncfile, "Times", ALL_TIMES, meta=False)

#Timesteps
array_times = np.array(timeindex)
idx=len(array_times)
str_times=np.datetime_as_string(array_times)

# My image array      
lat = np.array(lat)
lon = np.array(lon)

xmin=98.759
ymin=12.911
xmax=110.142
ymax=23.697
xres=0.045
yres=0.045

nrows=240
ncols=240
nrows=240
ncols=240

geotransform=(xmin,xres,0,ymax,0, -yres)

#Digital number for each pixel
for t in range(len(array_times)):
    var_timestep=getvar(ncfile, variable, timeidx=t, meta=False)
    file_name=str_times[t]
    time_array= np.array(var_timestep)
    print(file_name)
    output_raster = gdal.GetDriverByName('GTiff').Create('{}{}.tif'.format(file_name[0:13],variable),ncols, nrows, 1 ,gdal.GDT_Float32)  # Open the file
    output_raster.SetGeoTransform(geotransform)  # Specify its coordinates
    srs = osr.SpatialReference()                 # Establish its coordinate encoding
    srs.ImportFromEPSG(4326)                     # This one specifies WGS84 lat long.
    output_raster.SetProjection( srs.ExportToWkt() )   # Exports the coordinate system 
                                                       # to the file
    output_raster.GetRasterBand(1).WriteArray(time_array)   # Writes my array to the raster
    
    output_raster.FlushCache()
 

#for x in range(len(array_times)):
#    string_name=str_times[x]
#    os.rename(r'%s.tif'%x,r'%s.tif'%string_name[0:13])
