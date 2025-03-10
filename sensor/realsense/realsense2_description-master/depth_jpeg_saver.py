#! /usr/bin/python
# rospy for the subscriber
import rospy
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2

# Instantiate CvBridge
bridge = CvBridge()

def image_callback(msg):

	cv2_img = bridge.imgmsg_to_cv2(msg, "16UC1")
	cv2.imwrite('camera_image.jpeg', cv2_img)

def main():
    rospy.init_node('image_listener')
    # Define your image topic
    image_topic = '/camera/depth/image_raw'
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic, Image,image_callback)
    # Spin until ctrl + c
    rospy.spin()

if __name__ == '__main__':
    main()
