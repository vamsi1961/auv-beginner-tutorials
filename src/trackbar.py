#TRACK BAR FOR TUNING PID OF AUV PITCH
#AUTHOR:NIKESH KRISHNAN
#ORGANISTAION:TEAM AUV RIGNITC
#!/usr/bin/python
from Tkinter import *
from std_msgs.msg import Float64
import rospy
import time

rospy.init_node('tune_pid')

# send_pid_roll = rospy.Publisher('/pid_tuning_roll', PidTune, queue_size=10)

# pid_value = PidTune()



class Pitch():
	def __init__(self):
		self.send_pid_pitch_kp = rospy.Publisher('pitch_kp', Float64, queue_size=10)
                self.send_pid_pitch_ki = rospy.Publisher('pitch_ki', Float64, queue_size=10)
                self.send_pid_pitch_kd = rospy.Publisher('pitch_kd', Float64, queue_size=10)
		self.pid_value_pitch_kp = Float64()
                self.pid_value_pitch_ki = Float64()
                self.pid_value_pitch_kd = Float64()

		self.root = Tk()
		self.root.title("Pitch")

		self.scale = Scale(self.root, orient='horizontal', from_=0.00, to=100.00,resolution=0.01, label= 'Kp',width = "50", length = "500",troughcolor="red")
		self.scale1 =Scale(self.root, orient='horizontal', from_=0.00, to=100.00,resolution=0.01, label= 'Ki',width = "50", length = "500",troughcolor="green")
		self.scale2 =Scale(self.root, orient='horizontal', from_=0.00, to=100.00,resolution=0.01, label= 'Kd',width = "50", length = "500", troughcolor="blue")
		# scale3 =Scale(root, orient='horizontal', from_=0, to=300, label= 'Kp_z',width = "50", length = "500", troughcolor="gray")
		self.scale.pack()
		self.scale1.pack()
		self.scale2.pack()
		# scale3.pack()

		Button(self.root, text='set_value', command=self.set_value).pack()

	#root.mainloop()

	def set_value(self):

		self.pid_value_pitch_kp.data = self.scale.get()
		self.pid_value_pitch_ki.data = self.scale1.get()
		self.pid_value_pitch_kd.data = self.scale2.get()
		# pid_value.Kp_z = scale3.get()
		self.send_pid_pitch_kp.publish(self.pid_value_pitch_kp)
                self.send_pid_pitch_ki.publish(self.pid_value_pitch_ki)
                self.send_pid_pitch_kd.publish(self.pid_value_pitch_kd)
		# print scale.get(), scale1.get(), scale2.get()
		# print "send",self.pid_value_pitch
		# print "\n"
class Roll():
	def __init__(self):
		self.send_pid_roll = rospy.Publisher('/pid_tuning_roll', PidTune, queue_size=10)
		self.pid_value_roll = PidTune()

		self.root = Tk()
		self.root.title("Roll")

		self.scale = Scale(self.root, orient='horizontal', from_=0, to=5000, label= 'Kp',width = "50", length = "500",troughcolor="red")
		self.scale1 =Scale(self.root, orient='horizontal', from_=0, to=5000, label= 'Ki',width = "50", length = "500",troughcolor="green")
		self.scale2 =Scale(self.root, orient='horizontal', from_=0, to=5000, label= 'Kd',width = "50", length = "500", troughcolor="blue")
		# scale3 =Scale(root, orient='horizontal', from_=0, to=300, label= 'Kp_z',width = "50", length = "500", troughcolor="gray")
		self.scale.pack()
		self.scale1.pack()
		self.scale2.pack()
		# scale3.pack()

		Button(self.root, text='set_value', command=self.set_value).pack()

	#root.mainloop()

	def set_value(self):

		self.pid_value_roll.Kp = self.scale.get()
		self.pid_value_roll.Ki = self.scale1.get()
		self.pid_value_roll.Kd = self.scale2.get()
		# pid_value.Kp_z = scale3.get()
		self.send_pid_roll.publish(self.pid_value_roll)
		# print scale.get(), scale1.get(), scale2.get()
		# print "send",self.pid_value_roll
		# print "\n"


