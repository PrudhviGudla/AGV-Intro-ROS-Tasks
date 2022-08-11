#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def dummypublisher():
    pub = rospy.Publisher('dummy', String, queue_size=10)
    rospy.init_node('dummypublisher', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        dummy_str = "heeeeelo %s" % rospy.get_time()
        rospy.loginfo(dummy_str)
        pub.publish(dummy_str)
        rate.sleep()
        	
if __name__ == '__main__':
    try:
        dummypublisher()
    except rospy.ROSInterruptException:
        pass
        
        

