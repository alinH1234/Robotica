#! /usr/bin/env python

import rospy                                          
from topics_pkg.msg import Age 

def callback(msg):
    print(['An','Luna','Zi'])                            	# Define a function called 'callback' that receives a parameter named 'msg'
    print ([msg.year,msg.months,msg.days])                            	# Print the value 'data' inside the 'msg' parameter

rospy.init_node('topic_subscriber')                   	# Initiate a Node called 'topic_subscriber'
sub = rospy.Subscriber('/Age_topic', Age, callback)   	# Create a Subscriber object that will listen to the /counter
                                                      			# topic and will call the 'callback' function each time it reads
                                                      			# something from the topic
rospy.spin()                                          			# Create a loop that will keep the program in execution