# lidar_processing/convert_to_kitti.py
import numpy as np
import os

def save_as_kitti(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for file in os.listdir(input_dir):
        if file.endswith(".npy"):
            cloud = np.load(os.path.join(input_dir, file))
            cloud.astype('float32').tofile(os.path.join(output_dir, file.replace('.npy', '.bin')))

# Usage
input_dir = "../data/lidar_frames/"
output_dir = "../data/kitti_format/"
save_as_kitti(input_dir, output_dir)
