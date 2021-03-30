#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import serial
import numpy as np 
import cv2 
from dronekit import connect
import serial


cap = cv2.VideoCapture(0) 
ser=serial.Serial('/dev/ttyACM0',baudrate=9600,timeout=1)

fourcc = cv2.VideoWriter_fourcc(*'XVID') 
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))


quad = connect("/dev/ttyACM0", wait_ready=False, baud = 115200)

quad.wait_ready(True, raise_exception=False)


def talker():
 #   pub = rospy.Publisher('chatter', String, queue_size=10)
 #   rospy.init_node('talker', anonymous=True)
    rospy.loginfo("I will publish to the topic %s",'chatter')
#    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        if(quad.attitude.yaw!=None):
          print((quad.attitude.yaw/3.14)*180)
          rospy.loginfo((quad.attitude.yaw/3.14)*180)
        ret, frame = cap.read()  
        out.write(frame)
        cv2.imshow('Original', frame)
        '''arduinodata = ser.readline()

        rospy.loginfo(arduinodata)
        print(arduinodata)'''
 #       pub.publish(arduinodata)
        if cv2.waitKey(1) & 0xFF == ord('a'): 
           break
 #       rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass 