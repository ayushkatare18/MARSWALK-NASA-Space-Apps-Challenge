from PIL import Image
import os

for f in ["terrain_test.png", "cost_test.png"]:
    print("\nFILE:", f)

    if not os.path.exists(f):
        print("File not found")
        continue

    im = Image.open(f).convert("RGBA")
    alpha = im.getchannel("A")

    print("Dimensions:", im.size)
    print("File size:", os.path.getsize(f), "bytes")
    print("Alpha range:", alpha.getextrema())
    print("RGB range:", im.convert("RGB").getextrema())
    print("Visible pixels:", sum(1 for p in alpha.getdata() if p > 0))
