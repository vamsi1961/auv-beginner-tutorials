
import rospy
import serial
import time

from std_msgs.msg import Int32



ser=serial.Serial('/dev/ttyACM0',baudrate=9600,timeout=1)

rospy.init_node('listner', anonymous=True)


def listner():

 while 1:
   if 1:
    arduino =ser.readline()
    arduino.rstrip('\n')
   
    print(arduino.rstrip('\n'))
    count= String()
    count.data=arduino.rstrip('\n')  
          
 rate.sleep()  

def callback2(mot2):
 print(mot2.data)
 ser.write(mot2.data)

def callback1 (mot1):
 print(mot1.data)
 ser.write(mot1.data)

 
rospy.Subscriber('topic1', Int32 , callback1)
rospy.Subscriber('topic2', Int32 , callback2)



if __name__=='__main__':
     listner()