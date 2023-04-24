#! /usr/bin/env python
import rospy
# Import the service message used by the service /trajectory_by_name
from services_pkg.srv import CustomServMess, CustomServMessRequest
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('service_client')
# Wait for the service client /move_in_square to be running
rospy.wait_for_service('/move_in_square_duration')
# Create the connection to the service
move_in_square_service = rospy.ServiceProxy('/move_in_square_duration', CustomServMess)
# Create an object of type MoveInSquareRequest
move_in_square_object = CustomServMessRequest()
move_in_square_object.duration = 20
  
# Send through the connection the name of the request
result = move_in_square_service(move_in_square_object)
# Print the result given by the service called
print(result)