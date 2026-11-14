import os, sys
import rasterio
import numpy as np
from rasterio.transform import from_origin, xy
from rasterio.windows import Window

print('Rasterio version:', rasterio.__version__)
print('GDAL version:', rasterio.__gdal_version__)

# Create temporary GeoTIFF
tmp_path = os.path.abspath('temp_test.tif')
width, height = 2, 2
data = np.arange(width * height, dtype=rasterio.float32).reshape((height, width))
transform = from_origin(0, 2, 1, 1)
profile = {
    'driver': 'GTiff',
    'height': height,
    'width': width,
    'count': 1,
    'dtype': rasterio.float32,
    'transform': transform,
}
with rasterio.open(tmp_path, 'w', **profile) as dst:
    dst.write(data, 1)
print('Created temporary GeoTIFF at', tmp_path)

# Verify open and read
with rasterio.open(tmp_path) as src:
    arr = src.read(1)
print('Read array:', arr)

# Verify submodule imports
print('Window class:', Window)
print('xy function works:', xy(src.transform, [0, 1], [0, 1]))
