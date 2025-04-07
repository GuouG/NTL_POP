import numpy as np
import rasterio
import cv2
import matplotlib.pyplot as plt

# 读取RGB原始影像
with rasterio.open(r'E:\Experiment\pop_ntl\data\NTL\process\RGB_B.tif') as rgb_src:
    rgb_data = rgb_src.read()  # 读取所有波段
    rgb_meta = rgb_src.meta

# 读取光区影像
with rasterio.open(r'E:\Experiment\pop_ntl\data\NTL\process\PHL_B_expand_40.tif') as illumination_src:
    illumination_data = illumination_src.read(1)
    illumination_meta = illumination_src.meta

# 创建二值掩膜(0/1)
illumination_mask = (illumination_data > 0).astype(np.uint8)

# 强制尺寸对齐处理(微小差距可用)
from rasterio.warp import reproject, Resampling

if illumination_mask.shape != rgb_data[0].shape:
    # 创建目标数组
    resampled_mask = np.zeros(rgb_data[0].shape, dtype=np.uint8)

    # 执行重采样(最近邻插值)
    reproject(
        source=illumination_mask,
        destination=resampled_mask,
        src_transform=illumination_meta['transform'],
        dst_transform=rgb_meta['transform'],
        src_crs=illumination_meta['crs'],
        dst_crs=rgb_meta['crs'],
        resampling=Resampling.nearest
    )
    illumination_mask = resampled_mask

# 对每个RGB波段应用掩膜
denoised_rgb = np.zeros_like(rgb_data)
for band in range(rgb_data.shape[0]):
    denoised_rgb[band] = rgb_data[band] * illumination_mask  # 现在尺寸一致

# 更新元数据
rgb_meta.update(dtype=denoised_rgb.dtype)
# # 保存去噪结果
# with rasterio.open(r'E:\Urban\Urban_boundary\YRD\ntl\data\process\Denoised_RGB_1.tif', 'w', **rgb_meta) as dst:
#     dst.write(denoised_rgb)
#
# # 可视化结果（显示第3波段示例）
# plt.figure(figsize=(12, 6))
#
# plt.subplot(1, 2, 1)
# plt.title("原始RGB波段3")
# plt.imshow(rgb_data[2], cmap='Reds')
#
# plt.subplot(1, 2, 2)
# plt.title("去噪后RGB波段3")
# plt.imshow(denoised_rgb[2], cmap='Reds')
#
# plt.tight_layout()
# plt.show()

# 保存去噪结果
with rasterio.open(r'E:\Experiment\pop_ntl\data\NTL\process\Denoised_RGB_B.tif', 'w', **rgb_meta) as dst:
    dst.write(denoised_rgb)

# 可视化结果（RGB合成显示）
plt.figure(figsize=(12, 6))

# 原始RGB合成
plt.subplot(1, 2, 1)
plt.title("Pre-Processing RGB Composite (Band Order: R-G-B)")
# 彩色合成
rgb_display = np.clip(rgb_data[[0,1,2]].transpose(1,2,0)/255, 0, 1)  # 16bit数据除以65535
plt.imshow(rgb_display)

# 去噪后RGB合成
plt.subplot(1, 2, 2)
plt.title("Denoised RGB Composite (Band Order: R-G-B)")
# 彩色合成
denoised_display = np.clip(denoised_rgb[[0,1,2]].transpose(1,2,0)/255, 0, 1)
plt.imshow(denoised_display)

plt.tight_layout()
plt.show()
