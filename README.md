# NTL_POP
The project code of spatial matching between the remote sensing data of night lights and the population data in different time periods.

1. Data Processing
(1) Convert the luminous data (raster) to surface SHP, and the code file name is: data_processing_NTL_tif2mshp
(2) Aggregate the population data (CSV) with the code file name: data_processing_POP_excel_sum
(3) The aggregated population data (CSV) is converted to a point shp file, and the code file name is: data_processing_POP_xy2d
(4) Perform in-range summarization (analysis tools) in ArcGIS Pro. Enter the NTL shp and the POP shp of the population in the four periods, the summary field is value, and the statistics are sum. Perform four times, saving the results as four SHP files each.
2. Collinearity test
The nighttime light brightness values and population numbers of the four periods of the shp files were summarized and stored in a CSV file for collinearity test, and the code file name is: Multicollinearity test
3. Bivariate spatial autocorrelation
Calculate the Moran index chart and LISA chart for four periods. The code file name is: LISA
