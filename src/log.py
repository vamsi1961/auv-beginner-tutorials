import rospy
from std_msgs.msg import Float32
from std_msgs.msg import Int16
import time
a = 0
rospy.init_node('flag', anonymous=True)
def listener():
    while 1:
        flag = raw_input("enter flag: ")   
        if flag == "f":
            global a
            a = a+1
            #print(a)
            rospy.loginfo("flag = %d",a)
            start =time.time()
            rospy.loginfo("time = %f ",start)

if __name__ == '__main__':
    listener()
