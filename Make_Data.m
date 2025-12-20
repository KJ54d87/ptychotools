%Creates testing dp for rotate, specifically, puts a white rectangle on the
%left of dp

ds_file = "E:\output\N30_47_25_pristine_np1_003_300kV_10mX_21_pm_30mrad_4pA_CL370mm_5-nmnm_rotated-50.hdf5"; % Your file here
ds_path = '/datacube_root/datacube/data'; %Don't change this

save_file_dir = 'E:\output\'; % The directory you want to save in
save_file_name = "rectangle.hdf5"; % filename to save as 

save_file_full_path =  fullfile(save_file_dir, save_file_name);

data = h5read(ds_file, ds_path);
disp("Data loaded");
[dim1, dim2, dim3, dim4] = size(data);
clear data

data = zeros(dim1, dim2, dim3, dim4);
%Super cursed nested for loop to fill half of the dp with 256
for i = 1:dim3
    for j = 1:dim4
        for k = 1:dim1
            for m = 1:dim2/2
                data(m,k,i,j) = 256;
            end
        end
    end
end

%Make a new h5file with rotated probes
copyfile(ds_file, save_file_full_path)
%h5create(save_file_full_path, ds_path, size(data))
h5write(save_file_full_path, ds_path, data)