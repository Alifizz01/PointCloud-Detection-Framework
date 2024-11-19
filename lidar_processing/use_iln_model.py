import os

def use_iln_model(input_file, output_file, checkpoint_file, voxel_size=None):
    command = f"python external/iln/demo_resolution_free_lidar.py -i {input_file} -cp {checkpoint_file}"
    if voxel_size:
        command += f" -v {voxel_size}"
    command += f" -o {output_file}"
    os.system(command)

# Example usage
if __name__ == "__main__":
    input_file = "data/sample_sparse.pcd"  # Replace with your input file path
    output_file = "output/sample_dense.pcd"
    checkpoint_file = "models/iln_1d_400.pth"  # Change to the model you're using

    use_iln_model(input_file, output_file, checkpoint_file)
