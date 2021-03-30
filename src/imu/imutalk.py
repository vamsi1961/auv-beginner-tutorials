

#!/usr/bin/env/ python
# license removed for brevity

import rospy
import serial


from std_msgs.msg import String

def talker():
    rospy.init_node('pot', anonymous = True)
    pub = rospy.Publisher('potet',String,queue_size=10)
    ser=serial.Serial('/dev/ttyACM0',baudrate=9600,timeout=1)
       
    while 1:	
      if 1:
        arduino = ser.readline()
        arduino.rstrip('\n')
       
        print(arduino.rstrip('\n'))
 
        count = String()
        count.data = arduino.rstrip('\n')


        if not rospy.is_shutdown():
            pub.publish(count)
  


if __name__=='__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass


	   



