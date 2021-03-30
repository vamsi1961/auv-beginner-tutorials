
#!/usr/bin/env/ python
# license removed for brevity

import rospy
import serial
import time

from std_msgs.msg import String

pub = "global"
abcd = "global"
abcd = String()
ser=serial.Serial('/dev/ttyACM0',baudrate=9600,timeout=1)
rospy.init_node('pot', anonymous = True)


pub = rospy.Publisher('potet',String,queue_size=10)
	
def talker():
 while 1:
   if 1:
    arduino =ser.readline()
    arduino.rstrip('\n')
   
    print(arduino.rstrip('\n'))
    count= String()
    count.data=arduino.rstrip('\n')
    if not rospy.is_shutdown():
           pub.publish(count)
 rate.sleep()	
		
def callback(abcd):
        
    
    print(abcd.data)
            
  
    if(int(abcd.data)== 1):
        ser.write('1')
     
    if(int(abcd.data) == 0):
        ser.write('0')
       
    
            
rospy.Subscriber('asd', String, callback)


if __name__=='__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    

	   



