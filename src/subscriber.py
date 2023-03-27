#! /usr/bin/env python

import rospy                                          
from sensor_msgs.msg import LaserScan

def callback(sensor_msgs):                            	# Define a function called 'callback' that receives a parameter named 'msg'
    print (sensor_msgs.ranges)                            	# Print the value 'data' inside the 'msg' parameter

rospy.init_node('topic_subscriber')                   	# Initiate a Node called 'topic_subscriber'
sub = rospy.Subscriber('/scan', LaserScan, callback)   	# Create a Subscriber object that will listen to the /counter
                                                      			# topic and will call the 'callback' function each time it reads
                                                      			# something from the topic
rospy.spin()                                          			# Create a loop that will keep the program in execution
