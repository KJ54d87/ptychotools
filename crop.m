ds_file = "E:\Need rotation\N30_47_25_pristine_np1_003_300kV_10mX_21_pm_30mrad_4pA_CL370mm_5-nmnm.h5"; % Your file here
ds_path = '/datacube_root/datacube/data';

data = h5read(ds_file, ds_path);
disp("Data loaded");

x_start = 175;       % Start x-coordinate of the selected area
x_end = 175+63;         % End x-coordinate of the selected area
y_start = 176 - 63;       % Start y-coordinate of the selected area
y_end = 176;         % End y-coordinate of the selected area

data_selected = data(:, :, x_start:x_end, y_start:y_end);

h5create("cropped2.hdf5", ds_path, [128 128 x_end-x_start+1 y_end-y_start+1]);
h5write("cropped2.hdf5", ds_path, data_selected);
disp("Cropped data saved to cropped.hdf5");
