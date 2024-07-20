# import os
# import geopandas as gpd
# from esda.moran import Moran_Local_BV
# import libpysal
# import numpy as np
#
# def bivariate_spatial_autocorrelation(shp_file, field1, field2, output_folder):
#     # 读取Shapefile文件
#     gdf = gpd.read_file(shp_file)
#
#     # 提取字段值
#     variable1 = gdf[field1]
#     variable2 = gdf[field2]
#
#     # 创建权重矩阵
#     w = libpysal.weights.Queen.from_dataframe(gdf)
#
#     # 计算局部 Moran's I 统计量
#     moran_loc_bv = Moran_Local_BV(variable1, variable2, w)
#
#     # 根据 p 值和 LISA 类型对地理数据进行分类
#     lisa_classes = np.zeros(len(gdf), dtype=int)  # 初始化分类结果为0
#
#     # 将不显著相关赋值为0
#     lisa_classes[moran_loc_bv.p_sim >= 0.05] = 0
#
#     # 将高高聚类赋值为1
#     lisa_classes[(moran_loc_bv.p_sim < 0.05) & (moran_loc_bv.q == 1)] = 1
#
#     # 将高低聚类赋值为2
#     lisa_classes[(moran_loc_bv.p_sim < 0.05) & (moran_loc_bv.q == 2)] = 2
#
#     # 将低低聚类赋值为3
#     lisa_classes[(moran_loc_bv.p_sim < 0.05) & (moran_loc_bv.q == 3)] = 3
#
#     # 将低高聚类赋值为4
#     lisa_classes[(moran_loc_bv.p_sim < 0.05) & (moran_loc_bv.q == 4)] = 4
#
#     # 将分类结果添加到原始数据框中
#     gdf['lisa_classes'] = lisa_classes
#
#     # 创建输出文件夹（如果不存在）
#     os.makedirs(output_folder, exist_ok=True)
#
#     # 保存带有分类结果的新Shapefile文件
#     output_shp_file = os.path.join(output_folder, os.path.basename(shp_file).replace('.shp', '_lisa.shp'))
#     gdf.to_file(output_shp_file)
#
# # 指定四个shp文件及其字段对
# shp_files = [
#     ("E:/Urban/SH_time/sh_cai/result_pro_four/virrs_npp.shp", "grid_code", "npp"),
#     ("E:/Urban/SH_time/sh_cai/result_pro_four/virrs_sleep.shp", "grid_code", "sleep"),
#     ("E:/Urban/SH_time/sh_cai/result_pro_four/virrs_work.shp", "grid_code", "work"),
#     ("E:/Urban/SH_time/sh_cai/result_pro_four/virrs_all.shp", "grid_code", "all")
# ]
#
# # 指定输出文件夹
# output_folder = "E:/Urban/SH_time/four_type"
#
# # 对每个shp文件进行双变量空间自相关分析并保存结果
# for shp_file, field1, field2 in shp_files:
#     bivariate_spatial_autocorrelation(shp_file, field1, field2, output_folder)

