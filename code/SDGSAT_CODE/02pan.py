import numpy as np
import rasterio
import cv2
import matplotlib.pyplot as plt

#处理PL波段
with rasterio.open(r'E:\Experiment\pop_ntl\data\NTL\process\LH_B.tif') as src:
    pl_image = src.read(1)  # 读取第一个波段
    pl_meta = src.meta  # 保存元数据

# 设置阈值
threshold = 3  # 暗电流噪声阈值
S = 1  # 孤立噪声阈值（邻域像素数）

# 去除暗电流噪声
pl_image[pl_image < threshold] = 0

# 去除孤立噪声
binary_image = (pl_image > 0).astype(np.uint8)
neighbor_count = np.zeros_like(binary_image)

# 计算每个像素的8邻域中非零像素数量
for i in range(-1, 2):
    for j in range(-1, 2):
        if i == 0 and j == 0:
            continue  # 跳过中心像素
        # 移动图像并累加邻居数量
        shifted = np.roll(binary_image, (i, j), axis=(0, 1))
        neighbor_count += shifted

# 移除孤立噪声（邻居数小于S的像素）
filtered_image = binary_image.copy()
filtered_image[neighbor_count < S] = 0

# 转换回原始灰度范围
pl_image = filtered_image * 255

# 显示去噪后的全色波段图像
plt.title("Denoised Panchromatic Image")
plt.imshow(pl_image, cmap='gray')
plt.show()

#处理PH波段
with rasterio.open(r'E:\Experiment\pop_ntl\data\NTL\process\LH_B.tif') as src:
    ph_image = src.read(2)  # 读取第二个波段
    ph_meta = src.meta  # 保存元数据

# 设置阈值
threshold = 3  # 暗电流噪声阈值
S = 1  # 孤立噪声阈值（邻域像素数）

# 去除暗电流噪声
ph_image[ph_image < threshold] = 0

# 去除孤立噪声
binary_image = (ph_image > 0).astype(np.uint8)
neighbor_count = np.zeros_like(binary_image)

# 计算每个像素的8邻域中非零像素数量
for i in range(-1, 2):
    for j in range(-1, 2):
        if i == 0 and j == 0:
            continue  # 跳过中心像素
        # 移动图像并累加邻居数量
        shifted = np.roll(binary_image, (i, j), axis=(0, 1))
        neighbor_count += shifted

# 移除孤立噪声（邻居数小于S的像素）
filtered_image = binary_image.copy()
filtered_image[neighbor_count < S] = 0

# 转换回原始灰度范围
ph_image = filtered_image * 255

# 显示去噪后的全色波段图像
plt.title("Denoised Panchromatic Image")
plt.imshow(ph_image, cmap='gray')
plt.show()

#处理PL与PH相交
# 将两个波段转换为二值图像
ph_binary = (ph_image > 0).astype(np.uint8)
pl_binary = (pl_image > 0).astype(np.uint8)

# 执行波段相交操作（逻辑与）
intersection = np.logical_and(ph_binary, pl_binary).astype(np.uint8) * 255

# 显示相交结果
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title("PH Band")
plt.imshow(ph_image, cmap='gray')

plt.subplot(1, 3, 2)
plt.title("PL Band")
plt.imshow(pl_image, cmap='gray')

plt.subplot(1, 3, 3)
plt.title("PH ∩ PL Intersection")
plt.imshow(intersection, cmap='gray')

plt.tight_layout()
plt.show()
# 保存相交结果（可选）
with rasterio.open(r'E:\Experiment\pop_ntl\data\NTL\process\PHL_B.tif', 'w',
        driver = pl_meta['driver'],
        height = intersection.shape[0],
        width = intersection.shape[1],
        count = 1,
        dtype = intersection.dtype,
        crs = pl_meta['crs'],
        transform = pl_meta['transform']
    ) as dst:
        dst.write(intersection, 1)