#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def cb(message):
    rospy.loginfo(message.data*5)
    rospy.loginfo('---------------------------')

if __name__ == '__main__': 
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', Int32, cb) 
    rospy.spin()
