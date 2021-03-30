 #include "ros/ros.h"
 #include <iostream>
 #include <std_msgs/Int32.h>
 #include <std_msgs/Float32.h>
 #include <sensor_msgs/Joy.h>

 using namespace std;
 using namespace ros;

int x;

 std_msgs::Int32 msg_servo;
 std_msgs::Int32 msg_sl;
 std_msgs::Float32 msg_fr;
std_msgs::Float32 msg_fl;
std_msgs::Float32 msg_br;
std_msgs::Float32 msg_bl;
 std_msgs::Int32 msg_sr;
 char joy_check;



float check_straight, check_left, check_right, check_straightback, check_straightfront,up,down;
float check_depth, check_arm_open, check_arm_close;

class rov_controller
{
public:

 rov_controller()
  {
    pub_sl    = nh.advertise<std_msgs::Int32>("sl", 1);
    pub_sr    = nh.advertise<std_msgs::Int32>("sr", 1);
pub_fr    = nh.advertise<std_msgs::Float32>("fr", 1);
pub_fl    = nh.advertise<std_msgs::Float32>("fl", 1);
pub_br   = nh.advertise<std_msgs::Float32>("br", 1);
pub_bl    = nh.advertise<std_msgs::Float32>("bl", 1);
    pub_servo = nh.advertise<std_msgs::Int32>("joy_servo", 1);
    sub_joy   = nh.subscribe("joy", 1, &rov_controller::callback_joy, this);
  }



  void callback_joy(const sensor_msgs::Joy& joy)
  {
  	check_straight 		=	joy.axes[2];
	  check_left			=	joy.buttons[3];
	  check_right 		=	joy.buttons[1];
	  check_straightback  =	joy.buttons[0];
	  check_straightfront =	joy.buttons[2];
	  check_arm_open		=	joy.buttons[7];
	  check_arm_close		=	joy.buttons[6];
            up=joy.axes[1];
            down=joy.buttons[5];
/*.......checking which key is pressed in the joystick.....*/

if(joy.axes[1]==1)
{ ROS_INFO("down");
msg_br.data=1350;
msg_bl.data=1350;
msg_fr.data=1350;
msg_fl.data=1350;
pub_br.publish(msg_br);
pub_bl.publish(msg_bl);
pub_fr.publish(msg_fr);
pub_fl.publish(msg_fl);
}

if(joy.axes[1]==-1)
{ 
 ROS_INFO("up");
msg_br.data=1650;
msg_bl.data=1650;
msg_fr.data=1650;
msg_fl.data=1650;
pub_br.publish(msg_br);
pub_bl.publish(msg_bl);
pub_fr.publish(msg_fr);
pub_fl.publish(msg_fl);

}


if(joy.buttons[2]==1)
{ 
 ROS_INFO("stop depth");
msg_br.data=1500;
msg_bl.data=1500;
msg_fr.data=1500;
msg_fl.data=1500;
pub_br.publish(msg_br);
pub_bl.publish(msg_bl);
pub_fr.publish(msg_fr);
pub_fl.publish(msg_fl);

}

	if(check_straight>0 && check_straightback==1)
	{
		ROS_INFO("Forward");
		msg_sl.data=1275;
		msg_sr.data=1275;
		pub_sl.publish(msg_sl);
		pub_sr.publish(msg_sr);
	}

	


	if(check_straight==0 && check_straightback==0 && check_left==0 && check_right==0 )
	{
		ROS_INFO("stop");
		msg_sl.data=1500;
		msg_sr.data=1500;





		pub_sl.publish(msg_sl);
		pub_sr.publish(msg_sr);
	}
	if(check_straight<0 && check_straightfront==1)
	{
		ROS_INFO("Backward");
		msg_sl.data=1650;
		msg_sr.data=1650;
		pub_sl.publish(msg_sl);
		pub_sr.publish(msg_sr);
	}

	if(check_left>(0.5))
	{
		ROS_INFO("left");
    msg_sl.data =  1600;
    msg_sr.data =  1400;
		pub_sl.publish(msg_sl);
		pub_sr.publish(msg_sr);

	}
	if(check_right>(0.5))


	{
		ROS_INFO("Right");
		msg_sl.data =  1400;
    msg_sr.data =  1600;
		pub_sl.publish(msg_sl);
		pub_sr.publish(msg_sr);
	}
	if(check_arm_open==1)
	 {
	 	ROS_INFO("Arm Opens");
if(x<180)
{x=x+10;}
else
{x=180;}
  msg_servo.data = x;
    pub_servo.publish(msg_servo);
	 }
  
	if(check_arm_close==1)
	 {   	 	ROS_INFO("Arm Opens");
   if(x>0)
  {x=x-10;}
else
{x=0;}
	 	ROS_INFO("Arm Closes");
   msg_servo.data = x;
     pub_servo.publish(msg_servo);
	 }
  }

private:
  ros::NodeHandle nh;
ros::Publisher pub_fl;
  ros::Publisher pub_fr;
ros::Publisher pub_bl;
  ros::Publisher pub_br;
  ros::Publisher pub_sl;
  ros::Publisher pub_sr;
  ros::Publisher pub_servo;
  ros::Subscriber sub_joy;


};

int main(int argc, char **argv)
{

  ros::init(argc, argv, "rov_control");
  rov_controller control_object;
  ros::spin();
  return 0;
}
