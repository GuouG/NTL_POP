import arcpy
arcpy.env.overwriteOutput = True

# 数据路径
Border = r"../Data/基本数据/ZhengZhou.shp"
LH = r"../Data/原始影像/LH.tif"
RGB = r"../Data/原始影像/RGB.tif"

LH_Mask = arcpy.sa.ExtractByMask(
    in_raster = LH,
    in_mask_data = Border,
)
LH_Mask.save("../Data/掩膜提取/LH.tif")

RGB_Mask = arcpy.sa.ExtractByMask(
    in_raster = RGB,
    in_mask_data = Border,
)
RGB_Mask.save("../Data/掩膜提取/RGB.tif")