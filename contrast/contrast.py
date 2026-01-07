from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
from generate_mesh import generate_mesh

IMG = "obj_phase_roi_Niter120.tiff"
frames = 24

with Image.open(IMG) as sample:
    #print(sample.__dir__())
    mesh = generate_mesh(4, 290, 293, 13.7, 2.9, -6, 20, 13.7, 111.7, -100, 100)
    draw = ImageDraw.Draw(sample)
    for pt in mesh:
        draw.circle(pt, 6, width=1 , outline="blue")
        
        
