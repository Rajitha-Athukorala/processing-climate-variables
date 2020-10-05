# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 18:02:04 2020

@author: Rajitha
"""
from __future__ import print_function
import os
from netCDF4 import Dataset
from wrf import getvar, ALL_TIMES
import numpy as np
from osgeo import gdal
from osgeo import osr

all_files=os.listdir()
all_wrf_files=[]

#for root, dirs, files in os.walk('.'):
#    for file in files:
#        p=os.path.join(root,file)
#        all_files.append((os.path.abspath(p)))

#print(all_files)

for y in all_files:
    temp=y
    if (temp.find('.nc') != -1):
        all_wrf_files.append(temp)
    else:
        pass
    
all_wrf_files.reverse()
#print(all_wrf_files)
#print(all_wrf_files)

for x in all_wrf_files:
    temp=x
    print(temp)
    ncfile = Dataset(temp)
    #sw=getvar(ncfile, variable, ALL_TIMES, meta=False)
    #sw_time=getvar(ncfile, 'Times', ALL_TIMES, meta=False)
    #print(ncfile)
    variables1=['RAINC','RAINNC','SWDOWN']
    variables2=['HURS','WSS']
    variables3=['T2MIN','T2MAX']
    
    if (temp.find('wrfout') != -1):
        ras_var=variables1
    elif (temp.find('wrfcdx') != -1):
        ras_var=variables2
    elif (temp.find('wrfxtrm') != -1):
        ras_var=variables3
    else:
        print('Wrong input file')
    
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
    
    print(ras_var)
    
    for x in ras_var:
        for t in range(len(array_times)):
            variable=x
            print(variable)
            var_timestep=getvar(ncfile, variable, timeidx=t, meta=False)
            file_name=sw_str_times[t]
            time_array= np.array(var_timestep)
            flip_array=np.flipud(time_array)
            if variable=='HURS':
                flip_array[flip_array>1]=1
            else:
                pass
            print(file_name)
            #print(np.max(flip_array))
            output_raster = gdal.GetDriverByName('GTiff').Create('{}{}.tif'.format(file_name[0:13],variable),ncols, nrows, 1 ,gdal.GDT_Float32)  # Open the file
            output_raster.SetGeoTransform(geotransform)  # Specify its coordinates
            srs = osr.SpatialReference()                 # Establish its coordinate encoding
            srs.ImportFromEPSG(4326)                     # This one specifies WGS84 lat long.
            output_raster.SetProjection( srs.ExportToWkt() )   # Exports the coordinate system 
        #                                                       # to the file
            output_raster.GetRasterBand(1).WriteArray(flip_array)   # Writes my array to the raster
        #    
            output_raster.FlushCache()
#
#
#
