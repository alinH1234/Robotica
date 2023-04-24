#! /usr/bin/env python
import rospy
rospy.init_node("Friends")
rate = rospy.Rate(2) # We create a Rate object of 2Hz
while not rospy.is_shutdown(): # Endless loop until Ctrl + C
	print("How you doooin?")
	rate.sleep() # We sleep the needed time to maintain the Rate fixed above
# This program creates an endless loop that repeats itself 2 times per second (2Hz) until somebody presses Ctrl + C in the Shell
