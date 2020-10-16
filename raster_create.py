# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 11:51:01 2020

@author: Rajitha
"""
import os
import numpy as np
from osgeo import gdal
from osgeo import osr
from datetime import date, timedelta

xmin=99.11
ymin=12.95
xmax=111.13
ymax=23.7
xres=0.045
yres=0.045
nrows=240
ncols=240

geotransform=(xmin,xres,0,ymax,0, -yres)

Years=['2019']               #fill in the years required

for i1 in Years:
    hurs=np.load('HURS_'+str(i1)+'.npy')
    wss=np.load('WSS_'+str(i1)+'.npy')
    swdown=np.load('SWDOWN_'+str(i1)+'.npy')
    rain=np.load('RAIN_'+str(i1)+'.npy')
    t2min=np.load('T2MIN_'+str(i1)+'.npy')
    t2max=np.load('T2MAX_'+str(i1)+'.npy')
    file_year=[]
    startdate=date(int(i1), int('01'), int('01'))
    enddate=date(int(i1), int('12'), int('31'))
    delta = enddate - startdate
    print(i1)
    for i2 in range(delta.days +1):
        day = startdate + timedelta(days=i2)
        file_year.append(day)
    for i3 in range (wss.shape[-1]):
        hurs_array=hurs[:,:,i3]
        wss_array=wss[:,:,i3]
        swdown_array=swdown[:,:,i3]
        rain_array=rain[:,:,i3]
        t2min_array=t2min[:,:,i3]
        t2max_array=t2max[:,:,i3]
        output_raster_t2max = gdal.GetDriverByName('GTiff').Create('H:\\Downscaling project\\Raster data creation\\Rasters\\T2MAX-{}.tif'.format(file_year[i3]),ncols, nrows, 1 ,gdal.GDT_Float32)  # Open the file
        output_raster_t2min = gdal.GetDriverByName('GTiff').Create('H:\\Downscaling project\\Raster data creation\\Rasters\\T2MIN-{}.tif'.format(file_year[i3]),ncols, nrows, 1 ,gdal.GDT_Float32)
        output_raster_rain = gdal.GetDriverByName('GTiff').Create('H:\\Downscaling project\\Raster data creation\\Rasters\\RAIN-{}.tif'.format(file_year[i3]),ncols, nrows, 1 ,gdal.GDT_Float32)
        output_raster_hurs = gdal.GetDriverByName('GTiff').Create('H:\\Downscaling project\\Raster data creation\\Rasters\\HURS-{}.tif'.format(file_year[i3]),ncols, nrows, 1 ,gdal.GDT_Float32)
        output_raster_wss = gdal.GetDriverByName('GTiff').Create('H:\\Downscaling project\\Raster data creation\\Rasters\\WSS-{}.tif'.format(file_year[i3]),ncols, nrows, 1 ,gdal.GDT_Float32)
        output_raster_swdown = gdal.GetDriverByName('GTiff').Create('H:\\Downscaling project\\Raster data creation\\Rasters\\SWDOWN-{}.tif'.format(file_year[i3]),ncols, nrows, 1 ,gdal.GDT_Float32)
        
        output_raster_t2max.SetGeoTransform(geotransform)  # Specify its coordinates
        output_raster_t2min.SetGeoTransform(geotransform)
        output_raster_rain.SetGeoTransform(geotransform)
        output_raster_hurs.SetGeoTransform(geotransform)
        output_raster_wss.SetGeoTransform(geotransform)
        output_raster_swdown.SetGeoTransform(geotransform)
        
        srs = osr.SpatialReference()                 # Establish its coordinate encoding
        srs.ImportFromEPSG(4326)                     # This one specifies WGS84 lat long.
        
        output_raster_t2max.SetProjection( srs.ExportToWkt() )   # Exports the coordinate system 
        output_raster_t2min.SetProjection( srs.ExportToWkt() )
        output_raster_rain.SetProjection( srs.ExportToWkt() )
        output_raster_hurs.SetProjection( srs.ExportToWkt() )
        output_raster_wss.SetProjection( srs.ExportToWkt() )
        output_raster_swdown.SetProjection( srs.ExportToWkt() )
        #                                                       
        output_raster_t2max.GetRasterBand(1).WriteArray(t2max_array) 
        output_raster_t2min.GetRasterBand(1).WriteArray(t2min_array)# Writes my array to the raster
        output_raster_rain.GetRasterBand(1).WriteArray(rain_array)
        output_raster_hurs.GetRasterBand(1).WriteArray(hurs_array)
        output_raster_wss.GetRasterBand(1).WriteArray(wss_array)
        output_raster_swdown.GetRasterBand(1).WriteArray(swdown_array)
        #    
        output_raster_t2max.FlushCache()
        output_raster_t2min.FlushCache()
        output_raster_rain.FlushCache()
        output_raster_hurs.FlushCache()
        output_raster_wss.FlushCache()
        output_raster_swdown.FlushCache()
        
        