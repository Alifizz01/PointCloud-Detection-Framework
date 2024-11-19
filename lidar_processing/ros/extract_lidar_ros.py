import rosbag
import rospy
from sensor_msgs.msg import PointCloud2
from std_msgs.msg import Header

def republish_lidar_from_bag(bag_file, topic, pub_topic):
    rospy.init_node("lidar_republisher", anonymous=True)
    pub = rospy.Publisher(pub_topic, PointCloud2, queue_size=10)
    rate = rospy.Rate(10)

    with rosbag.Bag(bag_file, 'r') as bag:
        for _, msg, t in bag.read_messages(topics=[topic]):
            msg.header.stamp = rospy.Time.now()
            pub.publish(msg)
            rate.sleep()

if __name__ == "__main__":
    bag_file = "rosbag_files/sample.bag"  # Path to your ROSbag
    topic = "/lidar_points"               # LiDAR topic in your bag file
    pub_topic = "/processed_lidar"        # Topic for republishing

    try:
        republish_lidar_from_bag(bag_file, topic, pub_topic)
    except rospy.ROSInterruptException:
        pass
