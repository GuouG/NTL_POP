# import geopandas as gpd
# from esda.moran import Moran_Local_BV
# import libpysal
# import numpy as np
# import matplotlib.pyplot as plt
# from splot.esda import lisa_cluster
#
# # 读取空间数据文件，例如 shapefile
# file_path = 'D:\\Experiment\\urban_mismatches\\SH\\04_huizong\\04_0102\\pro_new\\huizong.shp'
# gdf = gpd.read_file(file_path)
#
# # 假设 gdf 包含两个变量，例如 'variable1' 和 'variable2'
# variable1 = gdf['gridcode']
# variable2 = gdf['sum_value']
#
# # 创建权重矩阵
# w = libpysal.weights.Queen.from_dataframe(gdf)
#
# # 计算局部 Moran's I 统计量
# moran_loc_bv = Moran_Local_BV(variable1, variable2, w)
#
# # 创建 GeoDataFrame 添加 Z 分数和 p 值列
# lisa_df = gdf.copy()
# lisa_df['LISA_Z'] = moran_loc_bv.Is
# lisa_df['LISA_p'] = moran_loc_bv.p_sim
#
# # 绘制 LISA 图
# fig, ax = plt.subplots(figsize=(12, 8))
# lisa_cluster(moran_loc_bv, gdf, p=0.05, ax=ax)
#
# # 保存 LISA 图
# lisa_plot_path = 'D:/Experiment/urban_mismatches/1128test/LISA_plot.png'
# plt.savefig(lisa_plot_path)
# plt.show()
#
# # 定义函数判断 LISA 类别
# def lisa_cluster_category(lisa_z, lisa_p):
#     if np.isnan(lisa_z) or np.isnan(lisa_p):
#         return 'NS'  # 未分类
#     elif lisa_z > 0 and lisa_p <= 0.05:
#         return 'HH'  # 高-高集群
#     elif lisa_z < 0 and lisa_p <= 0.05:
#         return 'LL'  # 低-低集群
#     elif lisa_z > 0 and lisa_p > 0.05:
#         return 'HL'  # 高-低集群
#     elif lisa_z < 0 and lisa_p > 0.05:
#         return 'LH'  # 低-高集群
#     else:
#         return 'NS'  # 不显著
#
# # 根据 LISA 类别创建 GeoDataFrame
# lisa_df['LISA_Category'] = lisa_df.apply(lambda row: lisa_cluster_category(row['LISA_Z'], row['LISA_p']), axis=1)
#
# # 按照不同 LISA 类别保存为不同的 shapefile 文件
# for category in ['HH', 'HL', 'LH', 'LL', 'NS']:
#     category_gdf = lisa_df[lisa_df['LISA_Category'] == category]
#     category_file_path = f'D:/Experiment/urban_mismatches/1128test/LISA_category/LISA_category_{category}.shp'
#     category_gdf.to_file(category_file_path)
#
# print("LISA 图和分类结果已保存为新的 shapefile 文件。")
#
#
# import geopandas as gpd
# from esda.moran import Moran_Local_BV
# import libpysal
# import numpy as np
# import matplotlib.pyplot as plt
# from splot.esda import lisa_cluster
#
# # 读取空间数据文件，例如 shapefile
# file_path = 'E:\\Urban\\SH_time\\result\\vansw.shp'
# gdf = gpd.read_file(file_path)
#
# # 假设 gdf 包含两个变量，例如 'variable1' 和 'variable2'
# variable1 = gdf['gridcode']
# variable2 = gdf['all']
# variable3 = gdf['npp']
# variable4 = gdf['sleep']
# variable5 = gdf['work']
#
# # 创建权重矩阵
# w_variable2 = libpysal.weights.Queen.from_dataframe(gdf)
# w_variable3 = libpysal.weights.Queen.from_dataframe(gdf)
# w_variable4 = libpysal.weights.Queen.from_dataframe(gdf)
# w_variable5 = libpysal.weights.Queen.from_dataframe(gdf)
#
# # 计算局部 Moran's I 统计量
# moran_loc_bv_variable2 = Moran_Local_BV(variable2, variable1, w_variable2)
# moran_loc_bv_variable3 = Moran_Local_BV(variable3, variable1, w_variable3)
# moran_loc_bv_variable4 = Moran_Local_BV(variable4, variable1, w_variable4)
# moran_loc_bv_variable5 = Moran_Local_BV(variable5, variable1, w_variable5)
#
# # 创建 GeoDataFrame 添加 Z 分数和 p 值列
# lisa_df_variable2 = gdf.copy()
# lisa_df_variable3 = gdf.copy()
# lisa_df_variable4 = gdf.copy()
# lisa_df_variable5 = gdf.copy()
#
# lisa_df_variable2['LISA_Z'] = moran_loc_bv_variable2.Is
# lisa_df_variable2['LISA_p'] = moran_loc_bv_variable2.p_sim
# lisa_df_variable3['LISA_Z'] = moran_loc_bv_variable3.Is
# lisa_df_variable3['LISA_p'] = moran_loc_bv_variable3.p_sim
# lisa_df_variable4['LISA_Z'] = moran_loc_bv_variable4.Is
# lisa_df_variable4['LISA_p'] = moran_loc_bv_variable4.p_sim
# lisa_df_variable5['LISA_Z'] = moran_loc_bv_variable5.Is
# lisa_df_variable5['LISA_p'] = moran_loc_bv_variable5.p_sim
#
# # 绘制 LISA 图
# fig, ax = plt.subplots(2, 2, figsize=(18, 18))
#
# lisa_cluster(moran_loc_bv_variable2, gdf, p=0.05, ax=ax[0, 0])
# ax[0, 0].set_title('LISA Cluster of all vs. virrs')
#
# lisa_cluster(moran_loc_bv_variable3, gdf, p=0.05, ax=ax[0, 1])
# ax[0, 1].set_title('LISA Cluster of npp vs. virrs')
#
# lisa_cluster(moran_loc_bv_variable4, gdf, p=0.05, ax=ax[1, 0])
# ax[1, 0].set_title('LISA Cluster of sleep vs. virrs')
#
# lisa_cluster(moran_loc_bv_variable5, gdf, p=0.05, ax=ax[1, 1])
# ax[1, 1].set_title('LISA Cluster of work vs. virrs')
#
# # 保存 LISA 图
# plt.savefig('E:/Urban/SH_time/sbl_result/LISA_plot_variable2_variable5.png')
# plt.show()
#
# import geopandas as gpd
# from esda.moran import Moran_BV
# from esda.moran import Moran_Local_BV
# import libpysal
# import numpy as np
# import matplotlib.pyplot as plt
# from splot.esda import lisa_cluster, plot_moran_bv_simulation, moran_scatterplot, plot_moran_bv
#
# # 读取空间数据文件，例如 shapefile
# file_path = 'E:\\Urban\\SH_time\\result\\vansw.shp'
# gdf = gpd.read_file(file_path)
#
# # 假设 gdf 包含五个变量，例如 'gridcode', 'all', 'npp', 'sleep', 'work'
# variable_names = ['gridcode', 'all', 'npp', 'sleep', 'work']
#
# # 创建空列表存储 Moran 对象和 GeoDataFrame
# moran_objects = []
# lisa_dfs = []
#
# # 遍历变量计算莫兰指数和 LISA
# for i in range(1, len(variable_names)):
#     # 提取变量
#     variable1 = gdf['gridcode']
#     variable2 = gdf[variable_names[i]]
#
#     # 创建权重矩阵
#     w = libpysal.weights.Queen.from_dataframe(gdf)
#
#     # 计算莫兰指数
#     moran_bv = Moran_BV(variable2, variable1, w)
#
#     # 计算局部 Moran's I 统计量
#     moran_loc_bv = Moran_Local_BV(variable2, variable1, w)
#
#     # 创建 GeoDataFrame 添加 Z 分数和 p 值列
#     lisa_df = gdf.copy()
#     lisa_df['LISA_Z'] = moran_loc_bv.Is
#     lisa_df['LISA_p'] = moran_loc_bv.p_sim
#
#     # 存储 Moran 对象和 GeoDataFrame
#     moran_objects.append((moran_bv, moran_loc_bv))
#     lisa_dfs.append(lisa_df)
#
# # 绘制 LISA 图、P 值分布图和莫兰指数散点图
# for i in range(len(variable_names) - 1):
#     fig, axes = plt.subplots(3, 1, figsize=(12, 18))
#
#     # 绘制 LISA 图
#     lisa_cluster(moran_objects[i][1], gdf, p=0.05, ax=axes[0])
#     axes[0].set_title(f'LISA Cluster of {variable_names[i+1]} vs. virrs')
#
#     # 绘制 P 值分布图
#     plot_moran_bv(moran_objects[i][0], zstandard=True, ax=axes[1])
#     axes[1].set_title(f'Moran BV P-value Distribution of {variable_names[i+1]} vs. virrs')
#
#     # 绘制莫兰指数散点图
#     moran_scatterplot(moran_objects[i][0], ax=axes[2], p=0.05)
#     axes[2].set_title(f'Moran BV Scatterplot of {variable_names[i+1]} vs. virrs')
#
#     # 保存图像
#     plt.savefig(f'E:/Urban/SH_time/sbl_result/{variable_names[i+1]}_moran_plot.png')
#     plt.show()
#
# fig, axes = plt.subplots(2, 2, figsize=(18, 18))
#
# for i, ax in enumerate(axes.flatten()):
#     moran_scatterplot(moran_objects[i][0], ax=ax)
#     ax.set_title(f"变量 {i+1} 的莫兰指数散点图")
#
# plt.tight_layout()
# plt.savefig('E:/Urban/SH_time/sbl_result/moran_scatterplots.png')
# plt.show()


