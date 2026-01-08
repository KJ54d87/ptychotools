import os
import io
from PIL import Image, ImageDraw, ImageColor
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from generate_mesh import generate_mesh, generate_circle_mesh
from calculate_intensities import intensity_contrast, luminence_contrast, michelsons_contrast, RMS

IMG = "obj_phase_roi_Niter120.tiff"
dir_name = "test_tiff"
frames = 24
contrast_function = RMS #Options are(will be) Michelsons, RMS, max_intensity
size = 480

def make_map(file, save_name):
    sample = file
    sample = sample.convert("rgb") #convert to rgb so we can draw
    sample = Image.fromarray(np.array(sample)) # wipe meta data so we can draw multiple colors
    # the above two lines are necessary for the drawing to work. Don't question it trust
    #sample = sample.convert("rgb")
    draw = ImageDraw.Draw(sample)
    for col in range(-6 ,10):
        potenital_points = generate_mesh(4, 290, 293, 13.7, 2.9, col, col+1, 13.7, 111.7, -20, 15)
        mesh = []
        for point in potenital_points:
            if point[0] >= 0 and point[0] < size and point[1] >= 0 and point[1]<size:
                mesh.append(point)

        #for pt in mesh:
        #    draw.circle(pt, 6, width=1 , outline="blue")

        #for i in range(len(mesh)):
        #    print(mesh[i])

        #generare numpy list
        circles = [generate_circle_mesh(mesh[i][0], mesh[i][1], 6) for i in range(len(mesh))]

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
    sample.save(save_name)

def run():
    with Image.open(IMG) as sample:
        try:
            os.mkdir(dir_name)
        except Exception:
            pass
        for i in range(1,frames):
            input = sample.copy()
            make_map(input, f"{dir_name}/frame{i:0=2}.tiff")
            sample.seek(sample.tell()+1)


if __name__ == "__main__":
    run()