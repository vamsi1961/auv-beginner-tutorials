import numpy as np 
import cv2 
import rospy
from std_msgs.msg import String

rospy.init_node('video', anonymous=True)  



def callback(val):
    value = val.data
    print(value)
    print(type(value))


    
    rospy.loginfo("log value = %s" , value) 


# loop runs if capturing has been initialized.  
def listener():   
   cap = cv2.VideoCapture(0)   
   fourcc = cv2.VideoWriter_fourcc(*'XVID') 
   out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  
   while not rospy.is_shutdown():
    rospy.Subscriber("flag", String, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
