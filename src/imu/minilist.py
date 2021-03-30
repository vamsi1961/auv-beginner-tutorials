import rospy
import serial

from std_msgs.msg import String
#from std_msgs.msg import String


#global mot1 
#global mot2  
#mot1 = Int32()
#mot2 = Int32()
pub = "global" 
global count
count = String()

ser =serial.Serial('/dev/ttyACM0',baudrate=9600,timeout=1)

rospy.init_node('listner', anonymous=True)

#pub = rospy.Publisher('topic3', Int32 ,queue_size=10)

def listner():

 while 1:
   if 1:
    arduino = ser.readline()
    arduino.rstrip('\n')
  
    print(type(arduino.rstrip('\n')))
   
    #count.data = arduino.rstrip('\n')
    #if not rospy.is_shutdown():
      #pub.publish(count)

  #rospy.spin()          
  #rate.sleep()	
a
#def callback1 (mot1):
 #    print(mot1.data)
  #   ser.write(mot1.data)

#def callback2(mot2):
     
 #    print(mot2.data)
  #   ser.write(mot2.data)
#rospy.Subscriber('topic1', Int32, callback1)
#rospy.Subscriber('topic2', Int32, callback2)


if __name__ == '__main__':
  try : 
      listner()
  except rospy.ROSInterruptException:
      pass
    
    