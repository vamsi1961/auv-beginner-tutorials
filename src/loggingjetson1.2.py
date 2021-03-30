import rospy
from std_msgs.msg import String
from std_msgs.msg import Int64
from geometry_msgs.msg import Vector3

a=0 
b=0
c=0
d=0
flow =0
flow2 = 0
pressure = 0
imu = 0
rospy.init_node('listener', anonymous=True)
pub = rospy.Publisher("flag", String, queue_size=10)

#rospy.init_node('flag1', anonymous=True)

def callback1(val1):

    global imu,a,b,c,flow,d,flow2
    imu = val1 # a takes 0 or 1
    a = 1

    
    if a==1 and b==1 and c==1 and d==1 :
        rospy.loginfo("roll value = %f", val1.x)
        rospy.loginfo("pitch value = %f",val1.y)
        rospy.loginfo("yaw value = %f", val1.z)
        rospy.loginfo( "flowmeter value = %s",flow)
        rospy.loginfo( "pressure value = %s",pressure)
        rospy.loginfo("flowmeter2 value = %s",flow2)
        pub.publish("f")
        a=b=c=d=0
    else :

        print("wrong code :1")
    

def callback2(val2):
   
    global flow,a,b,c,d,flow2 
    flow = val2.data 
    b=1
 
    if a==1 and b==1 and c==1 and d==1 :
        rospy.loginfo("roll value = %f", imu.x)
        rospy.loginfo("pitch value = %f",imu.y)
        rospy.loginfo("yaw value = %f", imu.z)
        rospy.loginfo( "flowmeter value = %s",val2.data)
        rospy.loginfo("pressure = %s",pressure)
        rospy.loginfo("flowmeter2 value = %s",flow2)
        pub.publish("f")
        a=b=c=d=0
      
    else : 

        print("wrong code :2")

    
    
def callback3(val3):
    global c,pressure,a,b,d,flow,flow2
    pressure = val3.data
    c=1
    
    if a==1 and b==1 and c==1 and d==1 :
        rospy.loginfo("roll value = %f", imu.x)
        rospy.loginfo("pitch value = %f",imu.y)
        rospy.loginfo("yaw value = %f", imu.z)
        rospy.loginfo("flowmeter value = %s",flow)
        rospy.loginfo("pressure = %s ",val3.data)
        rospy.loginfo("flowmeter2 value = %s",flow2)
        pub.publish("f")
        a=b=c=d=0
    else :
        print("wrong code :3")


def callback4(val4):
    global pressure,a,b,c,flow,d,flow2
    flow2 = val4.data
    d=1
    
    if a==1 and b==1 and c==1 and d==1 :
        rospy.loginfo("roll value = %f", imu.x)
        rospy.loginfo("pitch value = %f",imu.y)
        rospy.loginfo("yaw value = %f", imu.z)
        rospy.loginfo("flowmeter1 value = %s",flow)
        rospy.loginfo("pressure = %s ",pressure)
        rospy.loginfo("flowmeter2 value = %s",val4.data)
        pub.publish("f")
        a=b=c=d=0
    else :
        print("wrong code :4")
   
def listener():
    
    rospy.Subscriber("flowmeter1",Int64, callback2)
    rospy.Subscriber("flowmeter2",Int64, callback4)    
    rospy.Subscriber("pressure", Int64, callback3)
    rospy.Subscriber("ahrs", Vector3, callback1)

    rospy.spin()


if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass