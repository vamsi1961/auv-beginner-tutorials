import rospy

from std_msgs.msg import Int32


rospy.init_node('talker', anonymous = True)


pub1 = rospy.Publisher('a',Int32,queue_size=10)
pub2 = rospy.Publisher('b',Int32,queue_size=10)

def talker():
     
  while 1:    
      a=100
      b=100
      #var1 = input()
      #var2 = input()
      #a=var1
      #b=var2 
    
      pub1.publish(a)
      pub2.publish(b)
      #rospy.spin()

if __name__=='__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass