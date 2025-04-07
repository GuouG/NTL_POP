#arcpy.management.XYTableToPoint("04.csv", r"D:\Experiment\urban_mismatches\04_allmonth\202304\xy2d.shp", "wgs84_LNG", "wgs84_LAT", None, 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision')


# import arcpy
# arcpy.env.workspace = r"c:\output.gdb"
# arcpy.management.XYTableToPoint(r"D:\Experiment\urban_mismatches\04_allmonth\202304\04.csv", "D:\Experiment\urban_mismatches\04_allmonth\py_xy2d\xy2d.shp","wgs84_LNG", "wgs84_LAT", None,
#                                 arcpy.SpatialReference(4759, 115700))

# XYTableToPoint.py
# Description: Creates a point feature class from input table

# import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = r"c:\output.gdb"

# Set the local variables
in_table = r"E:\Experiment\pop_ntl\data\BUD\T4\t4.csv"
out_feature_class = r"E:\Experiment\pop_ntl\data\BUD\pop_shp\T4\t4.shp"
x_coords = "wgs84_LNG"
y_coords = "wgs84_LAT"
z_coords = None

# Make the XY event layer...
arcpy.management.XYTableToPoint(in_table, out_feature_class,
                                x_coords, y_coords, z_coords,
                                arcpy.SpatialReference(4759, 115700))

# Print the total rows
print(arcpy.management.GetCount(out_feature_class))







