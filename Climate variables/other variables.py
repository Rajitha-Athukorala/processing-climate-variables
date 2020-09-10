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
clvar = input('Climate variable:')
operation=int(input('What is the operation?: 1 for daily sum; 2 for daily average'))

if operation == 1:
    opr=1
    process='DS'
elif operation ==2:
    opr=24
    process='DA'
else:
    print('Wrong key for operand')
    
    
filenames=[]


startdate =date(int(starty), int(startm), int(startd))
enddate =date(int(endy), int(endm), int(endd))

delta = enddate - startdate
numdays=delta.days
for i in range(delta.days + 1):
    day = startdate + timedelta(days=i)
    filenames.append(day)
    
hourly_filenames=[]
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
        hourly='{}T{}{}.tif'.format(dx, dt, clvar)
        hourly_filenames.append(hourly)
        print(hourly)
print('Number of days:{}'.format(numdays))


for x in range(numdays+1):
    if x ==1:
        pass
    else:
        label=hourly_filenames[(24*x)]
        hour1=rasterio.open(hourly_filenames[(24*x)-6])
        hour2=rasterio.open(hourly_filenames[(24*x)-5])
        hour3=rasterio.open(hourly_filenames[(24*x)-4])
        hour4=rasterio.open(hourly_filenames[(24*x)-3])
        hour5=rasterio.open(hourly_filenames[(24*x)-2])
        hour6=rasterio.open(hourly_filenames[(24*x)-1])
        hour7=rasterio.open(hourly_filenames[(24*x)])
        hour8=rasterio.open(hourly_filenames[(24*x)+1])
        hour9=rasterio.open(hourly_filenames[(24*x)+2])
        hour10=rasterio.open(hourly_filenames[(24*x)+3])
        hour11=rasterio.open(hourly_filenames[(24*x)+4])
        hour12=rasterio.open(hourly_filenames[(24*x)+5])
        hour13=rasterio.open(hourly_filenames[(24*x)+6])
        hour14=rasterio.open(hourly_filenames[(24*x)+7])
        hour15=rasterio.open(hourly_filenames[(24*x)+8])
        hour16=rasterio.open(hourly_filenames[(24*x)+9])
        hour17=rasterio.open(hourly_filenames[(24*x)+10])
        hour18=rasterio.open(hourly_filenames[(24*x)+11])
        hour19=rasterio.open(hourly_filenames[(24*x)+12])
        hour20=rasterio.open(hourly_filenames[(24*x)+13])
        hour21=rasterio.open(hourly_filenames[(24*x)+14])
        hour22=rasterio.open(hourly_filenames[(24*x)+15])
        hour23=rasterio.open(hourly_filenames[(24*x)+16])
        hour24=rasterio.open(hourly_filenames[(24*x)+17])
        raster1=hour1.read(1)
        raster2=hour2.read(1)
        raster3=hour3.read(1)
        raster4=hour4.read(1)
        raster5=hour5.read(1)
        raster6=hour6.read(1)
        raster7=hour7.read(1)
        raster8=hour8.read(1)
        raster9=hour9.read(1)
        raster10=hour10.read(1)
        raster11=hour11.read(1)
        raster12=hour12.read(1)
        raster13=hour13.read(1)
        raster14=hour14.read(1)
        raster15=hour15.read(1)
        raster16=hour16.read(1)
        raster17=hour17.read(1)
        raster18=hour18.read(1)
        raster19=hour19.read(1)
        raster20=hour20.read(1)
        raster21=hour21.read(1)
        raster22=hour22.read(1)
        raster23=hour23.read(1)
        raster24=hour24.read(1)
        total=(raster1+raster2+raster3+raster4+raster5+raster6+raster7+raster8+raster9+raster10+raster11+raster12+raster13+raster14+raster15+raster16+raster17+raster18+raster19+raster20+raster21+raster22+raster23+raster24)/opr
        output_raster = gdal.GetDriverByName('GTiff').Create('{}-{}{}.tif'.format(process,label[0:13],clvar),240, 240, 1 ,gdal.GDT_Float32)  # Open the file
        output_raster.SetGeoTransform(geotransform)  # Specify its coordinates
        srs = osr.SpatialReference()                 # Establish its coordinate encoding
        srs.ImportFromEPSG(4326)                     # This one specifies WGS84 lat long.
        output_raster.SetProjection( srs.ExportToWkt() )   # Exports the coordinate system 
                                                               # to the file
        output_raster.GetRasterBand(1).WriteArray(total)   # Writes my array to the raster
            
        output_raster.FlushCache()
         

            
          
            
            
            
        
        


  
    
    