class Altitude():
	def __init__(self):
		self.send_pid_altitude = rospy.Publisher('/pid_tuning_altitude', PidTune, queue_size=10)
		self.pid_value_altitude = PidTune()

		self.root = Tk()
		self.root.title("Altitude")

		self.scale = Scale(self.root, orient='horizontal', from_=0, to=5000, label= 'Kp',width = "50", length = "500",troughcolor="red")
		self.scale1 =Scale(self.root, orient='horizontal', from_=0, to=5000, label= 'Ki',width = "50", length = "500",troughcolor="green")
		self.scale2 =Scale(self.root, orient='horizontal', from_=0, to=5000, label= 'Kd',width = "50", length = "500", troughcolor="blue")
		# scale3 =Scale(root, orient='horizontal', from_=0, to=300, label= 'Kp_z',width = "50", length = "500", troughcolor="gray")
		self.scale.pack()
		self.scale1.pack()
		self.scale2.pack()
		# scale3.pack()

		Button(self.root, text='set_value', command=self.set_value).pack()

	#root.mainloop()

	def set_value(self):

		self.pid_value_altitude.Kp = self.scale.get()
		self.pid_value_altitude.Ki = self.scale1.get()
		self.pid_value_altitude.Kd = self.scale2.get()
		# pid_value.Kp_z = scale3.get()
		self.send_pid_altitude.publish(self.pid_value_altitude)
		# print scale.get(), scale1.get(), scale2.get()
		# print "send",self.pid_value_altitude
		# print "\n"

class Yaw():
	def __init__(self):
		self.send_pid_yaw = rospy.Publisher('/pid_tuning_yaw', PidTune, queue_size=10)
		self.pid_value_yaw = PidTune()

		self.root = Tk()
		self.root.title("Yaw")

		self.scale = Scale(self.root, orient='horizontal', from_=0, to=5000, label= 'Kp',width = "50", length = "500",troughcolor="red")
		self.scale1 =Scale(self.root, orient='horizontal', from_=0, to=5000, label= 'Ki',width = "50", length = "500",troughcolor="green")
		self.scale2 =Scale(self.root, orient='horizontal', from_=0, to=5000, label= 'Kd',width = "50", length = "500", troughcolor="blue")
		# scale3 =Scale(root, orient='horizontal', from_=0, to=300, label= 'Kp_z',width = "50", length = "500", troughcolor="gray")
		self.scale.pack()
		self.scale1.pack()
		self.scale2.pack()
		# scale3.pack()

		Button(self.root, text='set_value', command=self.set_value).pack()

	#root.mainloop()

	def set_value(self):

		self.pid_value_yaw.Kp = self.scale.get()
		self.pid_value_yaw.Ki = self.scale1.get()
		self.pid_value_yaw.Kd = self.scale2.get()
		# pid_value.Kp_z = scale3.get()
		self.send_pid_yaw.publish(self.pid_value_yaw)
		# print scale.get(), scale1.get(), scale2.get()
		# print "send",self.pid_value_yaw
		# print "\n"


pitch = Pitch()
##roll = Roll()
#altitude = Altitude()
#yaw = Yaw()

def quit(event):
	pitch.root.quit()

if __name__ == '__main__':

	# while pitch.root.mainloop():
	# 	try:
	# 		time.sleep(0.5)
	# 	except KeyboardInterrupt:
	# 		pitch.root.quit()
	# 		break
	pitch.root.bind('<Control-c>',quit)
	#roll.root.bind('<Control-c>',quit)
	#altitude.root.bind('<Control-c>',quit)
	#yaw.root.bind('<Control-c>',quit)
	pitch.root.mainloop()
	# roll = Roll()