# import geopandas as gpd
# from esda.moran import Moran_Local_BV
# import libpysal
# import numpy as np
# import matplotlib.pyplot as plt
# from splot.esda import plot_moran_bv_simulation, moran_scatterplot, plot_moran_bv, lisa_cluster
#
# # 定义函数实现双变量空间自相关分析和绘图保存
# def bivariate_spatial_autocorrelation(shp_file_path, variable1_name, variable2_name, output_folder):
#     # 读取Shapefile文件
#     gdf = gpd.read_file(shp_file_path)
#
#     # 提取变量值
#     variable1 = gdf[variable1_name]
#     variable2 = gdf[variable2_name]
#
#     # 创建权重矩阵
#     w = libpysal.weights.Queen.from_dataframe(gdf)
#
#     # 计算局部 Moran's I 统计量
#     moran_loc_bv = Moran_Local_BV(variable1, variable2, w)
#
#     # 创建 GeoDataFrame 添加 Z 分数和 p 值列
#     lisa_df = gdf.copy()
#     lisa_df['LISA_Z'] = moran_loc_bv.Is
#     lisa_df['LISA_p'] = moran_loc_bv.p_sim
#
#     # 绘制莫兰指数散点图
#     moran_scatterplot(moran_loc_bv, p=0.05)
#     plt.title(f"{variable1_name} vs. {variable2_name}")
#     plt.savefig(f"{output_folder}/moran_scatterplot_{variable1_name}_{variable2_name}.png")
#     plt.close()
#
#     # 绘制莫兰指数 P 值图
#     plot_moran_bv(moran_loc_bv, zstandard=True, figsize=(10, 10))
#     plt.title(f"{variable1_name} vs. {variable2_name}")
#     plt.savefig(f"{output_folder}/moran_pvalue_{variable1_name}_{variable2_name}.png")
#     plt.close()
#
#     # 绘制 LISA 图
#     fig, ax = plt.subplots(figsize=(12, 8))
#     lisa_cluster(moran_loc_bv, gdf, p=0.05, ax=ax)
#     plt.title(f"LISA Cluster of {variable1_name} vs. {variable2_name}")
#     plt.savefig(f"{output_folder}/lisa_cluster_{variable1_name}_{variable2_name}.png")
#     plt.close()
#
# # 定义四个Shapefile文件和对应的变量
# shp_files = ['E:/Urban/SH_time/result/vansw.shp', 'E:/Urban/SH_time/result/vansw.shp', 'E:/Urban/SH_time/result/vansw.shp', 'E:/Urban/SH_time/result/vansw.shp']
# variables = [('gridcode', 'all'), ('gridcode', 'npp'), ('gridcode', 'sleep'), ('gridcode', 'work')]
#
# # 执行双变量空间自相关分析和绘图保存
# for i, shp_file in enumerate(shp_files):
#     variable1_name, variable2_name = variables[i]
#     output_folder = f"E:/Urban/SH_time/four_result/output_folder_{i+1}"
#     bivariate_spatial_autocorrelation(shp_file, variable1_name, variable2_name, output_folder)


