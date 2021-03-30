import cv2 
import rospy
import sys
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


def talker():
    DisImg = rospy.Publisher('DisplayingImage', Image, queue_size=1)
    rospy.init_node('SendingImage', anonymous=True)
    

    while 1:
        img = cv2.imread('red.jpeg')
        msg_image = CvBridge().cv2_to_imgmsg(img,"bgr8")
        DisImg.publish(msg_image)
        rospy.loginfo(msg_image)
        rospy.sleep(1)


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass


