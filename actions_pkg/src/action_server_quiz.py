#!/usr/bin/env python

import rospy
import actionlib

from ardrone_as.msg import ArdroneAction, ArdroneActionFeedback, ArdroneActionResult


class ArdroneActionServer:
    def _init_(self):
        self.server = actionlib.SimpleActionServer('ardrone_action', ArdroneAction, self.execute, False)
        self.server.start()
        rospy.loginfo('Ardrone Action Server Started')
    
    def execute(self, goal):
        success = False
        rate = rospy.Rate(1) # 1Hz
        
        if goal.goal == ArdroneAction.TAKEOFF:
            rospy.loginfo('Ardrone Takeoff Action Started')
            feedback = ArdroneActionFeedback()
            feedback.current_action = ArdroneAction.TAKEOFF
            
            for i in range(100):
                feedback.percent_complete = i
                self.server.publish_feedback(feedback)
                rate.sleep()
            success = True
        elif goal.goal == ArdroneAction.LAND:
            rospy.loginfo('Ardrone Land Action Started')
            feedback = ArdroneActionFeedback()
            feedback.current_action = ArdroneAction.LAND
            
            for i in range(100):
                feedback.percent_complete = i
                self.server.publish_feedback(feedback)
                rate.sleep()
            success = True
        
        if success:
            result = ArdroneActionResult()
            result.success = True
            self.server.set_succeeded(result)
        else:
            self.server.set_aborted()
        
if _name_ == '_main_':
    rospy.init_node('ardrone_action_server')
    server = ArdroneActionServer()
    rospy.spin()