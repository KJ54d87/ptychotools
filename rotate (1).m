clear

ds_file = "E:\Need rotation\N30_47_25_pristine_np1_003_300kV_10mX_21_pm_30mrad_4pA_CL370mm_5-nmnm.h5"; % Your file here
ds_path = '/datacube_root/datacube/data'; %Don't change this

save_file_dir = 'E:\output\'; % The directory you want to save in
save_file_name = "N30Pristine-50.hdf5"; % filename to save as 
%^above need to be edited for your system
save_file_full_path =  fullfile(save_file_dir, save_file_name);

rotate_deg = 50; % Degree to rotate probe by. Clockwise is negative, counterclockwise is positive. 
interpolation_method = "bilinear"; % Interpolation method for probes. Supported methods are "nearest", "bilinear" and "bicubic"  

% For each probe position, will do the equivalent of 
% rotates probe rotate_deg degrees
function translated = translate_dps(data, rotate_deg, interpolation_method)
    if isa(data, "single") % If data is in memory, treat as such
        
        [dim1, dim2, dim3, dim4] = size(data);
    
        for i = 1:dim3
            for j = 1:dim4
                probe = data(:, :, i, j);
                probe = imrotate(probe, rotate_deg, interpolation_method, "crop"); %Rotate probe
                data(:, :, i, j) = probe;
            end
        end
    elseif isa(data, 'matlab.io.MatFile') % If data is in a file, edit a row at a time.
        [dim1, dim2, dim3, dim4] = size(dp_in, 'data');
    
        for i = 1:dim4
            probes = data.data(:, :, :, i); % Load a row of data
            for j = 1:dim3
                probe = probes(:, :, j);
                probe = imrotate(probe, rotate_deg, interpolation_method); %Rotate probe
                probes(:, :, j) = probe;
            end
            data.data(:, :, :, i) = probes;
        end
    end
    translated = data;
end

% Depending on the size of the file. If data is small enough to fit in memory
% read to memory (faster) or writes data to a file

user = memory;
ID = H5F.open(ds_file);
memory_needed =  2*H5F.get_filesize(ID); %Double memory needed since a copy is passed to translate_dps
if user.MaxPossibleArrayBytes > 2*H5F.get_filesize(ID) % If there is enough space, load data into memory. Runs much faster
    data = h5read(ds_file, ds_path);
    disp("Data loaded");

    data_single = single(data);
    assert(all(eq(data_single, data), "all")) %Check for lost precision
    data = data_single;
    clear data_single;

    disp("Starting translation");

    data = translate_dps(data, rotate_deg, interpolation_method); % Process the data using the translation function

    %Make a new h5file with rotated probes
    copyfile(ds_file, save_file_full_path)
    %h5create(save_file_full_path, ds_path, size(data))
    h5write(save_file_full_path, ds_path, data)
else
    data = h5read(ds_file, ds_path);
    disp("Data loaded, writing to temp file");


    temp_file_name = "temp.mat";
    temp_file_full_path =  fullfile(save_file_dir, temp_file_name);

    save(temp_file_full_path, "data", "-v7.3");
    clear data
    m = matfile(temp_file_full_path, "writable", true);

    disp("Starting translation");
    translate_dps(m, rotate_deg, interpolation_method); % Process the data using the translation function
    %Make a new h5file with rotated probes
    copyfile(ds_file, save_file_full_path)
    h5write(save_file_full_path, ds_path, m.data)
end
