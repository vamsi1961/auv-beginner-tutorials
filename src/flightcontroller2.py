#!/usr/bin/env python
from dronekit import *
import serial
import rospy
from std_msgs.msg import Float64


quad = connect("/dev/ttyACM0", wait_ready=0, baud = 115200)
quad.wait_ready(True, raise_exception=False)


def talker2():


   pub2 = rospy.Publisher('ahrs', Float64, queue_size=10)
   rospy.init_node('flight', anonymous=True) 



   rate = rospy.Rate(10) # 10hz

   while not rospy.is_shutdown():

      if(quad.attitude.roll!=None):
          value = ((quad.attitude.roll/3.14)*180)

      pub2.publish(value)
      print(value)
      rate.sleep()    
      
    
if __name__ == '__main__':
    try:
        talker2()
    except rospy.ROSInterruptException:
        pass




