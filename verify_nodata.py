import rasterio
from osgeo import gdal

p = r"C:\Users\ayush\Downloads\MARSWALK\JEZ_hirise_soc_006_DTM_MOLAtopography_DeltaGeoid_1m_Eqc_latTs0_lon0_blend40.tif"

with rasterio.open(p) as ds:
    print("RASTERIO")
    print("NoData:", repr(ds.nodata))
    print("Tags:", ds.tags())
    print("Mask flags:", ds.mask_flag_enums)

ds = gdal.Open(p)
band = ds.GetRasterBand(1)
print("\nGDAL")
print("NoData:", repr(band.GetNoDataValue()))
print("Metadata:", band.GetMetadata())
print("Image structure:", ds.GetMetadata("IMAGE_STRUCTURE"))
