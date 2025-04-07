import os
import pandas as pd

# 输入文件夹路径
folder_path = r'E:\Experiment\pop_ntl\data\BUD\T4'

# 输出合并后的CSV文件路径
output_csv_path = r'E:\Experiment\pop_ntl\data\BUD\T4\t4.csv'

# 初始化一个空的DataFrame，用于存储合并后的数据
merged_data = pd.DataFrame()

# 遍历文件夹下的所有CSV文件
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        file_path = os.path.join(folder_path, file_name)

        # 读取CSV文件
        csv_data = pd.read_csv(file_path)

        # 根据经纬度进行合并，对人口数据进行求和
        merged_data = pd.concat([merged_data, csv_data.groupby(['wgs84_LNG', 'wgs84_LAT']).agg({'value': 'sum'}).reset_index()])

# 将合并后的数据保存为CSV文件
merged_data.to_csv(output_csv_path, index=False)

print("合并完成，结果保存在:", output_csv_path)
