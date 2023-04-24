#! /usr/bin/env python
import rospy 
from geometry_msgs.msg import Twist 
from sensor_msgs.msg import LaserScan

rospy.init_node('topic_publisher') # Initiate a Node named 'topic_publisher'
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) # Create a Publisher object, that will publish on the /counter topic
# messages of type Int32

rate = rospy.Rate(2) # Set a publish rate of 2 Hz
count = Twist() # Create a var of type Int32
count.linear.x = 1 
count.angular.z = 0

while not rospy.is_shutdown(): # Create a loop that will go until someone stops the program execution
    if sensor_msgs.ranges > 0:
        pub.publish(count) # Publish the message within the 'count' variable
        count.angular.z += 0.5 # Increment 'count' variable
        rate.sleep() # 