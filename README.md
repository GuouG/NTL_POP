# NTL_POP
The project of Spatiotemporal matching between nighttime light intensity and population activity density at different scales. Including the data and code used in the research.

1.data
(1)SDGSAT-1 data: The file name is RGB-B, which is the nighttime light remote sensing data used in the study. Due to the large size of the original image, the preprocessed image was uploaded.
(2)BUD data: The file name is budejan, and the file format is CSV, which records the latitude and longitude and the corresponding number of active population.

2.code
Including NTL and BUD data preprocessing code, as well as the processing of merging the two into vector data, including the calculation of bivariate spatial autocorrelation and consistency indicators.
(1)SDGSAT_CODE：There are a total of 5 Python code files that provide detailed records of the NTL data preprocessing process.
(2)BUD_CODE:There are 2 Python code files in total, detailing the process of merging and converting BUD data into SHP files.
(3)sbl.py：Used for bivariate spatial autocorrelation of data  nighttime light intensity and population activity density.
(4)ci.py：Used to calculate the consistency of bivariate spatial autocorrelation clustering results at different time periods.
