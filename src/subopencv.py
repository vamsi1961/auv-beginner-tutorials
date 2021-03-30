import cv2 
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import timeit


def callback(data):
    try:
      start = timeit.default_timer()
      print(start)
      cv_image = CvBridge().imgmsg_to_cv2(data, "bgr8")
      print(cv_image.shape)
      #cv2.imshow('Image', cv_image)
      print('1')
 

    except CvBridgeError, e:
      print e

def listener():
    rospy.init_node('ImageReceived', anonymous=True)
    rospy.Subscriber("DisplayingImage", Image, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()