import rasterio
import numpy as np

path = r"MARSWALK_DATA/processed/jezero/jezero_cost_450e0d0d_f2d7519a.tif"

with rasterio.open(path) as src:
    data = src.read(1)

    for name, (r, c) in {
        "START": (1123, 1456),
        "GOAL": (1589, 1923)
    }.items():

        r0, r1 = max(0, r-100), min(src.height, r+101)
        c0, c1 = max(0, c-100), min(src.width, c+101)

        window = data[r0:r1, c0:c1]
        valid = np.argwhere(window != 255)

        print(f"\n{name}:")
        print("Valid cells nearby:", len(valid))

        if len(valid) > 0:
            distances = np.sum(
                (valid - np.array([r-r0, c-c0]))**2,
                axis=1
            )
            nearest = valid[np.argmin(distances)]

            rr = int(nearest[0] + r0)
            cc = int(nearest[1] + c0)

            print("Nearest valid cell:", (rr, cc))
            print("Cost:", int(data[rr, cc]))
            print("Projected coordinates:",
                  src.transform * (cc + 0.5, rr + 0.5))
