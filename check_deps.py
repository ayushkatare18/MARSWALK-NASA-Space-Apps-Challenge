import sys
try:
    import rasterio
    print('rasterio version', rasterio.__version__)
except Exception as e:
    print('rasterio import error:', e)

try:
    import numpy
    print('numpy version', numpy.__version__)
except Exception as e:
    print('numpy import error:', e)

try:
    from PIL import Image
    print('Pillow version', Image.__version__)
except Exception as e:
    print('Pillow import error:', e)

try:
    from fastapi import FastAPI
    print('FastAPI import success')
except Exception as e:
    print('FastAPI import error:', e)