import geopandas as gpd
from esda.moran import Moran_Local_BV
import libpysal
import numpy as np
import matplotlib.pyplot as plt
from splot.esda import plot_moran_bv_simulation, moran_scatterplot, plot_moran_bv, lisa_cluster
import os

# 定义函数实现双变量空间自相关分析和绘图保存
def bivariate_spatial_autocorrelation(shp_file_path, field1, field2, output_folder):
    # 读取Shapefile文件
    gdf = gpd.read_file(shp_file_path)

    # 提取字段值
    variable1 = gdf[field1]
    variable2 = gdf[field2]

    # 创建权重矩阵
    w = libpysal.weights.Queen.from_dataframe(gdf)

    # 计算局部 Moran's I 统计量
    moran_loc_bv = Moran_Local_BV(variable1, variable2, w)

    # 创建 GeoDataFrame 添加 Z 分数和 p 值列
    lisa_df = gdf.copy()
    lisa_df['LISA_Z'] = moran_loc_bv.Is
    lisa_df['LISA_p'] = moran_loc_bv.p_sim

    # 创建输出文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 绘制莫兰指数散点图
    moran_scatterplot(moran_loc_bv, p=0.05)
    plt.title(f"{field1} vs. {field2}")
    plt.savefig(f"{output_folder}/moran_scatterplot_{field1}_{field2}.png")
    plt.close()

    # 绘制莫兰指数 P 值图
    plot_moran_bv(moran_loc_bv, zstandard=True, figsize=(10, 10))
    plt.title(f"{field1} vs. {field2}")
    plt.savefig(f"{output_folder}/moran_pvalue_{field1}_{field2}.png")
    plt.close()

    # 绘制 LISA 图
    fig, ax = plt.subplots(figsize=(12, 8))
    lisa_cluster(moran_loc_bv, gdf, p=0.05, ax=ax)
    plt.title(f"LISA Cluster of {field1} vs. {field2}")
    plt.savefig(f"{output_folder}/lisa_cluster_{field1}_{field2}.png")
    plt.close()

# 定义字段列表和Shapefile文件路径
shp_file_path = 'E:/Urban/SH_time/result/vansw.shp'
fields = ['gridcode', 'all', 'npp', 'sleep', 'work']

# 执行双变量空间自相关分析和绘图保存
for i, field1 in enumerate(fields):
    for j, field2 in enumerate(fields):
        if i < j:
            output_folder = f"E:/Urban/SH_time/four_result/output_folder_{i+1}_{j+1}"
            bivariate_spatial_autocorrelation(shp_file_path, field1, field2, output_folder)
