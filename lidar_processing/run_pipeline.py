import os

def run_pipeline():
    # Step 1: Extract LiDAR from rosbag
    os.system("python lidar_processing/extract_lidar.py")

    # Step 2: Apply ILN Model
    os.system("python lidar_processing/use_iln_model.py")

    # Step 3: Convert to KITTI Format
    os.system("python lidar_processing/convert_to_kitti.py")

    # Step 4: Run Object Detection
    os.system("python lidar_processing/run_detection.py")

    # Step 5: Visualize Detection Results
    os.system("python lidar_processing/visualize_detections.py")

if __name__ == "__main__":
    run_pipeline()
