import open3d as o3d

def visualize_point_cloud(file_path):
    pcd = o3d.io.read_point_cloud(file_path)
    o3d.visualization.draw_geometries([pcd])

# Example usage
if __name__ == "__main__":
    visualize_point_cloud("output/sample_dense.pcd")
