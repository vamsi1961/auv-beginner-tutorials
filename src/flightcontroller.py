from dronekit import *
import serial
import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Vector3

quad = connect("/dev/ttyACM0", wait_ready=0, baud = 115200)
quad.wait_ready(True, raise_exception=False)


def talker2():


   pub2 = rospy.Publisher('ahrs', Vector3, queue_size=10)
   rospy.init_node('flight', anonymous=True) 
   value = Vector3()


   rate = rospy.Rate(10) # 10hz

   while not rospy.is_shutdown():
      if(quad.attitude.roll!=None):
          value.x = ((quad.attitude.roll/3.14)*180)
         
          

      if(quad.attitude.pitch!=None):
          value.y = ((quad.attitude.pitch/3.14)*180)
         

      if(quad.attitude.yaw!=None):
          value.z = ((quad.attitude.yaw/3.14)*180)
       
      pub2.publish(value)
      print(value)
      rate.sleep()    
      
    
if __name__ == '__main__':
    try:
        talker2()
    except rospy.ROSInterruptException:
        pass



