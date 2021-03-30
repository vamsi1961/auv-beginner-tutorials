#!/usr/bin/env python
import rospy
from std_msgs.msg import String
pub = "global"
abc = "global"
abc = String()
pub = rospy.Publisher('chatter2', String, queue_size=10)
rospy.init_node('talker2', anonymous=True)

def talker():
    
   
    rate = rospy.Rate(10) 
    while not rospy.is_shutdown():
        hello_str = "hello "
        print(hello_str)
        pub.publish(hello_str)
        rate.sleep()



def callback(abcd):
        print(abcd.data)

rospy.Subscriber('abc', String, callback)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

