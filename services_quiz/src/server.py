#!/usr/bin/env python

import rospy
from services_pkg.srv import CustomServMess, CustomServMessResponse
from geometry_msgs.msg import Twist

class SquareServiceServer:
    def _init_(self):
        rospy.init_node('square_service_server')

        self.square_service = rospy.Service('move_in_square', ServMess, self.move_in_square)

        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

    def move_in_square(self, request):
        linear_velocity = 0.2
        angular_velocity = 0.2

        side_duration = 5.0

        num_sides = 4

        cmd_vel = Twist()

        for i in range(num_sides):
            cmd_vel.linear.x = linear_velocity
            cmd_vel.linear.y = 0.0
            cmd_vel.linear.z = 0.0

            cmd_vel.angular.x = 0.0
            cmd_vel.angular.y = 0.0
            cmd_vel.angular.z = angular_velocity

            self.cmd_vel_pub.publish(cmd_vel)

            rospy.sleep(side_duration)

        cmd_vel.linear.x = 0.0
        cmd_vel.angular.z = 0.0
        self.cmd_vel_pub.publish(cmd_vel)

        return ServMessResponse()

if __name__ == '__main__':
    server = SquareServiceServer()
    rospy.spin()