# import os
# import geopandas as gpd
# from esda.moran import Moran_Local_BV
# import libpysal
# import numpy as np
# import matplotlib.pyplot as plt
#
# def bivariate_spatial_autocorrelation(shp_file, field1, field2, output_folder):
#     # 读取Shapefile文件
#     gdf = gpd.read_file(shp_file)
#
#     # 提取字段值
#     variable1 = gdf[field1]
#     variable2 = gdf[field2]
#
#     # 创建权重矩阵
#     w = libpysal.weights.Queen.from_dataframe(gdf)
#
#     # 计算局部 Moran's I 统计量
#     moran_loc_bv = Moran_Local_BV(variable1, variable2, w)
#
#     # 根据 p 值和 LISA 类型对地理数据进行分类
#     lisa_classes = np.zeros(len(gdf), dtype=int)  # 初始化分类结果为0
#
#     # 将不显著相关赋值为0
#     lisa_classes[moran_loc_bv.p_sim >= 0.05] = 0
#
#     # 将高高聚类赋值为1
#     lisa_classes[(moran_loc_bv.p_sim < 0.05) & (moran_loc_bv.q == 1)] = 1
#
#     # 将高低聚类赋值为2
#     lisa_classes[(moran_loc_bv.p_sim < 0.05) & (moran_loc_bv.q == 2)] = 2
#
#     # 将低低聚类赋值为3
#     lisa_classes[(moran_loc_bv.p_sim < 0.05) & (moran_loc_bv.q == 3)] = 3
#
#     # 将低高聚类赋值为4
#     lisa_classes[(moran_loc_bv.p_sim < 0.05) & (moran_loc_bv.q == 4)] = 4
#
#     # 将分类结果添加到原始数据框中
#     gdf['lisa_classes'] = lisa_classes
#
#     # 创建输出文件夹（如果不存在）
#     os.makedirs(output_folder, exist_ok=True)
#
#     # 保存带有分类结果的新Shapefile文件
#     output_shp_file = os.path.join(output_folder, os.path.basename(shp_file).replace('.shp', '_lisa.shp'))
#     gdf.to_file(output_shp_file)
#
#     # 生成LISA图
#     fig, ax = plt.subplots(figsize=(10, 8))
#     gdf.plot(column='lisa_classes', categorical=True, legend=True, linewidth=0.1, ax=ax)
#     ax.set_title('LISA Map for ' + os.path.basename(shp_file))
#     plt.savefig(os.path.join(output_folder, os.path.basename(shp_file).replace('.shp', '_lisa.png')))
#     plt.close()
#
#     # 生成莫兰指数图
#     fig, ax = plt.subplots(figsize=(10, 8))
#     libpysal.viz.plot_local_autocorrelation(moran_loc_bv, gdf, ax=ax, p=0.05)
#     ax.set_title('Local Moran\'s I Map for ' + os.path.basename(shp_file))
#     plt.savefig(os.path.join(output_folder, os.path.basename(shp_file).replace('.shp', '_moran.png')))
#     plt.close()
#
# # 指定四个shp文件及其字段对
# shp_files = [
#     (r"E:\Urban\SH_time\new_0325\data\npp_pop\virrs_npp.shp", "gridcode", "sum_value"),
#     (r"E:\Urban\SH_time\new_0325\data\npp_pop\virrs_sleep.shp", "gridcode", "sum_value"),
#     (r"E:\Urban\SH_time\new_0325\data\npp_pop\virrs_work.shp", "gridcode", "sum_value"),
#     (r"E:\Urban\SH_time\new_0325\data\npp_pop\virrs_all.shp", "gridcode", "sum_value")
# ]
#
# # 指定输出文件夹
# output_folder = r"E:\Urban\SH_time\new_0325\data\sbl"
#
# # 对每个shp文件进行双变量空间自相关分析并保存结果
# for shp_file, field1, field2 in shp_files:
#     bivariate_spatial_autocorrelation(shp_file, field1, field2, output_folder)

# import os
# import geopandas as gpd
# from esda.moran import Moran_Local_BV
# import libpysal
# import esda
# import numpy as np
# import matplotlib.pyplot as plt
#
#
#
# def bivariate_spatial_autocorrelation(shp_file, field1, field2, output_folder):
#     # 读取Shapefile文件
#     gdf = gpd.read_file(shp_file)
#
#     # 提取字段值
#     variable1 = gdf[field1]
#     variable2 = gdf[field2]
#
#     # 创建权重矩阵
#     w = libpysal.weights.Queen.from_dataframe(gdf)
#
#     # 计算局部 Moran's I 统计量
#     moran_loc_bv = Moran_Local_BV(variable1, variable2, w)
#
#     # 根据 p 值和 LISA 类型对地理数据进行分类
#     lisa_classes = np.zeros(len(gdf), dtype=int)  # 初始化分类结果为0
#
#     # 将不显著相关赋值为0
#     lisa_classes[moran_loc_bv.p_sim >= 0.05] = 0
#
#     # 将高高聚类赋值为1
#     lisa_classes[(moran_loc_bv.p_sim < 0.05) & (moran_loc_bv.q == 1)] = 1
#
#     # 将高低聚类赋值为2
#     lisa_classes[(moran_loc_bv.p_sim < 0.05) & (moran_loc_bv.q == 2)] = 2
#
#     # 将低低聚类赋值为3
#     lisa_classes[(moran_loc_bv.p_sim < 0.05) & (moran_loc_bv.q == 3)] = 3
#
#     # 将低高聚类赋值为4
#     lisa_classes[(moran_loc_bv.p_sim < 0.05) & (moran_loc_bv.q == 4)] = 4
#
#     # 将分类结果添加到原始数据框中
#     gdf['lisa_classes'] = lisa_classes
#
#     # 创建输出文件夹（如果不存在）
#     os.makedirs(output_folder, exist_ok=True)
#
#     # 保存带有分类结果的新Shapefile文件
#     output_shp_file = os.path.join(output_folder, os.path.basename(shp_file).replace('.shp', '_lisa.shp'))
#     gdf.to_file(output_shp_file)
#
#     # 生成LISA图
#     fig, ax = plt.subplots(figsize=(10, 8))
#     gdf.plot(column='lisa_classes', categorical=True, legend=True, linewidth=0.1, ax=ax)
#     ax.set_title('LISA Map for ' + os.path.basename(shp_file))
#     plt.savefig(os.path.join(output_folder, os.path.basename(shp_file).replace('.shp', '_lisa.png')))
#     plt.close()
#
#     # 生成莫兰指数图
#     fig, ax = plt.subplots(figsize=(10, 8))
#     esda.plot_local_autocorrelation(moran_loc_bv, gdf, ax=ax, p=0.05)
#     ax.set_title('Local Moran\'s I Map for ' + os.path.basename(shp_file))
#     plt.savefig(os.path.join(output_folder, os.path.basename(shp_file).replace('.shp', '_moran.png')))
#     plt.close()
#
# # 指定四个shp文件及其字段对
# shp_files = [
#     (r"E:\Urban\SH_time\new_0325\data\npp_pop\virrs_npp.shp", "gridcode", "sum_value"),
#     (r"E:\Urban\SH_time\new_0325\data\npp_pop\virrs_sleep.shp", "gridcode", "sum_value"),
#     (r"E:\Urban\SH_time\new_0325\data\npp_pop\virrs_work.shp", "gridcode", "sum_value"),
#     (r"E:\Urban\SH_time\new_0325\data\npp_pop\virrs_all.shp", "gridcode", "sum_value")
# ]
#
# # 指定输出文件夹
# output_folder = r"E:\Urban\SH_time\new_0325\data\sbl"
#
# # 对每个shp文件进行双变量空间自相关分析并保存结果
# for shp_file, field1, field2 in shp_files:
#     bivariate_spatial_autocorrelation(shp_file, field1, field2, output_folder)

