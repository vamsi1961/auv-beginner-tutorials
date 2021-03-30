import numpy as np 
import cv2 
import rospy
from std_msgs.msg import String

cap = cv2.VideoCapture(0)   
  
# Define the codec and create VideoWriter object 
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
rospy.init_node('talker', anonymous=True)
flow = String()

def listener():
       
        rate = rospy.Rate(10) 
        rospy.spin()  

 
def callback(flow):

       
   while(True): 
        
    ret, frame = cap.read()  

    out.write(frame)  
    cv2.imshow('Original', frame) 
    print(flow.data)  
    print(frame.shape)
    # Wait for 'a' key to stop the program  
    if cv2.waitKey(1) & 0xFF == ord('a'): 
        break

rospy.Subscriber('chatter', String, callback) 


if __name__ == '__main__':
    listener()