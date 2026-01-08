import io
from PIL import Image, ImageDraw, ImageColor
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from generate_mesh import generate_mesh, generate_circle_mesh
from calculate_intensities import intensity_contrast, luminence_contrast, michelsons_contrast, RMS

IMG = "obj_phase_roi_Niter120.tiff"
frames = 24
contrast_function = RMS #Options are(will be) Michelsons, RMS, max_intensity
size = 480

with Image.open(IMG) as sample:
    sample = sample.convert("rgb") #convert to rgb so we can draw
    sample = Image.fromarray(np.array(sample)) # wipe meta data so we can draw multiple colors
    #sample = sample.convert("rgb")
    draw = ImageDraw.Draw(sample)
    for col in range(-6 ,10):
        mesh = generate_mesh(4, 290, 293, 13.7, 2.9, col, col+1, 13.7, 111.7, -10, 6)
        #for pt in mesh:
        #    draw.circle(pt, 6, width=1 , outline="blue")

        #for i in range(len(mesh)):
        #    print(mesh[i])

        #generare numpy list
        circles = [generate_circle_mesh(mesh[i][0], mesh[i][1], 7) for i in range(len(mesh))]

        circles_data = []
        for circle in circles:
            #draw.point(circle.tolist(), fill = "red")
            circle_data = []
            for pxl in circle:
                if pxl[0] >=0 and pxl[0]<size and pxl[1]>=0 and pxl[1]<size:
                    circle_data.append(sample.getpixel(pxl))
            circles_data.append(circle_data)
        #print(circles_data)

        intensity = []
        min_val = 9999999
        max_val = 0
        for circle_data in circles_data:
            #print(contrast_function(circle_data))
            intensity.append(float(contrast_function(circle_data)))
            if intensity[-1] > max_val:
                max_val = intensity[-1]
            if intensity[-1] < min_val:
                min_val = intensity[-1]

        color_map = mpl.cm.bwr
        norm = mpl.colors.Normalize(vmin=min_val, vmax=max_val)

        color = []
        for i in range(len(intensity)):
            rgb = color_map(norm(intensity[i]), bytes = True)
            color.append(rgb[:3])

        #print(color)

        #print(circles[0])
        #print(color[0])

        for i in range(len(intensity)):
            draw.point(circles[i].tolist(), fill=color[i])
            
        #print(intensity)
        #color_layer.save("color.png")
        #so apparently I can only draw one thing at a time.
        #This library is cursed
        #bruh

    sample.save("michelsons_contrast_raw.png")


