import rospy
from sensor_msgs.msg import PointCloud2
import numpy as np
import os
import sensor_msgs.point_cloud2 as pc2
from std_msgs.msg import Header

def process_point_cloud(msg, model_path, output_topic):
    # Convert ROS PointCloud2 to numpy array
    cloud = np.array(list(pc2.read_points(msg, skip_nans=True)))

    # Save to temporary file
    input_file = "/tmp/input_cloud.npy"
    np.save(input_file, cloud)

    # Run ILN model
    output_file = "/tmp/output_cloud.npy"
    command = f"python external/iln/demo_resolution_free_lidar.py -i {input_file} -cp {model_path} -o {output_file}"
    os.system(command)

    # Convert dense cloud back to ROS PointCloud2
    dense_cloud = np.load(output_file)
    header = Header()
    header.stamp = rospy.Time.now()
    header.frame_id = msg.header.frame_id
    dense_msg = pc2.create_cloud_xyz32(header, dense_cloud[:, :3])

    # Publish to output topic
    pub.publish(dense_msg)

if __name__ == "__main__":
    rospy.init_node("iln_lidar_processor", anonymous=True)

    # ROS parameters
    input_topic = "/processed_lidar"
    output_topic = "/dense_lidar"
    model_path = "models/iln_1d_400.pth"  # Pre-trained model path

    pub = rospy.Publisher(output_topic, PointCloud2, queue_size=10)
    rospy.Subscriber(input_topic, PointCloud2, process_point_cloud, callback_args=(model_path, output_topic))

    rospy.spin()
