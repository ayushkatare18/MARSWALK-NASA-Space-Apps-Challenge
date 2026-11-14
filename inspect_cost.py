import rasterio
import numpy as np

p = r"MARSWALK_DATA/processed/jezero/jezero_cost_450e0d0d_f2d7519a.tif"

with rasterio.open(p) as src:
    a = src.read(1)

    valid = np.argwhere(a != 255)

    print("Raster dimensions:", a.shape)
    print("Total valid cells:", len(valid))
    print("Valid row range:", valid[:, 0].min(), "to", valid[:, 0].max())
    print("Valid column range:", valid[:, 1].min(), "to", valid[:, 1].max())

    for r, c in [
        (1123, 1456),
        (1589, 1923)
    ]:
        print(f"Cell ({r},{c}):", a[r,c])

    # Find a representative valid cell near the centre of valid coverage
    centre = np.mean(valid, axis=0)
    distances = np.sum((valid-centre)**2, axis=1)
    rr, cc = valid[np.argmin(distances)]

    print("Representative valid cell:", (int(rr), int(cc)))
    print("Its cost:", int(a[rr,cc]))
    print("Projected centre:", src.transform * (cc+0.5, rr+0.5))
