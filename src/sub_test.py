#! /usr/bin/env python

import rospy                                          
from geometry_msgs.msg import Twist 

def callback(geometry_msgs):                            	# Define a function called 'callback' that receives a parameter named 'msg'
    print (geometry_msgs.linear.x)                            	# Print the value 'data' inside the 'msg' parameter

rospy.init_node('topic_subscriber')                   	# Initiate a Node called 'topic_subscriber'
sub = rospy.Subscriber('/cmd_vel', Twist, callback)   	# Create a Subscriber object that will listen to the /counter
                                                      			# topic and will call the 'callback' function each time it reads
                                                      			# something from the topic
rospy.spin()                                          			# Create a loop that will keep the program in execution