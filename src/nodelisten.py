import rospy
global x
global y

from std_msgs.msg import Int32

rospy.init_node('listner', anonymous=True)

def callback1(val1):
    x=val1.data
    #flag_1 = True
    print(x)

def callback2(val2):
     y=val2.data
     #flag_2 = True
     print(y)
     

def listner():
      rospy.Subscriber('a', Int32, callback1) 
      rospy.Subscriber('b', Int32, callback2)
     #  print("flag_1",flag_1)
     #  print("flag_2",flag_2)
     #  while flag_1 or flag_2: 
    
      #rospy.spin()

if __name__=='__main__':
     listner()