
import rospy
from std_msgs.msg import String
import time

asd = "global"
asd = String()
rospy.init_node('talker', anonymous=True)
       
def listener():
       
        rate = rospy.Rate(10) 
        rospy.spin()  

def callback(value):

   print(value.data)
   start = time.time()
   print(type(start))
   print(start)         
   rospy.loginfo("flag = %s ",value.data)
   rospy.loginfo("time = %f ",start)

rospy.Subscriber('flag', String, callback)  

if __name__ == '__main__':
    listener()

 
