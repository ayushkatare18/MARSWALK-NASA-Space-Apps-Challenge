import sys
from pathlib import Path

try:
    import rasterio
    print('rasterio version:', rasterio.__version__)
except Exception as e:
    print('rasterio import error:', e)

try:
    from osgeo import gdal
    print('GDAL version:', gdal.VersionInfo())
except Exception as e:
    print('GDAL import error:', e)

# Settings import from backend
sys.path.append(str(Path(__file__).parents[3]))  # add project root to path
from app.core.config import settings
print('DEM path exists:', settings.dem_path.exists())
print('DEM path:', settings.dem_path)
print('COST path exists:', settings.COST_PATH.exists())
print('COST path:', settings.COST_PATH)
