import io
from PIL import Image, ImageDraw, ImageColor
import numpy as np
import matplotlib.pyplot as plt
from generate_mesh import generate_mesh, generate_circle_mesh
from calculate_intensities import intensity_contrast, luminence_contrast, michelsons_contrast

IMG = "obj_phase_roi_Niter120.tiff"
frames = 24
contrast_function = "Michelsons" #Options are(will be) Michelsons, RMS, max_intensity

with Image.open(IMG) as sample:
    #print(sample.__dir__())
    #newImg = Image.frombytes("rgb", (480, 480))
    #mesh = generate_mesh(4, 290, 293, 13.7, 2.9, -6, 12, 13.7, 111.7, -15, 5)
    draw = ImageDraw.Draw(sample)
    #for pt in mesh:
        #draw.circle(pt, 6, width=1 , outline="blue")
    
    mesh = generate_circle_mesh(290, 293, 4)
    print(mesh)
    draw.point(mesh.tolist(), fill = "red")
    
    #so apparently I can only draw one thing at a time. 
    #This program is curse
    #bruh
    
        
    
    sample.save("test.png")
    
        
