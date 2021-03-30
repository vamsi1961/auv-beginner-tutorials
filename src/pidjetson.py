import rospy
from std_msgs.msg import Float64
from std_msgs.msg import String
import time
import serial


derror = 0
ierror = 0
derrort = 0
error = 0
olderror = 0

global kp,ki,kd,pub
kp = 0
ki = 0
kd = 0
ser=serial.Serial('/dev/ttyACM1',baudrate=57600,timeout=1)
rospy.init_node('pidflight', anonymous=True) 


def pid(value1):
    rate = rospy.Rate(10) 
    global derror,derrort,ierror,error,olderror,start
    start = time.time()
    yaw = 123
    value = value1.data

    # print(value)
    # # kp1 = callbackp()
    # print(kp)
    # print(ki)
    # print(kd)
  
    error = value - yaw
  #  print(error)
    p = kp * error
   # print(p)

    derror = error + olderror
   # print(derror)
    stopd = time.time()
    timed = stopd - start
   # print(timed)
    derrort = derror / timed
   # print(derrort)

    d = kd * derrort

  #  print(d)

    ierror = ierror + error

    stopi = time.time()
    timei = stopi-start
    ierrort = ierror * timei
  #  print(ierrort)

    i = 0 * ierrort
 #   print(i)
    
    olderror = error
    finalyaw = p + i + d

   # error1 = error
 #   pub.publish(finalyaw)
    print("final value=" ,finalyaw)
    if(error < 0):
        leftmotor = 200 +finalyaw
        if(leftmotor > 255):
            leftmotor = 255
        rightmotor = 200
        finalsp = leftmotor*1000 + 200
        final = int(finalsp)
        finalspeed = str(final) 
        print(finalspeed) 
        ser.write(finalspeed)
        ser.write('/n')   


    if(error > 0):
        rightmotor = 200 + finalyaw
        if(rightmotor > 255):
            rightmotor = 255
        leftmotor = 200 
        finalsp = 200*1000 + rightmotor
        final = int(finalsp)
        finalspeed = str(final) 
        print(finalspeed) 
        ser.write(finalspeed)
        ser.write('/n')  
  #  time.sleep(1)
    rate.sleep()

def callbackp(Kp1):
  #print(Kp1.data)
  global kp
  kp= (Kp1.data)/1000
 # print(kp)
 # return kp
def callbackd(Kd1):
  global kd 
 # print(Kd1.data)
  kd= (Kd1.data)/100000
#  print(kd)
# def callbacki(Ki1):
#   global ki
#   print(Ki1.data)
#   ki = (Ki1.data)/10000000000000
#   print(ki)


def listener():
    # kp=0
    # ki=0
    # kd=0
    rospy.Subscriber("ahrs",Float64, pid)
    rospy.Subscriber('pitch_kp', Float64 , callbackp) 
    rospy.Subscriber('pitch_kd', Float64 , callbackd) 
 #   rospy.Subscriber('pitch_ki', Float64 , callbacki)
    
    rospy.spin()


if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
