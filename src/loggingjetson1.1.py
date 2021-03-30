import rospy
from std_msgs.msg import String
from std_msgs.msg import Int64
from geometry_msgs.msg import Vector3

a=0 
b=0
c=0
flow =0
pressure = 0
imu = 0
rospy.init_node('listener', anonymous=True)
pub = rospy.Publisher("flag", String, queue_size=10)

#rospy.init_node('flag1', anonymous=True)

def callback1(val1):

    global imu,a,b,c,flow
    imu = val1 # a takes 0 or 1
    a = 1

    
    if a==1 and b==1 and c==1 :
        rospy.loginfo("roll value = %f", val1.x)
        rospy.loginfo("pitch value = %f",val1.y)
        rospy.loginfo("yaw value = %f", val1.z)
        rospy.loginfo( "flowmeter value = %s",flow)
        rospy.loginfo( "pressure value = %s",pressure)
        pub.publish("f")
        a=b=c=0
    else :

        print("wrong code :1")
    

def callback2(val2):
   
    global flow,a,b,c 
    flow = val2.data 
    b=1
 
    if a==1 and b==1 and c==1:
        rospy.loginfo("roll value = %f", imu.x)
        rospy.loginfo("pitch value = %f",imu.y)
        rospy.loginfo("yaw value = %f", imu.z)
        rospy.loginfo( "flowmeter value = %s",val2.data)
        rospy.loginfo("pressure = %s",pressure)
        pub.publish("f")
        a=b=c=0
      
    else : 

        print("wrong code :2")

    
    
def callback3(val3):
    global c,pressure,a,b
    pressure = val3.data
    c=1
    
    if a==1 and b==1 and c==1 :
        rospy.loginfo("roll value = %f", imu.x)
        rospy.loginfo("pitch value = %f",imu.y)
        rospy.loginfo("yaw value = %f", imu.z)
        rospy.loginfo("flowmeter value = %s",flow)
        rospy.loginfo("pressure = %s ",val3.data)
        pub.publish("f")
        a=b=c=0
    else :
        print("wrong code :3")
   
def listener():

    rospy.Subscriber("ahrs", Vector3, callback1)
    rospy.Subscriber("flowmeter",Int64, callback2)
    rospy.Subscriber("pressure", Int64, callback3)
    

    rospy.spin()


if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass