import pandas as pd
import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor

# 读取本地的 Excel 文件
file_path = r'E:\Urban\SH_time\new_0401\result\共线性\virrs_pop.xlsx'  # 修改为你的文件路径
df = pd.read_excel(file_path)

# 提取数据并添加常数列
data = df.iloc[:, :5]
data['constant'] = 1

# 计算相关系数矩阵
correlation_matrix = data.corr()
print("Correlation Matrix:")
print(correlation_matrix)

# 计算VIF
vif_series = pd.Series([variance_inflation_factor(data.values, i) for i in range(data.shape[1])], index=data.columns)
print("\nVIF:")
print(vif_series)