import os
import geopandas as gpd
from esda.moran import Moran_Local_BV
import libpysal
import numpy as np
import matplotlib.pyplot as plt
from splot.esda import plot_local_autocorrelation

def bivariate_spatial_autocorrelation(shp_file, field1, field2, output_folder):
    # 读取Shapefile文件
    gdf = gpd.read_file(shp_file)

    # 提取字段值
    variable1 = gdf[field1]
    variable2 = gdf[field2]

    # 创建权重矩阵
    w = libpysal.weights.Queen.from_dataframe(gdf)

    # 计算局部 Moran's I 统计量
    moran_loc_bv = Moran_Local_BV(variable1, variable2, w)

    # 根据 p 值和 LISA 类型对地理数据进行分类
    lisa_classes = np.zeros(len(gdf), dtype=int)  # 初始化分类结果为0

    # 将不显著相关赋值为0
    lisa_classes[moran_loc_bv.p_sim >= 0.05] = 0

    # 将高高聚类赋值为1
    lisa_classes[(moran_loc_bv.p_sim < 0.05) & (moran_loc_bv.q == 1)] = 1

    # 将高低聚类赋值为2
    lisa_classes[(moran_loc_bv.p_sim < 0.05) & (moran_loc_bv.q == 2)] = 2

    # 将低低聚类赋值为3
    lisa_classes[(moran_loc_bv.p_sim < 0.05) & (moran_loc_bv.q == 3)] = 3

    # 将低高聚类赋值为4
    lisa_classes[(moran_loc_bv.p_sim < 0.05) & (moran_loc_bv.q == 4)] = 4

    # 将分类结果添加到原始数据框中
    gdf['lisa_classes'] = lisa_classes

    # 创建输出文件夹（如果不存在）
    os.makedirs(output_folder, exist_ok=True)

    # 保存带有分类结果的新Shapefile文件
    output_shp_file = os.path.join(output_folder, os.path.basename(shp_file).replace('.shp', '_lisa.shp'))
    gdf.to_file(output_shp_file)

    # 生成LISA图
    fig, ax = plt.subplots(figsize=(10, 8))
    gdf.plot(column='lisa_classes', categorical=True, legend=True, linewidth=0.1, ax=ax)
    ax.set_title('LISA Map for ' + os.path.basename(shp_file))
    plt.savefig(os.path.join(output_folder, os.path.basename(shp_file).replace('.shp', '_lisa.png')))
    plt.close()

    # 生成莫兰指数图
    fig, ax = plt.subplots(figsize=(10, 8))
    plot_local_autocorrelation(moran_loc_bv, gdf, attribute='lisa_classes', p=0.05)
    ax.set_title('Local Moran\'s I Map for ' + os.path.basename(shp_file))
    plt.savefig(os.path.join(output_folder, os.path.basename(shp_file).replace('.shp', '_moran.png')))
    plt.close()

# 指定四个shp文件及其字段对
shp_files = [
    (r"E:\Urban\SH_time\new_0401\xz\virrs_npp.shp", "sum_value", "sum_value_"),
    (r"E:\Urban\SH_time\new_0401\xz\virrs_sleep.shp", "sum_value", "sum_value_"),
    (r"E:\Urban\SH_time\new_0401\xz\virrs_work.shp", "sum_value", "sum_value_"),
    (r"E:\Urban\SH_time\new_0401\xz\virrs_all.shp", "sum_value", "sum_value_")
]

# 指定输出文件夹
output_folder = r"E:\Urban\SH_time\new_0401\xz\result\SBL"

# 对每个shp文件进行双变量空间自相关分析并保存结果
for shp_file, field1, field2 in shp_files:
    bivariate_spatial_autocorrelation(shp_file, field1, field2, output_folder)


