# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:11:21 2020

@author: Rajitha
"""

from __future__ import print_function
from netCDF4 import Dataset
from wrf import getvar, ALL_TIMES
import numpy as np
from osgeo import gdal
from osgeo import osr


#get the user input file
filename =input("Enter the filename:")

#get the user input variable
variable =input("Enter the required variable:")
ncfile = Dataset(filename)
sw=getvar(ncfile, variable, ALL_TIMES, meta=False)
sw_time=getvar(ncfile, 'Times', ALL_TIMES, meta=False)

array_times=np.array(sw_time)
sw_str_times=np.datetime_as_string(array_times)

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

geotransform=(xmin,xres,0,ymax,0,-yres)

for t in range(len(array_times)):
    var_timestep=getvar(ncfile, variable, timeidx=t, meta=False)
    file_name=sw_str_times[t]
    time_array= np.array(var_timestep)
    flip_array=np.flipud(time_array)
    print(file_name)
    output_raster = gdal.GetDriverByName('GTiff').Create('{}{}.tif'.format(file_name[0:13],variable),ncols, nrows, 1 ,gdal.GDT_Float32)  # Open the file
    output_raster.SetGeoTransform(geotransform)  # Specify its coordinates
    srs = osr.SpatialReference()                 # Establish its coordinate encoding
    srs.ImportFromEPSG(4326)                     # This one specifies WGS84 lat long.
    output_raster.SetProjection( srs.ExportToWkt() )   # Exports the coordinate system 
#                                                       # to the file
    output_raster.GetRasterBand(1).WriteArray(flip_array)   # Writes my array to the raster
#    
    output_raster.FlushCache()

