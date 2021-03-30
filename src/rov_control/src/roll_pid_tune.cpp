/*     ROS NODE FOR AUV TO STABILIZE PITCH
      AUTHOR : NIKESH KRISHNAN
ORGANIZATION : RIGNITC*/

#include <ros/ros.h>

#include <sstream>
#include "std_msgs/Int8.h"
#include "std_msgs/Char.h"
#include "std_msgs/Int64.h"      
#include "std_msgs/Float32.h"


using namespace std;

float kp,kd,ki,pitch,previous_error,sum_error=0,diff_error,pwm,error;
float setpoint=0;

std_msgs::Char cmd;
//ros::Subscriber<std_msgs::Float32> sub_kp("pitch_kp", &chatterCallback_kp);
//ros::Subscriber<std_msgs::Float32> sub_kd("pitch_kd", &chatterCallback_kd);
//ros::Subscriber<std_msgs::Float32> sub_ki("pitch_ki", &chatterCallback_ki);
//ros::Subscriber<std_msgs::Float32> sub_pitch("orientation_pitch", &chatterCallback_pitch);

class pitch_pid
{private:

    ros::NodeHandle nh;
    ros::Publisher cmd_pwm_front_right;
    ros::Publisher cmd_pwm_back_left;
    ros::Publisher cmd_pwm_front_left;
    ros::Publisher cmd_pwm_back_right;
    ros::Subscriber sub_kd;
    ros::Subscriber sub_kp;
    ros::Subscriber sub_ki;
    ros::Subscriber sub_pitch;	


  	public:
	pitch_pid()
		
		{cout<<"intializing_variables"<<"\n";
	      sub_pitch = nh.subscribe("orientation_pitch",1, &pitch_pid::chatterCallback_pitch,this);	        
              sub_kp = nh.subscribe("pitch_kp",10, &pitch_pid::chatterCallback_kp,this);
              sub_kd = nh.subscribe("pitch_kd",10, &pitch_pid::chatterCallback_kd,this);
    	      sub_ki = nh.subscribe("pitch_ki",10, &pitch_pid::chatterCallback_ki,this);     
              cmd_pwm_front_left   = nh.advertise<std_msgs::Float32>("fl", 1000);
              cmd_pwm_back_left   = nh.advertise<std_msgs::Float32>("bl", 1000);
              cmd_pwm_back_right   = nh.advertise<std_msgs::Float32>("br", 1000);
              cmd_pwm_front_right   = nh.advertise<std_msgs::Float32>("fr", 1000);
		}

    void chatterCallback_kp(const std_msgs::Float32& message)
    {
      kp = message.data;
  
    }

    void chatterCallback_kd(const std_msgs::Float32& message)
    {
      kd = message.data;
    }

  void chatterCallback_ki(const std_msgs::Float32& message)
    {
      ki =  message.data;
    }


 void chatterCallback_pitch(const std_msgs::Float32& message)
    { cout<<"computing pid"<<"\n";
      pitch = message.data;
     
    /*pwm computing using pid*/
      float dummy = setpoint-pitch;
       if(dummy<=-3.6||dummy>=3.6)
      { error=dummy;
      sum_error=sum_error+error;
      diff_error=error-previous_error;
      pwm = kp*error+ki*sum_error+kd*diff_error;
      previous_error=error;
      }
    /*******************************/     
      else if(dummy>=-3.6&&dummy<=3.6)
     {pwm=0;}

      std_msgs::Float32 msg_front_left; 
      std_msgs::Float32 msg_back_left; 
      std_msgs::Float32 msg_front_right; 
      std_msgs::Float32 msg_back_right; 
    
      msg_front_left.data=1500+pwm;
      msg_front_right.data=1500+pwm;
      msg_back_left.data=1500-pwm;
      msg_back_right.data=1500-pwm;
       cout<<"kp "<< kp<<"\n";
       cout<<"ki "<<ki<<"\n";
       cout<<"kd "<<kd<<"\n";
       cout<<"DUMMY ERROE "<<dummy<<"\n";
       cout<<"ERROR"<<error<<"\n";


 
       cout<<"fl "<< msg_front_left.data<<"\n";
       cout<<"fr "<<msg_front_right.data<<"\n";
       cout<<"bl "<<msg_back_left.data<<"\n";
       cout<<"br "<<msg_back_right.data<<"\n";
       cmd_pwm_front_left.publish(msg_front_left);
       cmd_pwm_front_right.publish(msg_front_right);
       cmd_pwm_back_left.publish(msg_back_left);
       cmd_pwm_back_right.publish(msg_back_right);

    
    }


	

        


	


};

int main(int argc, char** argv)
	{   
  		ros::init(argc,argv,"pitch_pid_tune");
  		pitch_pid object;
     
  		ros::spin();		return 0;  

	}
