# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 17:02:05 2020

@author: Rajitha
"""
from datetime import date, timedelta
import rasterio
from osgeo import gdal
from osgeo import osr


starty = input('Starting date:')
startm = input('Starting month:')
startd = input('Starting day:')
endy = input('End year:')
endm = input('End month:')
endd = input('End day:')
clvar1 = input('Climate variable1:')
clvar2 = input('Climate variable2:')
    
filenames=[]


startdate =date(int(starty), int(startm), int(startd))
enddate =date(int(endy), int(endm), int(endd))

delta = enddate - startdate
numdays=delta.days
for i in range(delta.days + 1):
    day = startdate + timedelta(days=i)
    filenames.append(day)
    
hourly1_filenames=[]
hourly2_filenames=[]
hours=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']    

xmin=98.759
ymin=12.911
xmax=110.142
ymax=23.697
xres=0.045
yres=0.045

nrows=240
ncols=240

geotransform=(xmin,xres,0,ymax,0, -yres)


   
for dx in filenames:
    for dt in hours:
        hourly1='{}T{}{}.tif'.format(dx, dt, clvar1)
        hourly1_filenames.append(hourly1)
        hourly2='{}T{}{}.tif'.format(dx, dt, clvar2)
        hourly2_filenames.append(hourly2)
print('Number of days:{}'.format(numdays))


for x in range(numdays+1):
#    if x ==1:
#        pass
#    else:
    label=hourly1_filenames[(24*x)]
    hour1=rasterio.open(hourly1_filenames[(24*x)-6]) 	#For RAINC
    hour2=rasterio.open(hourly2_filenames[(24*x)-6])	#For RAINNC
    hour24=rasterio.open(hourly1_filenames[(24*x)+17])
    hour25=rasterio.open(hourly2_filenames[(24*x)+17])
    raster1=hour1.read(1)
    raster2=hour2.read(1)
    raster24=hour24.read(1)
    raster25=hour25.read(1)
    total=(raster24+raster25)-(raster1+raster2)
    output_raster = gdal.GetDriverByName('GTiff').Create('AC-{}-rain.tif'.format(label[0:10]),240, 240, 1 ,gdal.GDT_Float32)  # Open the file
    output_raster.SetGeoTransform(geotransform)  # Specify its coordinates
    srs = osr.SpatialReference()                 # Establish its coordinate encoding
    srs.ImportFromEPSG(4326)                     # This one specifies WGS84 lat long.
    output_raster.SetProjection( srs.ExportToWkt() )   # Exports the coordinate system 
                                                           # to the file
    output_raster.GetRasterBand(1).WriteArray(total)   # Writes my array to the raster
        
    output_raster.FlushCache()
         

            
          
            
            
            
        
        


  
    
    
