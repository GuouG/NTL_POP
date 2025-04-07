import numpy as np
import rasterio
import cv2
import matplotlib.pyplot as plt

# 分别读取RGB三个波段
with rasterio.open(r'E:\Experiment\pop_ntl\data\NTL\process\Denoised_RGB_B.tif') as rgb_src:
    red_band = rgb_src.read(1)
    green_band = rgb_src.read(2)
    blue_band = rgb_src.read(3)
    RGB_meta = rgb_src.meta

# 辐射校正
red_band = (red_band * 0.0000102744) + 0.0000099253
green_band = (green_band * 0.0000041779) + 0.0000060840
blue_band = (blue_band * 0.0000070119) + 0.0000136754

# 转换单位
red_band = red_band * 294 * 100
green_band = green_band * 106 * 100
blue_band = blue_band * 102 * 100

# 保存结果
RGB_meta.update(count=1)
with rasterio.open(r'E:\Experiment\pop_ntl\data\NTL\radiance\red_band.tif', 'w', **RGB_meta) as dst:
    dst.write(red_band, 1)
with rasterio.open(r'E:\Experiment\pop_ntl\data\NTL\radiance\green_band.tif', 'w', **RGB_meta) as dst:
    dst.write(green_band, 1)
with rasterio.open(r'E:\Experiment\pop_ntl\data\NTL\radiance\blue_band.tif', 'w', **RGB_meta) as dst:
    dst.write(blue_band, 1)



# 计算亮度波段
brightness_band = 0.2989 * red_band + 0.5870 * green_band + 0.1140 * blue_band
# 保存亮度波段
RGB_meta.update(count=1)
with rasterio.open(r'E:\Experiment\pop_ntl\data\NTL\radiance\brightness.tif', 'w', **RGB_meta) as dst:
    dst.write(brightness_band, 1)
# 可视化亮度波段（可选）
plt.imshow(brightness_band, cmap='gray')
plt.title('Brightness Band')
plt.colorbar()
plt.show()

# 波段合成
RGB_meta.update(count=3)
# 保存合成结果
with rasterio.open(r'E:\Experiment\pop_ntl\data\NTL\radiance\RGB_Band.tif', 'w', **RGB_meta) as dst:
    dst.write(red_band, 1)
    dst.write(green_band, 2)
    dst.write(blue_band, 3)