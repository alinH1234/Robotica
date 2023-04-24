#! /usr/bin/env python
import rospy
import time
# Import the service message used by the service /trajectory_by_name
from services_pkg.srv import CustomServMess, CustomServMessResponse
from geometry_msgs.msg import Twist

def duration_response(request):
    print(f"Robotul se va misca in cerc pentru {request.duration} secunde")
    current_time = time.time()
    while(time.time()<current_time + request.duration):	
        rospy.loginfo("Service move in circle has been called")
        vel.linear.x = 0.2
        vel.angular.z = 1
        pub.publish(vel)
    vel.linear.x = 0
    vel.angular.z = 0
    pub.publish(vel)
    move_in_square_response.success=True


    return move_in_square_response


rospy.init_node('service_server')
move_in_square_response = CustomServMessResponse()
my_service = rospy.Service('/move_in_square_duration',CustomServMess,duration_response)
pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)
vel = Twist()
rate = rospy.Rate(2)
rospy.spin()
