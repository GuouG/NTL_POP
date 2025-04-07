# import arcpy
# arcpy.env.overwriteOutput = True
#
# # 数据路径
# Border = r"../Data/基本数据/ZhengZhou.shp"
# IMG = r"../Data/处理过程/PH_PL_Intersection.tif"
# # 掩膜提取
# mask_img = arcpy.sa.ExtractByMask(
#     in_raster = IMG,
#     in_mask_data = Border,
# )
# mask_img.save("../Data/处理过程/PH_PL_Intersection.tif")

###
import numpy as np
import rasterio
import cv2
import matplotlib.pyplot as plt

# 读取已识别的光区文件
with rasterio.open(r"E:\Experiment\pop_ntl\data\NTL\process\PHL_B_sh.tif") as src:
    illumination = src.read(1)
    meta = src.meta
# 转换为二值图像（0和255）
binary_illumination = (illumination > 0).astype(np.uint8) * 255

# 定义八邻域结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# 执行形态学膨胀（可调整迭代次数）
dilation_iterations = 1  # 控制扩展程度
expanded_illumination = cv2.dilate(
    binary_illumination,
    kernel,
    iterations=dilation_iterations
)
# 保存扩展后的结果
with rasterio.open(r"E:\Experiment\pop_ntl\data\NTL\process\PHL_B_expand.tif", 'w',
                  driver=meta['driver'],
                  height=expanded_illumination.shape[0],
                  width=expanded_illumination.shape[1],
                  count=1,
                  dtype=expanded_illumination.dtype,
                  crs=meta['crs'],
                  transform=meta['transform']) as dst:
    dst.write(expanded_illumination, 1)

# 可视化对比
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title("Original Illumination")
plt.imshow(binary_illumination, cmap='gray')

plt.subplot(1, 3, 2)
plt.title("Expanded Illumination")
plt.imshow(expanded_illumination, cmap='gray')

# 在保存前添加差异可视化
plt.subplot(1, 3, 3)
plt.title("Expansion Difference")
plt.imshow(expanded_illumination - binary_illumination, cmap='Reds')

plt.tight_layout()
plt.show()
#
# #Change Python Environment(arcpy)
# import arcpy
# arcpy.env.overwriteOutput = True
#
# # 数据路径
# Border = r"../Data/基本数据/ZhengZhou.shp"
# IMG = r"../Data/处理过程/Extended_Illumination.tif"
# # 掩膜提取
# mask_img = arcpy.sa.ExtractByMask(
#     in_raster = IMG,
#     in_mask_data = Border,
# )
# mask_img.save("../Data/处理过程/Extended_Illumination.tif")
#
# #光区重采样
# import arcpy
# arcpy.env.overwriteOutput = True
#
# Illumination = r"../Data/处理过程/PH_PL_Intersection.tif"
# Extended_Illumination = r"../Data/处理过程/Extended_Illumination.tif"
# arcpy.management.Resample(
#     in_raster = Illumination,
#     out_raster = r'../Data/处理过程/Illumination_Resample.tif',
#     cell_size = '40',
# )
# arcpy.management.Resample(
#     in_raster = Extended_Illumination,
#     out_raster = r'../Data/处理过程/Extended_Resample.tif',
#     cell_size = '40',
# )