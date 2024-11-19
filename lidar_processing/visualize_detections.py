# lidar_processing/visualize_detections.py
import open3d as o3d
import numpy as np

def visualize_point_cloud_with_detections(cloud_file, detections_file):
    cloud = np.fromfile(cloud_file, dtype=np.float32).reshape(-1, 4)
    detections = np.load(detections_file)  # Load your detection results

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(cloud[:, :3])

    # Visualize
    o3d.visualization.draw_geometries([pcd])

# Usage
cloud_file = "../data/kitti_format/frame_0.bin"
detections_file = "../output/detections/frame_0.npy"  # Replace with actual detection output
visualize_point_cloud_with_detections(cloud_file, detections_file)
