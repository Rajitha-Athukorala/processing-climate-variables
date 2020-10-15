---This script will generate rasters from the npy files---

Please run this code inside the folder containing the npy files.

Add the required years of data in rasters to the script from the list Years = ['2019','2018']

Change the path to the directory where the files need to be saved in:
 
output_raster_t2max = gdal.GetDriverByName('GTiff').Create('Path//to//folder//T2MAX-{}.tif'.format(file_year[i3]),ncols, nrows, 1 ,gdal.GDT_Float32)

*Recommended to run the script batchwise for if the computing resources are minimal.