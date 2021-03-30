#!/usr/bin/env python
import rospy
from std_msgs.msg import String
pub = "global"
abc = "global"
abc = String()
rospy.init_node('listner', anonymous=True)

pub = rospy.Publisher('asd' , String , queue_size=10)

def listner():

      rate = rospy.Rate(10)       
      rospy.spin()

def callback(abc):
	
        
        print(int(abc.data)) 

        if(int(abc.data) > 150):
          pub.publish("1")
        if(int(abc.data) <150):
          pub.publish("0")
       
rospy.Subscriber("potet", String , callback)

if __name__=='__main__':
        try: 
           listner()
        except rospy.ROSInterruptException:
           pass

