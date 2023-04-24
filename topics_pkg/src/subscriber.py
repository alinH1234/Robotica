#! /usr/bin/env python

import rospy                                          
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(sensor_msgs):                            	# Define a function called 'callback' that receives a parameter named 'msg'
    if sensor_msgs.ranges[360] > 1:
        move.linear.x = 0.5
        move.angular.z = 0.0
    if sensor_msgs.ranges[360] < 1:
        move.linear.x = 0.0
        move.angular.z = 0.5
    if sensor_msgs.ranges[0] < 1:
        move.linear.x = 0.0
        move.angular.z = 0.5
    if sensor_msgs.ranges[720] < 1:
        move.linear.x = 0.0
        move.angular.z = -0.5

rospy.init_node('topic_subscriber')                   	
sub = rospy.Subscriber('/scan', LaserScan, callback)   
pub = rospy.Publisher('/cmd_vel',Twist)  

move = Twist()
                                                
rospy.spin()                                          