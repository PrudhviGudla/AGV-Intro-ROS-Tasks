#!/usr/bin/env python
import rospy

from geometry_msgs.msg  import Twist

#from std_msgs.msg import Float64

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    #velocity = data.data
    
def task3subscriber():

    rospy.init_node('task3subscriber', anonymous=True)

    rospy.Subscriber("cmd_vel", Twist, callback)

    rospy.spin()

if __name__ == '__main__':
    task3subscriber()
