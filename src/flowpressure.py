import rospy
from std_msgs.msg import String
from std_msgs.msg import Int64
from std_msgs.msg import Float64
import serial

def flowtalker():
   pub1 = rospy.Publisher('flowmeter',Int64, queue_size=10)
   pub2 = rospy.Publisher('pressure',  Int64, queue_size=10)
   rospy.init_node('flow', anonymous=True)
   ser=serial.Serial('/dev/ttyACM0',baudrate=9600,timeout=1)
   rate = rospy.Rate(10) # 10hz
   while not rospy.is_shutdown():

        arduinodata = ser.readline()
        arduino = arduinodata + "0"
        print(arduinodata)
    #     arduino = float(arduinodata)
    #  #   print(type(arduino))     

    # #    arduino = int(arduinodata)
    #     flow1 = arduino//10000000
    #     flow2pressure = arduino %10000000
    #     flow2 = flow2pressure//10000
    #     pressure = flow2pressure%10000
    #     print((flow1))
    #     print((flow2))
    #     print((pressure))
    #     pub1.publish(flow1)
    #     pub2.publish(pressure)

    #     pub1.publish(arduinodata)


    
        rate.sleep()

if __name__ == '__main__':
    try:
        flowtalker()
    except rospy.ROSInterruptException:
        pass        
