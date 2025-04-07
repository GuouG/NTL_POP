import os
import pandas as pd

# 定义文件夹路径
folder_path = r'E:\Experiment\pop_ntl\data\CI'  # 替换为你的文件夹路径
output_file = r'E:\Experiment\pop_ntl\data\CI\output_result.xlsx'  # 输出文件名

# 初始化一个字典来存储结果
results = []

# 遍历文件夹中的所有文件
for file_name in os.listdir(folder_path):
    if file_name.endswith('.xlsx'):
        file_path = os.path.join(folder_path, file_name)

        # 读取Excel文件
        df = pd.read_excel(file_path)

        # 统计四个字段同时为0、1、2、3、4的数量
        count_0 = df[(df['LISA_CL_t1'] == 0) & (df['LISA_CL_t3'] == 0) &
                     (df['LISA_CL_t2'] == 0) & (df['LISA_CL_t4'] == 0)].shape[0]
        count_1 = df[(df['LISA_CL_t1'] == 1) & (df['LISA_CL_t3'] == 1) &
                     (df['LISA_CL_t2'] == 1) & (df['LISA_CL_t4'] == 1)].shape[0]
        count_2 = df[(df['LISA_CL_t1'] == 2) & (df['LISA_CL_t3'] == 2) &
                     (df['LISA_CL_t2'] == 2) & (df['LISA_CL_t4'] == 2)].shape[0]
        count_3 = df[(df['LISA_CL_t1'] == 3) & (df['LISA_CL_t3'] == 3) &
                     (df['LISA_CL_t2'] == 3) & (df['LISA_CL_t4'] == 3)].shape[0]
        count_4 = df[(df['LISA_CL_t1'] == 4) & (df['LISA_CL_t3'] == 4) &
                     (df['LISA_CL_t2'] == 4) & (df['LISA_CL_t4'] == 4)].shape[0]

        # 将结果保存到字典中
        results.append({
            'File': file_name,
            'Count_0': count_0,
            'Count_1': count_1,
            'Count_2': count_2,
            'Count_3': count_3,
            'Count_4': count_4
        })

# 将结果转换为DataFrame
result_df = pd.DataFrame(results)

# 保存结果到Excel文件
result_df.to_excel(output_file, index=False)

print(f"结果已保存到 {output_file}")