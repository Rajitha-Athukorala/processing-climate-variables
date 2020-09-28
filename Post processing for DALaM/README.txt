Task 8 – Generate rasters for climate variables from wrfout, wrfxtrm and wrfcdx files.
Introduction

The task 7 involved the downloading results for the 6 climate variables. This task is the final task in phase2 which involves the generation of raster files for each variable. It also involves the process of generating a .npy file for each variable so that the data can be input to AEZ.

Variable	Statistic	Output duration	IO stream	Variable name
Temperature (2m)	Min	1 day	wrfxtrm	T2MIN
Temperature (2m)	Max	1 day	wrfxtrm	T2MAX
Rainfall	Accumulation	1 day	wrfout	RAINC+RAINNC
Short wave radiation	Average	1 day	wrfout	SWDOWN
Windspeed	Average	1 day	wrfcdx	WSS
Relative humidity	Average	1 day	wrfcdx	HURS

There are 3 main steps involved
1.	Create hourly rasters
2.	Create daily statistic rasters
3.	Create .npy file

To do these 3 tasks, 3 scripts have been written in python. The following libraries are also pre-requisite

a)	rasterio
b)	osgeo
c)	future
d)	netCDF4
e)	numpy
f)	wrf
g)	glob

These libraries can be installed using pip for any preferred IDE.

Scripts
There are 3 mainscripts for processing the data and to generate daily statistics. The model outputs are hourly data (24 steps per day).

Script 1 – raster_out_ncks
This script will output hourly rasters from your model output data.
User inputs
•	Filename – name of the file/path (ex: wrfout_d02_2011-01-30_17:00:00_wrf.nc)
•	Required climate variable (given in the table above)
Output	
•	Hourly raster files for the requested climate variable
Once all the hourly data is generated, copy all the rasters to one folder with the climate variable name.

Script 2 -  rain_processing final/other variables
There are 2 scripts for obtaining daily statistics. One main script for calculating daily rainfall and the other script can be used to obtain daily statistics for all other variables. Run this script inside the folder with all the hourly climate rasters.
rain_processing_final script
User inputs
•	Starting date:
•	Starting month:
•	Starting day:
•	End year:
•	End month:
•	End day:
•	Climate variable1:
•	Climate variable2:
Output
•	Daily accumulation of rainfall
Other variables script
•	Starting date:
•	Starting month:
•	Starting day:
•	End year:
•	End month:
•	End day:
•	Climate variable:
•	What is the operation?: 1 for daily sum; 2 for daily average
Output
•	Daily statistic of the required variable

Script 3 – create npy from rasters
This script will create an npy file from the raster files to be used in AEZ.
User inputs
•	Name of the climate variable/output file name
Output
•	.npy file for the selected climate variable
At the end of this script, you will have a .npy file which can be used for running AEZ.

Help
Please contact Mr. Thaileng Thol or Rajitha Athukorala from AIT for any inquiries. A brief introductory can be arranged upon request. The scripts can be cloned from the github https://github.com/Rajitha-Athukorala/processing-climate-variables.git repository.











