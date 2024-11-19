# lidar_processing/extract_lidar.py
import rosbag
import sensor_msgs.point_cloud2 as pc2
import numpy as np
import os

def extract_lidar(bag_file, output_dir, topic):
    bag = rosbag.Bag(bag_file, 'r')
    os.makedirs(output_dir, exist_ok=True)

    for idx, (topic, msg, t) in enumerate(bag.read_messages(topics=[topic])):
        # Convert ROS point cloud to numpy array
        cloud = np.array(list(pc2.read_points(msg, skip_nans=True)))
        np.save(os.path.join(output_dir, f"frame_{idx}.npy"), cloud)

    bag.close()

# Usage
bag_file = "../rosbag_files/sample.bag"
output_dir = "../data/lidar_frames/"
topic = "/lidar_points"  # Replace with your LiDAR topic
extract_lidar(bag_file, output_dir, topic)
