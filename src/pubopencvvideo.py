import cv2 
import rospy
import sys
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError




def talker():
    cap = cv2.VideoCapture(0)
    # fourcc = cv2.VideoWriter_fourcc(*'XVID') 
    # out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480)) 

    # DisImg = rospy.Publisher('DiplayingImage', Image, queue_size=10)
    # rospy.init_node('SendingImage', anonymous=True)
    # rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        
        # msg_image = CvBridge().cv2_to_imgmsg(frame)
        # DisImg.publish(msg_image, "bgr8")
        cv2.imshow('Original', frame)
           # Wait for 'a' key to stop the program  
        if cv2.waitKey(1) & 0xFF == ord('a'): 
          break
        # rate.sleep()
    cap.release() 
  
# After we release our webcam, we also release the output 
    out.release()  
      


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass



