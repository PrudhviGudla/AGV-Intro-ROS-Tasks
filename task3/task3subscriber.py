#!/usr/bin/env python
import rospy

from geometry_msgs.msg  import Twist

import numpy as np
  
k = np.random.normal(size=(20300))

i= -1
    
def callback(data):
    

    rospy.loginfo(" without noise data.linear.x = %s ", data.linear.x)
    global i
    i += 1
    
    data.linear.x += k[i]
    data.linear.y += k[i]
    data.linear.z += k[i]
    data.angular.x += k[i]
    data.angular.y += k[i]
    data.angular.z += k[i]
    
    rospy.loginfo(" after adding noise = %s ", data.linear.x )
    rospy.loginfo("%s ", data.linear.y )
    rospy.loginfo("%s ", data.linear.z )
    rospy.loginfo("%s ", data.angular.x )
    rospy.loginfo("%s ", data.angular.y )
    rospy.loginfo("%s ", data.angular.z )
    
    
    
def task3subscriber():

    rospy.init_node('task3s', anonymous=True)

    rospy.Subscriber("cmd_vel", Twist, callback)

    rospy.spin()

if __name__ == '__main__':
    task3subscriber()
