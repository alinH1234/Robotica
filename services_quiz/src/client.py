import rospy
from std_srvs.srv import ServMess, ServMessRequest

if _name_ == '_main_':
    rospy.init_node('square_service_client')
    rospy.wait_for_service('move_in_square')

        move_in_square = rospy.ServiceProxy('move_in_square', Empty)

        response = move_in_square(EmptyRequest())

        rospy.loginfo('Square movement completed')