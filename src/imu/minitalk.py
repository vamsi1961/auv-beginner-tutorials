import rospy

from Tkinter import *
from std_msgs.msg import String
global mag 
global pub1 
global pub2   
global then 
#mag = String()
rospy.init_node('talker', anonymous = True)
global mot1
global mot2

pub1 = rospy.Publisher('topic1',String,queue_size=10)
pub2 = rospy.Publisher('topic2',String,queue_size=10)

def talker():

  rate = rospy.Rate(10)
  rate.sleep()
  then = rospy.Time.now()
  
  mot1 = 200
  mot2 = 200
 
  pub1.publish(mot1)
  pub1.publish(mot2)
      
#def callback(mag):

  def show_values():
 
    Kp1 = w1.get()
    Ki1 = w2.get()
    Kd1 = w3.get()
    Kp2 = d1.get()
    Ki2 = d2.get()
    Kd2 = d3.get()

    print (Kp1,Ki1,Kd1,Kp2,Ki2,Kd2)

  master = Tk()
  w1 = Scale(master, from_=0, to= 100, orient=HORIZONTAL)
  w1.set(0)
  w1.pack()
  w2 = Scale(master, from_=0, to=100, orient=HORIZONTAL)
  w2.set(0)
  w2.pack()
  w3 = Scale(master, from_=0, to=100, orient=HORIZONTAL)
  w3.set(0)
  w3.pack()

  d1 = Scale(master, from_=0, to= 100, orient=HORIZONTAL)
  d1.set(0)
  d1.pack()
  d2 = Scale(master, from_=0, to=100, orient=HORIZONTAL)
  d2.set(0)
  d2.pack()
  d3 = Scale(master, from_=0, to=100, orient=HORIZONTAL)
  d3.set(0)
  d3.pack()

  Button(master, text='Show', command=show_values).pack()

  mainloop()

#print(mag.data) 
#  lasterror = 0
  now = rospy.Time.now()
  t = now-then 
  e = 100 - (mag.data)

#Proportional term
  p = Kp1 * e
    
#Integral term
  sum = 0
  sum =  sum + e 
  i = Ki1 * (sum * t) 

# Derivative term
  d = Kd1 * ( (e - lastError)/t )       
  
  lastError = e 
   
  motorSpeed = p + i + d 
  
  motor1 = int(mot1) + motorSpeed 
 
  if (motor1 > 255): 
     fsp = 255
  else:
     fsp = motor1

  lasterror2 = 0
  now2 = rospy.Time.now()
  t2 = now2-then 
  e2 = 100 - (mag.data)
  #Proportional term
  p = Kp2 * e2
  
  #Integral term
  sum2 = 0
  sum2 = sum2 + e2
  i = Ki2 * (sum2 * t2 )  

 # Derivative term
  d = Kd2 * ( (e2 - lastError)/t2 )       
  lasterror2 = e2

  motorSpeed2 = p + i + d 

  motor2 = int(mot2) - motorSpeed 

  if (motor2 > 255): 
     fsp2 = 255
  else:
     fsp2 = motor2

  pub1.publish(fsp)
  print(fsp)
  pub2.publish(fsp2)
  print(fsp2)

 
rospy.Subscriber('topic3', String , callback) 

if __name__=='__main__':
   try:
     talker()
   except rospy.ROSInterruptException:
      pass    