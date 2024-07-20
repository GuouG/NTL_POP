from osgeo import gdal, ogr, osr
import numpy as np

# 读取tif文件
input_tif = r'E:\Urban\SH_time\new_0401\data\virrs\nighttime_lights202310.tif'
ds = gdal.Open(input_tif)
cols = ds.RasterXSize
rows = ds.RasterYSize
gt = ds.GetGeoTransform()
srs = osr.SpatialReference()
srs.ImportFromWkt(ds.GetProjection())

# 创建面shp文件
output_shp = r'E:\Urban\SH_time\new_0401\data\virrs\virrs.shp'
driver = ogr.GetDriverByName('ESRI Shapefile')
out_ds = driver.CreateDataSource(output_shp)
out_layer = out_ds.CreateLayer('grid', srs, geom_type=ogr.wkbPolygon)
out_layer.CreateField(ogr.FieldDefn('value', ogr.OFTInteger))

# 栅格大小
x_min = gt[0]
y_max = gt[3]
x_max = x_min + cols * gt[1]
y_min = y_max + rows * gt[5]

# 创建面要素
for i in range(rows):
    for j in range(cols):
        ring = ogr.Geometry(ogr.wkbLinearRing)
        ring.AddPoint(x_min + j * gt[1], y_max + i * gt[5])
        ring.AddPoint(x_min + (j + 1) * gt[1], y_max + i * gt[5])
        ring.AddPoint(x_min + (j + 1) * gt[1], y_max + (i + 1) * gt[5])
        ring.AddPoint(x_min + j * gt[1], y_max + (i + 1) * gt[5])
        ring.AddPoint(x_min + j * gt[1], y_max + i * gt[5])
        poly = ogr.Geometry(ogr.wkbPolygon)
        poly.AddGeometry(ring)

        feature = ogr.Feature(out_layer.GetLayerDefn())
        feature.SetGeometry(poly)

        # 设置栅格波段值为面shp字段值
        value = ds.ReadAsArray(j, i, 1, 1)[0, 0]
        if not np.isnan(value):
            feature.SetField('value', int(value))
        #feature.SetField('value', value)
        #feature.SetField('value', int(value))
        out_layer.CreateFeature(feature)

out_ds = None
ds = None
