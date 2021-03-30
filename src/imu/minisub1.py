import rospy
import serial

lastError1 = 0
lastError2 = 0

mot1 = "global"
mot2 = "global"

arduino=serial.Serial('/dev/ttyACM0',9600,timeout=1)

then = rospy.Time.now()

from std_msgs.msg import Int32


rospy.init_node('listner', anonymous=True)
val1 = arduino.read()
val2 = arduino.read()



def listner():
    
     rate = rospy.Rate(1000)       
     rospy.spin()

def callback2(mot2):
     
     print(mot2.data)
     arduino.write(mot2.data)
     now2 = rospy.Time.now()
     t2 = now2-then 

  # Proportional term
     p = kp * val2
    
  # Derivative term
     d = kd * ( (val2 - lastError2)/t2 )       
     lastError2 = val2           # previous output level
  # Integral term
     i = ki * (val2*t2 )      # integrator state     

     motorSpeed = p + i + d 
     newsp2 = mot1 + motorSpeed 

     if (newsp2 >255) 
       fsp2 = 255
     else if (newsp2 < 255)
       fsp2 = newsp2 

      arduino.write(fsp2.data)

  def callback1 (mot1):
     print(mot1.data)
     arduino.write(mot1.data)
     now1 = rospy.Time.now()
     t1 = now1 - then 
  # Proportional term
     p = kp * val1
    
  # Derivative term
     d = kd * ( (val1 - lastError1)/t1 )       
     lastError1 = val1           # previous output level
  # Integral term
     i = ki * (val1*t1 )      # integrator state     

     motorSpeed = p + i + d 

     newsp1 = mot1 + motorSpeed 
     if (newsp1 >255) 
        fsp1 = 255
     else if (newsp1 < 255)
        fsp1 = newsp1

     arduino.write(fsp1.data)
  

rospy.Subscriber('topic1', Int32 , callback1)
rospy.Subscriber('topic2', Int32 , callback2)


if __name__=='__main__':
     listner()



