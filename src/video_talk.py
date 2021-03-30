import rospy
from std_msgs.msg import Int32
import cv2

def talker():

    pub = rospy.Publisher('chatter', Int32, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rospy.loginfo("I will publish to the topic %s",'chatter' )
    rate = rospy.Rate(10) # 10hz
    cap = cv2.VideoCapture(0)
    if (cap.isOpened() == False): 
        print("Unable to read camera feed")

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
    
    while(True):
        while not rospy.is_shutdown():
            ret, frame = cap.read()
            
            if ret == True: 
                out.write(frame)
                cv2.imshow('frame',frame)
                pub.publish(frame[0,0,1])
                rospy.loginfo("I will publish to the topic %s",'chatter' )
                rate.sleep()
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                else:
                    break 

    cap.release()
    out.release()
    cv2.destroyAllWindows() 

            
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass 





